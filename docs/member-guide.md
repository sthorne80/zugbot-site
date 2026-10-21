# Member Guide

## Character lookup

Use `/character` to look up a public character without linking it:

1. Type the character name.
2. Begin typing the realm name.
3. Select the realm suggestion, such as `Thunderhorn — thunderhorn`.

The suggestion shows the realm name and the short official name ZugBot uses for it, called a slug. You normally do not need to know the slug. If suggestions are unavailable, you can enter it yourself.

## Verify and link your characters

Type `/link` and press Enter. You do not need to fill anything in first. ZugBot opens a private panel that only you can see, with two choices:

- If you connected Battle.net in the last 30 days, select one or more characters that are not linked yet and click **Link Selected**. If more than 25 characters are available, use the page buttons to see the rest.
- If you do not want to connect Battle.net, click **Add Manually** and enter one `CharacterName RealmSlug` per line.

Battle.net verification is optional. To confirm which characters are on your Battle.net account:

1. Run `/verify` in Discord.
2. Click **Verify with Battle.net**.
3. Your browser leaves ZugBot and opens Battle.net's own sign-in and approval page. Before entering your password, check that the address is on a `battle.net` domain.
4. Sign in to Battle.net and approve access.
5. Battle.net sends you back to ZugBot. Return to Discord and click **Finish Verification**.
6. Run `/link`, select the verified characters you want, and click **Link Selected**.

After `/verify`, ZugBot remembers the characters Battle.net confirmed for 30 days. When you link several characters, ZugBot adds the whole group together. If one character cannot be added, none of them are added and your links stay unchanged. Fix the problem and try again. Linking later does not restart the 30-day period.

To change your Main during either workflow, deliberately choose a linked character in the separate **Make Main** control. Leave it blank to preserve the current Main.

!!! warning "Do not enter Battle.net credentials into ZugBot"
    ZugBot never asks you to type your Battle.net password on zugbot.net or in Discord. After you click **Verify with Battle.net**, enter your password only if the browser address is on a `battle.net` domain. Battle.net sends you back to ZugBot after you approve access. If a page on zugbot.net, Discord, or another non-`battle.net` domain asks for your Battle.net password, do not enter it. Never paste passwords, sign-in codes, tokens, or sensitive return links into Discord. Read [Battle.net Verification & Privacy](verification.md) to see what ZugBot keeps.

| Command | Purpose |
| --- | --- |
| `/verify` | Optionally connect Battle.net to confirm which characters are yours |
| `/link` | Open your private character-linking panel; just type `/link` and press Enter |
| `/profile` | View one of your linked character profiles |
| `/alts` | List all linked characters and identify your main |
| `/main` | Set a linked character as your main |
| `/unlink` | Remove a linked character |

### Link characters manually

In `/link`, click **Add Manually** and enter one character per line:

```text
CharacterName RealmSlug
CharacterName RealmSlug
```

For example:

```text
Treehab thunderhorn
Zugdealer thunderhorn
```

Rules:

- use Blizzard's official realm slug; see the [Realm Slug Reference](realm-slugs.md);
- put each character on its own line;
- use the optional separate **Make Main** field only when you intend to change your Main;
- leave **Make Main** blank to preserve the current Main.

Manual links show as Unverified. If you run `/verify` later, ZugBot can change exact matches to Verified characters.

## Modern Mythic+

`/season` shows the current dungeon list. Run `/key`, then choose a role, key level, and dungeon to create a group card that stays available in Discord. If several characters are linked, ZugBot asks which one to use.

Group cards let Tanks, Healers, and DPS join or leave. The group leader can manage open spots and use Smart LFG. Active cards come back after a bot restart.

## Smart LFG notifications

Smart LFG is opt-in and configured per Discord server:

```text
/lfgnotify enable tank:true healer:false dps:true min_level:5 max_level:10
```

Choose any combination of Tank, Healer, and DPS and optional minimum or maximum key levels. Use `/lfgnotify settings` to review preferences, `/lfgnotify test` to test direct-message delivery, and `/lfgnotify disable` to opt out for that server.

## Guild Planner

Planner cards stay matched with Discord Scheduled Events and show the current role counts and signup list.

### Role signups and characters

Tank, Healer, DPS, and Bench require at least one linked character:

- with one linked character, ZugBot selects it automatically;
- with multiple linked characters, Discord opens a private list that only you can see;
- the selector shows at most the first 25 linked characters, with the main first;
- the chosen character name is saved with that event date.

The roster displays entries like `@DiscordMember (Character)`. The realm is added when needed to distinguish duplicate character names. Unlinking the character later does not erase the name already shown for an existing signup.

Maybe and Can't Attend are attendance states. They do not require a linked character or open the character selector. Changing any response replaces the existing response instead of creating a duplicate.

### Automatic reminders

ZugBot processes reminder windows at 24 hours and 1 hour before each event. Eligible recipients are the organizer, even without an RSVP, and members currently joined as Tank, Healer, DPS, or Bench.

Maybe and Can't Attend are excluded, as are people no longer in the Discord server. Discord must allow ZugBot to send the person a direct message, so delivery cannot be guaranteed. Each event date keeps its own reminder history.

### Recurring events

Weekly events stay on the same weekday and local time for the guild. Monthly events stay on the same day of the month and local time. If a month is shorter, an event set for the 31st moves to that month's last day, then returns to the 31st when possible: January 31 becomes February 28 or 29, then March 31.

Each date is a separate event with its own Planner Event ID, Discord Scheduled Event, Planner card, signups, character choices, and reminder history.

Editing one event date changes only that date and does not move future events. Cancelling one date does not stop the series. Use `/event stoprecurrence planner_event_id:<id>` to stop future dates while leaving the current event in place.

## Ready checks and fun

ZugBot also includes `/readycheck`, `/roll`, `/coinflip`, `/beer`, `/freebeer`, and `/zug`.
