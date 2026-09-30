# Changelog

This page summarizes notable public-facing ZugBot changes.

## Unreleased

### Added

- structured file-based logging
- guild-scoped Smart LFG notification preferences
- owner-triggered Mythic+ notification flow
- persistent guild configuration
- Modern and WoW: Forever server preferences
- five-role guild role configuration
- Rules & Vibes onboarding agreement
- guild promotion/demotion administration
- automatic database backups

### Changed

- refreshed `/help` and `/about`
- unified application version display across `/help`, `/about`, and `/version`

### Fixed

- improved guild scoping for Mythic+ cleanup/debug operations
- improved Blizzard token refresh handling
- improved backup rotation behavior

## 0.3.0 — 2026-06-28

Initial production baseline included:

- character lookup and profiles
- linked main/alts
- Mythic+ group creation
- persistent SQLite storage
- interactive Discord views/buttons
- Linux production deployment
- version/runtime diagnostics

For planned work, see the [Roadmap](roadmap.md).
