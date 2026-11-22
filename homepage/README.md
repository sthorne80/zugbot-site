# ZugBot homepage prototype

This branch previews the proposed product homepage at the custom-domain root. All detailed guides come from the existing MkDocs build. The production workflow still builds only MkDocs.

## Preview locally

Use Node.js 24.22.3 or another version supported by the pinned Astro release, npm, and Python 3.13. Run the following from the repository root, with your preferred Python environment active.

```sh
python -m pip install -r requirements.txt
npm --prefix homepage ci
npm --prefix homepage run build
python homepage/preview.py
```

Open the loopback URL printed by the server. The default is `http://127.0.0.1:4321/`. Stop it with Ctrl+C. Use `--port 4322` to select a different port, or `python homepage/preview.py --check` for a build and compatibility check without serving. Rebuild Astro and restart the preview after editing the homepage. The existing `mkdocs serve` command continues to preview the production design.

## What is in the branch

| Path under `homepage/` | Purpose |
| --- | --- |
| `src/pages/index.astro` | Homepage, navigation, accessible mobile menu, real feature guides, starter commands and support. Imports the existing fortress artwork and v2 emblem directly from `docs/assets/`. |
| `src/styles/home.css` | Responsive hero art direction, typography, feature cards, keyboard focus and reduced-motion styles. |
| `package.json`, `package-lock.json`, `astro.config.mjs` | Pinned Astro and design dependencies, static output at the domain root, isolated `/_zugbot/` assets. |
| `public/_zugbot/licenses/` | Upstream notices for the locally served Barlow fonts and Lucide interface icons. |
| `preview.py` | Local-only composer and link checker. Builds MkDocs strictly, overlays the built homepage in a fresh temporary review tree, compares every other file, and checks links, fragments, assets and search destinations. |
| `.gitignore`, `README.md` | Exclude generated files and document how to review the branch. |

The seven requested destinations are reachable from the homepage. Home is the logo, Features and Support are sections, and Guild Command Center, Peon Fight Club, Get Started and Documentation open existing guides. Only the homepage has a new design. Feature copy follows the website's release notes and guides. The three feature illustrations are navigation icons. [Production changelog](https://zugbot.net/changelog/) · [Guild Command Center](https://zugbot.net/discord-activity/) · [Peon Fight Club](https://zugbot.net/peon-fight-club/) · [Guild Planner](https://zugbot.net/planner/)

## Architecture recommendation

Use Astro's static output for reviewed product pages and keep MkDocs Material responsible for the existing guide tree. GitHub Pages can serve the resulting HTML, styles, fonts, images and search index at the current custom domain. The website needs no server runtime or OAuth handler. A separate `/docs/` migration would introduce redirects and change relative paths for existing users. [Astro on GitHub Pages](https://docs.astro.build/en/guides/deploy/github/) · [MkDocs configuration](https://www.mkdocs.org/user-guide/configuration/) · [GitHub Pages artifacts](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages)

For a later approved release, use the same three-directory design as the local preview. Build MkDocs and Astro separately, copy the MkDocs artifact to a fresh assembly directory, then add only approved Astro output. The sole allowed overlap today is `index.html`. Keep each generator's assets isolated and run the compatibility checks before uploading a single Pages artifact. Preserve the prior artifact and commit for rollback. Introduce any workflow change in its own reviewed change.

## Route and deployment constraints

- Direct public checks on November 22, 2026 covered the homepage, 15 guides, all 14 repository assets, the 404 document, both sitemap formats and the Material search index. Each returned HTTP 200 directly. Each page canonical matched its requested URL. [Live sitemap](https://zugbot.net/sitemap.xml)
- Keep `/privacy/`, `/terms/` and `/verification/` at their exact paths with their complete MkDocs documents and fragments. Preserve `/getting-started/`, `/discord-activity/`, `/peon-fight-club/`, `/member-guide/`, `/forever/`, `/realm-slugs/`, `/planner/`, `/admin-guide/`, `/commands/`, `/troubleshooting/`, `/roadmap/` and `/changelog/`. The last two guides distinguish released features from plans. External bookmarks and private integration settings cannot be enumerated from the website alone.
- Keep `/assets/`, `/search/search_index.json`, `/sitemap.xml`, `/sitemap.xml.gz` and `/404.html`. Realm lookup needs both its JavaScript and the JSON next to the script directory. Preserve the eight legacy homepage content IDs used in `preview.py`.
- Existing MkDocs search has six homepage records with the old homepage wording. Their targets are valid in the prototype. Refresh these entries for an approved cutover. Extend both sitemaps when future product pages add URLs. Reserve distinct routes for marketing pages that would otherwise collide with guides.
- The baseline uses a floating MkDocs Material dependency range. Phase 1 built with MkDocs 1.6.1 and Material 9.8.2. Compare protected HTML against the approved release when dependencies change. Material's maintainers state critical maintenance ends May 5, 2027. Track the documentation theme's lifecycle independently of the homepage rollout. [Maintainer update](https://squidfunk.github.io/mkdocs-material/blog/2025/11/05/zensical/)
- Pull requests build MkDocs. Pushes to main and manual dispatch can deploy. All runs currently share a cancel-in-progress concurrency group. When introducing Astro CI, give review builds separate concurrency and gate deployment on the approved production ref. The custom domain is already configured for Pages Actions. [Existing workflow](https://github.com/sthorne80/zugbot-site/blob/13f419d6d5d3a68c6a6fdce080fa2355afea7cc2/.github/workflows/pages.yml)
- The original Discord Lab invite returned Discord error `50270` (expired) on November 22. The prototype points visitors to the setup and support guides and the existing support email. Restore the Lab call to action once a valid invitation is supplied. The existing donation destinations remain linked.
