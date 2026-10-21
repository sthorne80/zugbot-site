# Command Reference

These commands are currently implemented in Production. Planned commands are not listed as released.

## Character / Warband

| Command | Description |
| --- | --- |
| `/character` | Look up a public character; the realm field supports Blizzard-backed autocomplete and manual slug entry |
| `/verify` | Authenticate with Battle.net and refresh your verified character roster |
| `/link` | Open an ephemeral panel for verified bulk selection or manual bulk entry; takes no arguments |
| `/profile` | View a linked character profile |
| `/alts` | List linked characters |
| `/main` | Set a linked character as the main |
| `/unlink` | Remove a linked character |

`/verify` opens Battle.net's optional authorization flow. ZugBot never asks for your Battle.net password; see [Battle.net Verification & Privacy](verification.md) for phishing-safety guidance and the exact retention model.

With a fresh verified roster, `/link` lets you select multiple currently unlinked characters, paginates rosters over 25, and links the chosen batch atomically. Without OAuth, choose **Add Manually** and enter one `CharacterName RealmSlug` per line. In either path, use the separate **Make Main** control only when you intend to change your Main; leaving it blank preserves the current Main. `/linkmany` has been retired.

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
