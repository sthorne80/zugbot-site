# Changelog

This page summarizes notable public-facing ZugBot changes.

## 0.4.0 — 2026-09-30

### Added

- Guild Planner event creation with Discord Scheduled Event integration
- persistent Guild Planner event cards
- Join / Maybe / Can't Attend attendance responses
- planner event editing and cancellation
- guild-scoped IANA planner timezone configuration
- organizer and configured guild-leadership planner controls
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
- improved Guild Planner event-card visibility for the Planner Event ID

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
