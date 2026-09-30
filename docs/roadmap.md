# Roadmap

ZugBot's roadmap is intentionally flexible. This page describes planned direction, not a promise that every item will ship exactly as written.

## Foundation

Already implemented foundations include:

- Blizzard API integration
- Raider.IO integration
- character profiles
- linked warband/main-alt management
- Mythic+ group system
- interactive Discord UI
- SQLite persistence
- multi-guild setup
- five-role guild authority configuration
- Rules & Vibes onboarding
- Smart LFG notification preferences
- Guild Planner with Discord Scheduled Events, persistent RSVP cards, edit/cancel flows, and guild-local timezone support

## Guild Operations

### Guild Planner

Released in **0.4.0**:

- one-time event creation, editing, and cancellation
- Discord Scheduled Event integration
- persistent event cards in the configured Raid/Events channel
- Join / Maybe / Can't Attend RSVP state
- guild-scoped IANA timezone configuration
- organizer and configured leadership controls
- restart-safe reconciliation

Planned next steps include recurring events, reminders, role-based signups, attendance history, and event lifecycle reconciliation.

### Game-mode-aware grouping

ZugBot already stores Modern WoW and WoW: Forever preferences.

A future update will keep `/key` specific to Modern Mythic+ and add a separate Forever-oriented dungeon-group flow rather than assuming both games use the same mechanics.

## Raid tools

Planned areas include:

- raid composition assistance
- missing utility detection
- raid supply coordination
- attendance tracking

## Guild Dashboard

A future web dashboard may add:

- guild roster
- calendar
- Mythic+ groups
- attendance
- player profiles
- analytics
- officer tooling

## Analytics

Potential analytics include:

- average key level
- timed completion rate
- favorite dungeons
- group fill time
- participation and attendance trends

## Philosophy

ZugBot should assist guild leaders without removing player choice, respect player privacy, minimize unnecessary notifications, and remain useful to more than one specific guild.
