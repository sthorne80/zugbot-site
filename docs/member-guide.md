# Member Guide

## Link characters by game

Type `/link` and press Enter. ZugBot opens a private panel only you can see.

1. If ZugBot asks which game you want, choose **Modern WoW** or **WoW: Forever**. With only one enabled game, its flow opens directly.
2. Select characters from a fresh Battle.net list, click **Verify with Battle.net**, or choose **Add Manually**.
3. Select or enter characters.
4. Click **Link Selected** or submit the manual form.
5. Optionally choose a Main for that game.

If both game modes are enabled, `/link` asks which one you want. If only one is enabled, ZugBot opens that flow directly.

### Verify once for both games

Battle.net verification is optional. To refresh the characters Battle.net confirms belong to you:

1. Run `/verify`.
2. Click **Verify with Battle.net**.
3. Sign in and approve access on Battle.net's own website.
4. Return to Discord and click **Finish Verification**.
5. Run `/link`. If ZugBot asks which game you want, choose it. Then select characters and click **Link Selected**.

The same authorization refreshes Modern WoW and WoW: Forever rosters when Forever information is available. Verified lists last 30 days. Lists with more than 25 characters have page buttons.

If a batch cannot be linked safely, none of that batch is added. Fix the problem and try again.

!!! warning "Do not enter Battle.net credentials into ZugBot"
    ZugBot never asks for your Battle.net password on zugbot.net or in Discord. Enter it only on a `battle.net` address. Never paste passwords, sign-in codes, tokens, or sensitive return links into Discord. See [Battle.net Verification & Privacy](verification.md).

### Modern manual linking

Run `/link`. If ZugBot asks which game you want, choose **Modern WoW**. Click **Add Manually** and enter one character per line:

```text
Treehab thunderhorn
Zugdealer thunderhorn
```

The format is `CharacterName RealmSlug`. A realm slug is Blizzard's short official realm name. You can find it in the [Realm Slug Reference](realm-slugs.md).

### Forever manual linking

Run `/link`. If ZugBot asks which game you want, choose **WoW: Forever**. Click **Add Manually** and enter one full character name per line:

```text
Abrakadaver Salwyn
Pallyamorous Smitegeist
```

Do not add a realm. Forever characters use their full names and have no realm field in ZugBot. See the [WoW: Forever guide](forever.md).

Manual links are Unverified until a later Battle.net verification confirms ownership.

## Main characters and `/alts`

Modern and Forever each have an independent Main. Changing the Forever Main does not change the Modern Main.

- Leave **Make Main** blank while linking to preserve the current Main.
- Use `/main`, select the game, then choose the intended linked character.
- Use `/alts` to see separate Modern WoW and WoW: Forever sections.
- Use `/unlink`, select the game, and choose the intended character.

## Character profiles

Use `/profile` and select a linked character.

- Modern profiles include realm-based Blizzard information.
- Forever profiles use the full character name and do not show or require a realm.

Use `/character` for an unlinked public Modern character lookup. Start typing the realm and choose a suggestion. If suggestions are unavailable, enter the official realm slug.

## Modern Mythic+

`/season` shows the current Modern dungeon list. `/key` creates a Modern WoW Mythic+ group. Forever characters do not appear in `/key` character selection. Use `/dungeon` to create a Forever five-player dungeon group with role signup and external PUG controls.

Group cards let Tanks, Healers, and DPS join or leave. The leader can manage open spots and use Smart LFG. Active cards return after a bot restart.

## Smart LFG notifications

Smart LFG is for Modern Mythic+ and is configured per Discord server:

```text
/lfgnotify enable tank:true healer:false dps:true min_level:5 max_level:10
```

Use `/lfgnotify settings` to review preferences, `/lfgnotify test` to test direct messages, and `/lfgnotify disable` to opt out.

## Guild Planner

Production 0.11.0 Planner role signups use the linked characters for the selected event game mode, including WoW: Forever.

Tank, Healer, DPS, and Bench require a linked Modern character. With one eligible character, ZugBot selects it automatically. With several, Discord opens a private list with the Main first. Maybe and Can't Attend do not require a character.

The chosen character is saved with that event date, so the roster still renders if the character is later unlinked. Reminders are attempted 24 hours and 1 hour before the event for the organizer and current role signups.

Weekly and monthly dates are independent events. Editing or cancelling one date does not rewrite the series. Use `/event stoprecurrence planner_event_id:<id>` to stop future dates.

## Ready checks and fun

ZugBot also includes `/readycheck`, `/roll`, `/coinflip`, `/beer`, `/freebeer`, and `/zug`.
