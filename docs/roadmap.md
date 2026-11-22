# Roadmap

This page distinguishes features **live in Production** from ideas under consideration. Proposed work is not a promise or release date.

## Available now

### Guild Command Center in Discord

- Graphical Discord Activity with Dashboard, Events, Groups, Characters, Fun, incident reporting, and permission-controlled Leadership and Guild Setup
- Retail WoW Mythic+ and WoW: Forever group coordination
- One-time, weekly, and monthly events, linked-character signups, native Discord Scheduled Events, and reminders
- Linked characters, independent Mains, optional Battle.net ownership verification, and public profile lookup
- Member directory and authorized staff tools using configured authority, Discord permissions, guild boundaries, and hierarchy
- Persistent guild configuration and restart-safe records

### Tavern and Peon Fight Club

- Dice, coins, peon wisdom, beers, and a ten-claim Brewfest Keg
- Two-fighter D20 Peon Fight Club, Combat Journal, trophy and 24-hour Champion, Hall of Fame, and battle archive
- New 24-hour challenge window; cancellation and safe recovery after deleted Discord messages

### Safeguards

- Member authentication and guild/channel permissions
- Highest valid configured authority tier for overlapping staff roles, with specific checks for each action
- Formal moderation writes and automatic Discord Champion role assignment **disabled** in Production
- Slash commands remain available alongside the Activity

## Planned ideas — not currently available

### Local ZugBot AI assistant

A possible future Activity section could connect to a locally hosted Ollama model. The design being considered includes a **bounded request queue**, per-member limits, a **sleeping peon** status when the host computer is offline, and optional cited searches of current WoW sources where permitted.

**ZugBot AI chat and web searching are not live Production features.** Cloud AI inference is not an automatic fallback.

### Other ideas

- More raid readiness, composition, and supplies assistance
- Guild activity insights and richer participation analytics
- Better event discussions and coordination
- More Tavern activities after existing games prove useful

## Product principles

Respect members' privacy and server autonomy, enforce Discord permissions, minimize spam, keep useful data durable, and make guild coordination enjoyable.
