import { defineConfig } from 'astro/config';

export default defineConfig({
  site: 'https://zugbot.net',
  publicDir: './.generated/public',
  output: 'static',
  devToolbar: { enabled: false },
  build: { assets: '_zugbot', inlineStylesheets: 'never' },
});
