# ZugBot website

This repository builds the public product site and field manual for ZugBot. Discord runs the Activity. The website serves static pages, guides, and labeled local demonstrations.

## Run it locally

Use Node 24.22.3 and Python 3.13. From the repository root with a Python environment active:

```sh
python -m pip install -r requirements.txt
npm --prefix homepage ci
python homepage/build.py
python homepage/preview.py
```

Open the loopback address printed by the preview server. The default is `http://127.0.0.1:4321/`. Use `--port` for another port. The full build checks article content, routes, canonical URLs, fragments, static assets, search and both sitemaps.

For frontend editing, run `npm --prefix homepage run dev` after installing dependencies. It prepares the MkDocs data before starting Astro's dev server. Rerun preparation after editing guide Markdown. The production-equivalent preview uses `homepage/dist/`. The npm build and preview commands also work with an active Python environment or a `PYTHON` environment variable pointing to its interpreter.

## Review and release

The Pages workflow builds the complete site and attaches a downloadable static preview to the run. Deployment requires an explicit manual workflow run from `main` with the publish input enabled. See [architecture, URL ownership and release notes](homepage/README.md).
