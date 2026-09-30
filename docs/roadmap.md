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
- Guild Planner MVP with Discord Scheduled Events

## Guild Operations

### Guild Planner

The **0.4.0 Guild Planner MVP is released** with:

- one-time event creation
- Discord Scheduled Event integration
- persistent event cards in the configured Raid Channel
- Join / Maybe / Can't Attend responses
- event editing and cancellation
- organizer and guild-leadership management controls
- guild-scoped IANA timezone handling
- restart-safe persistence

Future planner work may include:

- easier event selection/autocomplete instead of manually entering IDs
- recurring weekly events
- role-based Tank/Healer/DPS/Bench signups
- reminders
- event discussion threads
- attendance history and readiness tooling
- event lifecycle reconciliation for events that have already ended

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
