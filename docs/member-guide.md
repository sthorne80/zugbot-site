# Member Guide

## Character lookup

Use `/character` to look up a public World of Warcraft character without linking it to your Discord account.

## Link your characters

Use `/link` to add a character to your ZugBot profile as a main or alt.

If you have several characters to add, `/linkmany` can link multiple characters from one submitted list.

Useful profile commands:

| Command | Purpose |
| --- | --- |
| `/profile` | View one of your linked character profiles |
| `/alts` | List your linked characters |
| `/main` | Set your main character |
| `/unlink` | Remove a linked character |

## Modern WoW Mythic+

### Current season

`/season` displays the current Modern WoW Mythic+ rotation.

For **Midnight Season 2**, ZugBot currently uses:

- Altar of Fangs
- Murder Row
- Den of Nalorakk
- The Blinding Vale
- Voidscar Arena
- Kings' Rest
- Ruby Life Pools
- Temple of Sethraliss

### Create a group

Run `/key` and choose:

- your role: Tank, Healer, or DPS;
- key level;
- dungeon.

If you have multiple linked characters, ZugBot asks which character you want to use.

The group card supports:

- Tank / Healer / DPS joining
- leaving the group
- PUG slot management
- owner controls
- Smart LFG notification support when enabled

Groups are persisted so active cards can recover after a bot restart.

## Smart LFG notifications

Smart LFG is opt-in and configured per Discord server.

Example:

```text
/lfgnotify enable tank:true healer:false dps:true min_level:5 max_level:10
```

You can choose any combination of Tank, Healer, and DPS and optionally set a minimum and/or maximum key level.

Other commands:

- `/lfgnotify settings` — show your current settings
- `/lfgnotify test` — send yourself a test DM
- `/lfgnotify disable` — stop notifications for that server

If a test DM fails, check whether your Discord privacy settings allow direct messages from that server.

## Guild Planner

Guild Planner events appear as persistent cards in the server's configured Raid/Events channel and are synchronized with Discord Scheduled Events.

For active events, choose the response that matches how you plan to participate:

- **Tank**
- **Healer**
- **DPS**
- **Bench**
- **Maybe**
- **Can't Attend**

Changing your response updates your existing signup. The event card shows live composition counts and a grouped roster.

## Ready checks and fun

ZugBot also includes lightweight server utilities:

- `/readycheck`
- `/roll`
- `/coinflip`
- `/beer`
- `/freebeer`
- `/zug`
