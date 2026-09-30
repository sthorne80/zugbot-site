# Command Reference

This page lists commands currently implemented in ZugBot. Planned commands are not included here.

## Character / Warband

| Command | Description |
| --- | --- |
| `/character` | Look up a public WoW character |
| `/link` | Link a character to your Discord account |
| `/linkmany` | Link several characters at once |
| `/profile` | View a linked character profile |
| `/alts` | List your linked characters |
| `/main` | Set your main character |
| `/unlink` | Remove a linked character |

## Modern WoW / Mythic+

| Command | Description |
| --- | --- |
| `/season` | Show the current Mythic+ dungeon pool |
| `/key` | Create an interactive Mythic+ group |

## LFG notifications

| Command | Description |
| --- | --- |
| `/lfgnotify enable` | Enable Smart LFG notifications for this server |
| `/lfgnotify disable` | Disable Smart LFG notifications |
| `/lfgnotify settings` | View your notification preferences |
| `/lfgnotify test` | Send yourself a test notification DM |

`/lfgnotify enable` supports Tank, Healer, and DPS opt-ins plus optional minimum and maximum key levels.

## General / Utility

| Command | Description |
| --- | --- |
| `/help` | Show the in-Discord command reference |
| `/about` | Show a concise overview of ZugBot |
| `/version` | Show version and runtime diagnostics |
| `/readycheck` | Start a quick ready check |

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
| `/admin promote` | Promote a member by one configured progression tier |
| `/admin demote` | Demote a member by one configured progression tier |
| `/admin onboarding-post` | Post or replace the active Rules & Vibes agreement |
| `/debugdb` | Show guild-scoped database/runtime counts |
| `/endkeys` | Close active Mythic+ groups in the invoking guild |

!!! warning "Not released yet"
    The Guild Planner `/event` flow and a dedicated WoW: Forever dungeon-group command are roadmap features. They will be added to this reference only after they are released.
