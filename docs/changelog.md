# Changelog

This page summarizes notable public-facing ZugBot changes.

## 0.5.0 — 2026-09-30

### Added

- role-based Guild Planner signups for Tank, Healer, DPS, and Bench
- live planner composition counts and grouped roster display
- backward-compatible support for legacy joined RSVPs without an assigned role

### Changed

- Maybe and Can't Attend remain one-click planner responses
- planner RSVP changes update the existing signup instead of creating duplicates
- cancelled planner cards keep their roster while disabling signup controls

## 0.4.0 — 2026-09-30

### Added

- Guild Planner with `/event create`, `/event edit`, `/event cancel`, and `/event timezone`
- Discord Scheduled Event integration
- persistent planner cards with Join / Maybe / Can't Attend responses
- guild-local IANA timezone support with UTC persistence
- organizer and configured leadership event-management controls

### Changed

- planner event cards integrate directly with Discord's native Events surface
- help output documents planner commands and permissions

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
