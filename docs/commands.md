# Command Reference

These commands are currently implemented in Production. Planned commands are not listed as released.

## Character / Warband

| Command | Description |
| --- | --- |
| `/character` | Look up a public character; start typing a realm and choose it from the suggestions, or enter its official slug |
| `/verify` | Optionally connect Battle.net to confirm which characters are yours |
| `/link` | Open a private character-linking panel that only you can see; type `/link` and press Enter without filling anything in |
| `/profile` | View a linked character profile |
| `/alts` | List linked characters |
| `/main` | Set a linked character as the main |
| `/unlink` | Remove a linked character |

Battle.net verification is optional. When you click **Verify with Battle.net**, your browser goes to Battle.net's own sign-in page. ZugBot never asks you to enter your Battle.net password on zugbot.net or in Discord. See [Battle.net Verification & Privacy](verification.md) for safety and privacy details.

If you connected Battle.net in the last 30 days, `/link` lets you choose several of your characters from a list. Lists longer than 25 characters have page buttons. If you do not want to connect Battle.net, choose **Add Manually** and enter one `CharacterName RealmSlug` per line. **Make Main** is optional; leave it blank to keep your current Main. Manual links show as Unverified, and a later `/verify` can change exact matches to Verified. The old `/linkmany` command no longer exists because its job is now part of `/link`.

When you link several characters, ZugBot adds the whole group together. If one character cannot be added, none of them are added. Your links stay unchanged so you can fix the problem and try again.

## Modern WoW / Mythic+

| Command | Description |
| --- | --- |
| `/season` | Show the current Mythic+ dungeon pool |
| `/key` | Create a Mythic+ group card that members can use in Discord |

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
| `/event edit` | Edit one event date |
| `/event cancel` | Cancel one event date |
| `/event stoprecurrence` | Stop future dates without cancelling the current event |
| `/event timezone` | Set the time zone used for guild events |

`/event create` first asks whether the event happens once, weekly, or monthly, then asks for the event type. Planner cards support Tank, Healer, DPS, and Bench with linked-character selection, plus Maybe and Can't Attend. The organizer and signed-up role members can receive reminders 24 hours and 1 hour before the event.

## General / Utility

| Command | Description |
| --- | --- |
| `/help` | Show the in-Discord command reference |
| `/about` | Show a concise ZugBot overview |
| `/version` | Show the running ZugBot version and troubleshooting details |
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
| `/debugdb` | Show saved-item and running-process counts for the current Discord server |
| `/endkeys` | Close active Mythic+ groups in the current Discord server |

Modern and WoW: Forever preferences are stored today, but `/key` is the implemented Modern Mythic+ flow. A separate Forever group command is not released.
