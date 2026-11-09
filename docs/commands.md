# Command Reference

These commands are currently implemented in Production. Planned commands are not listed as released.

## Character / Warband

| Command | Description |
| --- | --- |
| `/character` | Look up a public character; start typing a realm and choose it from the suggestions, or enter its official slug |
| `/verify` | Refresh Modern WoW and, when available, WoW: Forever character lists from one Battle.net authorization |
| `/link` | Link Modern or Forever characters from a private panel only you can see |
| `/profile` | View a linked Modern or Forever character profile |
| `/alts` | Show linked characters in separate game-mode sections |
| `/main` | Set the Main character for the selected game mode |
| `/unlink` | Remove a linked character from the selected game mode |

Battle.net verification is optional. When you click **Verify with Battle.net**, your browser goes to Battle.net's own sign-in page. ZugBot never asks you to enter your Battle.net password on zugbot.net or in Discord. See [Battle.net Verification & Privacy](verification.md) for safety and privacy details.

If you connected Battle.net in the last 30 days, `/link` lets you choose several characters from either roster. Lists longer than 25 characters have page buttons. If you do not want to connect Battle.net, choose **Add Manually**. Modern uses `CharacterName RealmSlug`; Forever uses the full character name and no realm. Modern and Forever have separate Main characters. The old `/linkmany` command no longer exists because its job is now part of `/link`.

When you link several characters, ZugBot adds the whole group together. If one character cannot be added, none of them are added. Your links stay unchanged so you can fix the problem and try again.

## Modern WoW / Mythic+

| Command | Description |
| --- | --- |
| `/season` | Show the current Mythic+ dungeon pool |
| `/key` | Create a Mythic+ group card that members can use in Discord |

`/key` and `/season` are Modern WoW-only. Forever characters do not appear in `/key`.

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

`/event create` first asks whether the event happens once, weekly, or monthly, then asks for the event type. In Production 0.10.0, Planner role character selection uses Modern WoW linked characters only. Planner cards also support Maybe and Can't Attend. The organizer and signed-up role members can receive reminders 24 hours and 1 hour before the event.

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

Modern and WoW: Forever character linking, verification, profiles, Mains, and character management are released. `/key` remains the Modern Mythic+ flow. Forever dungeon grouping and Forever Planner character signups are not released in Production 0.10.0.
