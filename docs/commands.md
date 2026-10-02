# Command Reference

These commands are implemented in ZugBot 0.9.1. Planned commands are not listed as released.

## Character / Warband

| Command | Description |
| --- | --- |
| `/character` | Look up a public character; the realm field supports Blizzard-backed autocomplete and manual slug entry |
| `/link` | Link a Main or Alt; the realm field supports the same autocomplete and manual fallback |
| `/linkmany` | Link up to 20 characters from one free-text field using official realm slugs |
| `/profile` | View a linked character profile |
| `/alts` | List linked characters |
| `/main` | Set a linked character as the main |
| `/unlink` | Remove a linked character |

`/linkmany` uses `Name RealmSlug Main|Alt; Name RealmSlug Main|Alt`. It has no per-entry autocomplete, accepts semicolon- or line-separated entries, permits one Main per batch, and defaults an omitted type to Alt. Use the [Realm Slug Reference](realm-slugs.md).

## Modern WoW / Mythic+

| Command | Description |
| --- | --- |
| `/season` | Show the current Mythic+ dungeon pool |
| `/key` | Create an interactive, persistent Mythic+ group |

## LFG notifications

| Command | Description |
| --- | --- |
| `/lfgnotify enable` | Enable Smart LFG notifications for this server |
| `/lfgnotify disable` | Disable Smart LFG notifications |
| `/lfgnotify settings` | View notification preferences |
| `/lfgnotify test` | Send a test notification DM |

`/lfgnotify enable` supports Tank, Healer, and DPS opt-ins plus optional minimum and maximum key levels.

## Guild Planner

| Command | Description |
| --- | --- |
| `/event create` | Create a One-time, Weekly recurring, or Monthly recurring event and native Discord Scheduled Event |
| `/event edit` | Edit one Planner occurrence |
| `/event cancel` | Cancel one Planner occurrence |
| `/event stoprecurrence` | Stop future occurrences without cancelling the current occurrence |
| `/event timezone` | Set the guild Planner IANA timezone |

`/event create` asks for recurrence first and event type second. Planner cards support Tank, Healer, DPS, and Bench with linked-character selection, plus Maybe and Can't Attend. The organizer and joined-role members are eligible for 24-hour and 1-hour reminders.

## General / Utility

| Command | Description |
| --- | --- |
| `/help` | Show the in-Discord command reference |
| `/about` | Show a concise ZugBot overview |
| `/version` | Show version and runtime diagnostics |
| `/readycheck` | Start a ready check |

## Fun

| Command | Description |
| --- | --- |
| `/zug` | Summon ZugBot wisdom |
| `/roll` | Roll a die |
| `/coinflip` | Flip a coin |
| `/beer` | Give someone a beer |
| `/freebeer` | Start a round for everyone |

## Admin / Server Configuration

| Command | Description |
| --- | --- |
| `/setup` | Configure ZugBot for the Discord server |
| `/admin promote` | Promote a member by one normal progression tier |
| `/admin demote` | Demote a member by one normal progression tier |
| `/admin onboarding-post` | Post or replace the active Rules & Vibes agreement |
| `/debugdb` | Show guild-scoped database/runtime counts |
| `/endkeys` | Close active Mythic+ groups in the invoking guild |

!!! note
    Modern and WoW: Forever preferences are stored today, but `/key` is the implemented Modern Mythic+ flow. A separate Forever group command is not released.
