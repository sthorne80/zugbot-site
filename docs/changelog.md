# Changelog

This page summarizes notable public-facing ZugBot changes. Current production is **0.9.1**.

## 0.9.1 — 2026-10-02

### Added

- realm autocomplete for `/character` and `/link`
- human-readable suggestions backed by Blizzard's official realm index

### Changed

- realm suggestions are cached so typing does not request Blizzard data on every keystroke
- autocomplete submits the official realm slug internally
- manual realm slug entry remains available if autocomplete data is unavailable

## 0.9.0 — 2026-10-01

### Added

- Monthly Guild Planner recurrence using the original guild-local calendar day and wall-clock time
- month-end clamping that preserves the original monthly anchor, including leap years

### Changed

- `/event create` now asks for One-time, Weekly recurring, or Monthly recurring before event type
- creation modal titles identify the selected recurrence
- `/event stoprecurrence` works for weekly and monthly series

## 0.8.1 — 2026-10-01

### Fixed

- stopped cards show **Weekly — Stopped** and retain that state after RSVP changes, edits, cancellations, restoration, and restarts
- `/event stoprecurrence` refreshes the Planner card immediately when Discord permits
- a card refresh problem is reported separately from a successfully stopped recurrence

## 0.8.0 — 2026-10-01

### Added

- Weekly Guild Planner recurrence
- `/event stoprecurrence` for stopping future occurrences without cancelling the current one

### Changed

- every weekly occurrence has independent RSVPs, character selections, reminder history, Discord Scheduled Event, Planner card, and ID
- editing or cancelling one occurrence does not shift or stop the series
- weekly schedules preserve guild-local weekday and time across DST

## 0.7.0 — 2026-10-01

### Added

- automatic 24-hour and 1-hour Planner reminders
- reminder DMs for organizers and joined Tank, Healer, DPS, or Bench attendees who remain guild members
- reminder messages with current composition, signup counts, and event links

Maybe and Can't Attend are excluded. Delivery depends on Discord allowing direct messages.

## 0.6.0 — 2026-09-30

### Added

- linked-character selection for Tank, Healer, DPS, and Bench Planner signups
- character snapshots that continue to render after the character is unlinked

### Changed

- Planner rosters show each joined member's selected character
- a single linked character is selected automatically; multiple characters open an ephemeral selector

## 0.5.0 — 2026-09-30

### Added

- Tank, Healer, DPS, and Bench Planner signups
- live composition counts and grouped rosters

### Changed

- Maybe and Can't Attend remain one-click attendance states
- changing a response updates the existing RSVP
- cancelled cards retain their roster and disable controls

## 0.4.0 — 2026-09-30

### Added

- Guild Planner with create, edit, cancel, and IANA timezone commands
- native Discord Scheduled Event integration and restart-safe cards
- Smart LFG preferences and notification controls
- persistent server setup and five-role guild authority configuration
- Rules & Vibes onboarding
- automatic database backups

### Changed

- `/help` and `/about` were refreshed for current capabilities and consistent version display

### Fixed

- Mythic+ cleanup and diagnostics are scoped to the invoking guild
- expired Blizzard access tokens refresh and retry once
- backup rotation reliably retains the newest backups

## 0.3.0 — 2026-06-28

The initial production baseline included character lookup and profiles, linked mains and alts, Mythic+ group creation, persistent storage, interactive Discord controls, Linux deployment, and version/runtime diagnostics.

For future direction, see the [Roadmap](roadmap.md).
