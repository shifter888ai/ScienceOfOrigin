# Cloudflare Workers AI setup for the Ask page

The Ask page uses a Cloudflare Pages Function at `functions/api/ask.js` and a Workers AI binding named `AI`.

## One-time dashboard setup

1. Open Cloudflare Dashboard → Workers & Pages.
2. Open the Science of Origin Pages project.
3. Go to **Settings → Bindings**.
4. Select **Add → Workers AI**.
5. Set the variable name to exactly `AI`.
6. Add the binding to the **Production** environment. Add it to **Preview** too if preview deployments will be tested.
7. Save the binding and redeploy the Pages project after the code has been merged.

The function uses Google's `@cf/google/gemma-4-26b-a4b-it` model through the binding. No API key or other secret is needed in the website code.

## How it works

- The browser sends the conversation to `/api/ask`.
- The Pages Function searches the site's `search-index.json`, retrieves up to four relevant research pages, and includes their text as reference context.
- Workers AI generates the answer. The page displays links to the retrieved source pages.
- The function limits message sizes and conversation history, rejects cross-origin browser requests, and returns a clear message if the AI allowance is unavailable.

## Usage allowance

Workers AI Free includes a daily Neurons allowance. If it is exhausted, the Ask endpoint returns a temporary usage-limit message. No paid upgrade or automatic billing change is configured by this project.

## Local testing

Use Wrangler Pages local development with an AI binding:

```sh
npx wrangler pages dev dist --ai AI
```

Workers AI local development still uses the Cloudflare account's Workers AI service and counts toward its usage.
