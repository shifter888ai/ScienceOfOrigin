(() => {
  const form = document.getElementById('chat-form');
  const input = document.getElementById('chat-input');
  const log = document.getElementById('chat-log');
  const status = document.getElementById('chat-status');
  const send = document.getElementById('chat-send');
  if (!form || !input || !log || !status || !send) return;

  const messages = [];

  // Convert escaped Markdown punctuation back to its intended form.
  // Rendering is performed with DOM text nodes; model output is never HTML.
  const normalizeMarkdown = value =>
    String(value).replace(/\\([\\\x60*_{}\[\]()#+.!|>~-])/g, '$1');

  const appendInline = (parent, value) => {
    const parts = String(value).split(/(\\*\\*[^*]+?\\*\\*|\\*[^*]+?\\*)/g);
    for (const part of parts) {
      if (!part) continue;
      if (part.startsWith('**') && part.endsWith('**')) {
        const strong = document.createElement('strong');
        strong.textContent = part.slice(2, -2);
        parent.append(strong);
      } else if (part.startsWith('*') && part.endsWith('*')) {
        const emphasis = document.createElement('em');
        emphasis.textContent = part.slice(1, -1);
        parent.append(emphasis);
      } else {
        parent.append(document.createTextNode(part));
      }
    }
  };

  const renderAnswer = (container, content) => {
    const lines = normalizeMarkdown(content).replace(/\r\n?/g, '\n').split('\n');
    let paragraph = [];
    let list = null;
    let listKind = '';

    const flushParagraph = () => {
      if (!paragraph.length) return;
      const block = document.createElement('p');
      paragraph.forEach((line, index) => {
        if (index) block.append(document.createElement('br'));
        appendInline(block, line);
      });
      container.append(block);
      paragraph = [];
    };

    const flushList = () => {
      list = null;
      listKind = '';
    };

    for (const rawLine of lines) {
      const line = rawLine.trim();
      if (!line) {
        flushParagraph();
        flushList();
        continue;
      }

      const heading = line.match(/^#{1,3}\s+(.+)$/) ||
        line.match(/^\\*\\*(.+)\\*\\*$/);
      if (heading) {
        flushParagraph();
        flushList();
        const element = document.createElement('h4');
        appendInline(element, heading[1]);
        container.append(element);
        continue;
      }

      const bullet = line.match(/^[-*]\s+(.+)$/);
      const numbered = line.match(/^\d+[.)]\s+(.+)$/);
      if (bullet || numbered) {
        flushParagraph();
        const kind = bullet ? 'ul' : 'ol';
        if (!list || listKind !== kind) {
          flushList();
          list = document.createElement(kind);
          listKind = kind;
          container.append(list);
        }
        const item = document.createElement('li');
        appendInline(item, (bullet || numbered)[1]);
        list.append(item);
        continue;
      }

      flushList();
      paragraph.push(line);
    }
    flushParagraph();
  };

  const addMessage = (role, content, sources) => {
    const article = document.createElement('div');
    article.className = 'chat-message ' + role;
    const label = document.createElement('span');
    label.className = 'chat-role';
    label.textContent = role === 'user' ? 'You' : 'Science of Origin AI';
    const text = document.createElement('div');
    if (role === 'assistant') {
      text.className = 'chat-answer';
      renderAnswer(text, content);
    } else {
      text.textContent = content;
    }
    article.append(label, text);
    if (Array.isArray(sources) && sources.length) {
      const list = document.createElement('ul');
      list.className = 'chat-sources';
      for (const source of sources) {
        if (!source || typeof source.url !== 'string' || typeof source.title !== 'string') continue;
        const item = document.createElement('li');
        const link = document.createElement('a');
        link.href = source.url;
        link.textContent = source.title;
        item.append(link);
        list.append(item);
      }
      if (list.children.length) article.append(list);
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
