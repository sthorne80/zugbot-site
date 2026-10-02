# Roadmap

Current production is **ZugBot 0.9.1**. This page separates released behavior from future direction; planned work is not a delivery promise.

## Current

### Member and group operations

- Blizzard-backed character lookup and realm autocomplete
- linked main and alt profiles, including `/linkmany`
- Mythic+ group creation with linked characters and persistent cards
- Smart LFG role and key-range preferences
- multi-guild server setup and restart-safe persistence

### Guild administration

- Admin, Founder, Moderator, Member, and New Member authority model
- controlled promotion and demotion
- persistent Rules & Vibes onboarding

### Guild Planner

- One-time, Weekly recurring, and Monthly recurring events
- linked-character Tank, Healer, DPS, and Bench signups
- Maybe and Can't Attend states
- native Discord Scheduled Events
- guild-local IANA timezones with DST-aware wall-clock recurrence
- automatic 24-hour and 1-hour reminders
- `/event stoprecurrence`
- independent occurrences and restart recovery

## Planned

### Event operations

- event discussion threads
- automatic voice channels
- readiness dashboard
- attendance tracking
- event lifecycle reconciliation

### Raid operations

- raid composition tools
- utility and readiness assistance
- raid supplies coordination

### Dashboard and analytics

- guild dashboard and calendar views
- roster and participation tools
- advanced operational analytics

### Additional grouping

ZugBot stores Modern WoW and WoW: Forever preferences today. A future Forever-oriented dungeon flow may complement the current Modern Mythic+ `/key` command without pretending both modes use identical mechanics.

## Product principles

ZugBot should assist leaders without removing member choice, respect privacy, minimize unnecessary notifications, and remain useful across different communities.
