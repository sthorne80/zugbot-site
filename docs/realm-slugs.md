# Realm Slug Reference

!!! tip
    **For `/character`, you normally do not need this page.** Start typing your realm in Discord and choose it from ZugBot's suggestions. You may need the official slug when using `/link`'s **Add Manually** form.

This reference is primarily for `/link`'s manual entry, manual public lookups, and troubleshooting. Manual character linking uses one `CharacterName RealmSlug` entry per line.

## Display names and slugs

| Display name | Slug |
| --- | --- |
| Area 52 | `area-52` |
| Mal'Ganis | `malganis` |

These examples illustrate the difference, but simple lowercase or punctuation removal is not authoritative for every realm. Use the official value from Blizzard's realm index.

## Search official realm data

<div class="realm-reference" data-realm-reference>
  <label class="realm-search-label" for="realm-search">Search by realm name, slug, or region</label>
  <input class="realm-search" id="realm-search" type="search" placeholder="Try Area 52, area-52, or us" autocomplete="off" disabled>
  <p class="realm-data-updated" data-realm-updated hidden></p>
  <p class="realm-search-status" data-realm-status role="status" aria-live="polite">Loading realm reference data…</p>
  <div class="realm-results" data-realm-results></div>
  <noscript>JavaScript is required to search the generated realm reference. `/character` autocomplete still works in Discord.</noscript>
</div>

For `/link` → **Add Manually**, use the slug in entries such as:

```text
Treehab thunderhorn
Zugdealer thunderhorn
```

Use the separate optional **Make Main** field only when you intend to change your Main.

This list comes from Blizzard's public game data and contains only the region, display name, and official slug.

<small>Realm data is sourced from Blizzard's public API. ZugBot is an independent project and is not affiliated with or endorsed by Blizzard Entertainment.</small>
