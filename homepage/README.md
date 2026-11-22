# Site architecture and route ownership

The original prototype directory, `homepage/`, now contains the entire static Astro website. One shared layout supplies the navigation, footer, local fonts, focus states, mobile menu and canonical URL. Product showcases and guides share that layout. The three interactive feature demonstrations use locally illustrated examples of documented Discord behavior. The website does not authenticate users or make bot requests.

## Build path

1. `mkdocs.export.yml` inherits the existing MkDocs configuration. A build-only hook exports the rendered article HTML and headings for each non-homepage Markdown source in `docs/`. It retains code, admonitions, tables, internal links, and legal wording.
2. `homepage/build.py` prepares guide data in `.generated/`, along with the original public assets and search data. Astro renders the product routes, help center, old guide routes and error page into a fresh candidate directory.
3. The assembler replaces the stale MkDocs homepage search records with the nine new product/help destinations. Detailed guide sections remain searchable. One XML sitemap and its gzip copy describe all 24 public page URLs. The 404 is excluded.
4. `check_site.py` verifies the expected route set, collision rules, one H1 per page, canonicals, duplicate IDs, guide markup parity, internal links and fragments, search targets, CSS asset URLs and legacy asset bytes. The builder swaps in `dist/` after validation. The review server serves unknown paths with the actual 404 status and page.

Astro, MkDocs, their existing dependencies, and GitHub Pages handle the entire site. Search runs locally in the browser. The Node and Python build tools are not required on the hosting platform. [Astro Pages guide](https://docs.astro.build/en/guides/deploy/github/) · [GitHub Pages artifacts](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages)

## Product routes

| Visitor destination | Public route | Detailed material |
| --- | --- | --- |
| Home | `/` | The eight existing public homepage fragment IDs are preserved. |
| Features | `/features/` | Links to showcases and released capability guides. |
| Guild Command Center | `/guild-command-center/` | Existing guide stays at `/discord-activity/`. |
| Peon Fight Club | `/tavern/peon-fight-club/` | Existing rules and bookmarks stay at `/peon-fight-club/`. |
| Guild Planner | `/guild-planner/` | Existing guide stays at `/planner/`. |
| Characters & Groups | `/characters-and-groups/` | Links to `/member-guide/`, `/forever/` and verification. |
| Get Started | `/get-started/` | Existing detailed walkthrough stays at `/getting-started/`. |
| Support | `/support/` | Integrates the Lab invite, email, troubleshooting and donation links. |
| Documentation | `/documentation/` | Search plus a categorized index of all 15 guides. |

### Existing guide URLs

All fifteen have the new Astro guide shell. The exact article content and original heading IDs come from the existing documents. None of these addresses requires a redirect.

| Group | Preserved routes |
| --- | --- |
| Launch and coordination | `/getting-started/`, `/discord-activity/`, `/peon-fight-club/`, `/planner/`, `/member-guide/`, `/forever/` |
| Reference and operations | `/commands/`, `/admin-guide/`, `/realm-slugs/`, `/troubleshooting/` |
| Release history | `/changelog/`, `/roadmap/` |
| Integration and legal | `/privacy/`, `/terms/`, `/verification/` |

Original reachable assets, including the realm lookup JavaScript and JSON, remain at their published paths. The legacy search JSON endpoint, both sitemap paths and `/404.html` remain available. The home bookmarks are `#main-content`, `#hero-title`, `#features`, `#planner-title`, `#tools-title`, `#start-title`, `#support`, and `#support-title`. OAuth callbacks on separate API hosts are outside the website artifact. The website audit cannot enumerate private external bookmarks.

## Content and operational notes

- On November 22, 2026, all 16 existing page routes, 14 tracked public assets and four generated public resources responded directly with HTTP 200. The donation destinations resolved and the supplied Discord invitation resolved to ZugBot Lab. Discord reported its expiration as December 22, 2026 at 12:30 p.m. Eastern. Recheck the invitation before release.
- The website repository contains no released product screenshots or verified public Production install URL. The demonstrations are labeled illustrations. Onboarding uses Discord's documented installation path and points to support for the approved app profile. [Discord app guide](https://support.discord.com/hc/en-us/articles/21334461140375-Using-Apps-on-Discord)
- The branch workflow builds on PRs and pushes to main and the redesign branch. Review artifacts expire after seven days. Only the manually enabled deploy job on main can write Pages. Keep an approved prior artifact or Git revision available for rollback.
- Use `python homepage/build.py` or `npm --prefix homepage run build` for a release-equivalent artifact. A direct Astro build skips assembly checks and final search/sitemap generation. Serving the artifact from a repository subpath requires a distinct base-path build. The production custom domain and local review both use the origin root.
- Keep the protected Markdown and integration route checks when upgrading MkDocs or its plugins. The tested Material release is 9.8.2. Its maintainers plan to end critical maintenance May 5, 2027. [Maintainer update](https://squidfunk.github.io/mkdocs-material/blog/2025/11/05/zensical/)
