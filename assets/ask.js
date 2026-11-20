(() => {
  const form = document.getElementById('chat-form');
  const input = document.getElementById('chat-input');
  const log = document.getElementById('chat-log');
  const status = document.getElementById('chat-status');
  const send = document.getElementById('chat-send');
  if (!form || !input || !log || !status || !send) return;

  const messages = [];
  const addMessage = (role, content, sources) => {
    const article = document.createElement('div');
    article.className = 'chat-message ' + role;
    const label = document.createElement('span');
    label.className = 'chat-role';
    label.textContent = role === 'user' ? 'You' : 'Science of Origin AI';
    const text = document.createElement('div');
    text.textContent = content;
    article.append(label, text);
    if (Array.isArray(sources) && sources.length) {
      const list = document.createElement('ul');
      list.className = 'chat-sources';
      for (const source of sources) {
        const item = document.createElement('li');
        const link = document.createElement('a');
        link.href = source.url;
        link.textContent = source.title;
        item.append(link);
        list.append(item);
      }
      article.append(list);
    }
    log.append(article);
    log.scrollTop = log.scrollHeight;
  };

  form.addEventListener('submit', async event => {
    event.preventDefault();
    const question = input.value.trim();
    if (!question || send.disabled) return;
    messages.push({ role: 'user', content: question });
    addMessage('user', question);
    input.value = '';
    send.disabled = true;
    status.textContent = 'Thinking…';
    try {
      const response = await fetch('/api/ask', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ messages: messages.slice(-8) })
      });
      const data = await response.json().catch(() => ({}));
      if (!response.ok) throw new Error(data.error || 'The AI service is temporarily unavailable.');
      const answer = String(data.answer || 'I could not produce an answer. Please try again.');
      messages.push({ role: 'assistant', content: answer });
      addMessage('assistant', answer, data.sources);
      if (messages.length > 10) messages.splice(0, messages.length - 10);
      status.textContent = '';
    } catch (error) {
      const message = error && error.message ? error.message : 'Something went wrong. Please try again.';
      addMessage('assistant', message);
      status.textContent = 'Your question was not completed.';
    } finally {
      send.disabled = false;
      input.focus();
    }
  });

  input.addEventListener('keydown', event => {
    if (event.key === 'Enter' && !event.shiftKey) {
      event.preventDefault();
      form.requestSubmit();
    }
  });
})();
