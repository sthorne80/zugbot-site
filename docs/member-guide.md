# Member Guide

## Character lookup

Use `/character` to look up a public character without linking it:

1. Type the character name.
2. Begin typing the realm name.
3. Select the realm suggestion, such as `Thunderhorn — thunderhorn`.

The suggestion shows the human-readable realm and its official slug. You normally do not need to know the slug; manual slug entry remains available when autocomplete is unavailable.

## Verify and link your characters

Run `/verify` before linking characters you want marked as Battle.net verified.

1. Run `/verify` in Discord.
2. Click **Verify with Battle.net**.
3. Sign in on Battle.net's own authorization site.
4. Return to Discord and click **Finish Verification**.
5. Run `/link`, start typing a character name or realm, select the character from your verified roster, and choose **Main** or **Alt**.

A successful verification refreshes a time-bounded roster of characters Battle.net says belong to the authenticated account. `/link` uses that roster so you can link additional verified characters without another Battle.net login while the verification remains fresh.

!!! warning "Do not enter Battle.net credentials into ZugBot"
    ZugBot never asks for your Battle.net password in Discord, on zugbot.net, or in a ZugBot form. Enter credentials only on Battle.net. Never paste passwords, authorization codes, raw OAuth state, tokens, or sensitive callback URLs into Discord. Read [Battle.net Verification & Privacy](verification.md) for exactly what is retained.

| Command | Purpose |
| --- | --- |
| `/verify` | Refresh your verified Battle.net character roster |
| `/link` | Link one character from your fresh verified roster as Main or Alt |
| `/profile` | View one of your linked character profiles |
| `/alts` | List all linked characters and identify your main |
| `/main` | Set a linked character as your main |
| `/unlink` | Remove a linked character |

### Link several characters manually

`/linkmany` is one free-text field and does **not** provide per-character roster autocomplete. Use this format:

```text
Name RealmSlug Main|Alt; Name RealmSlug Main|Alt
```

For example:

```text
Treehab thunderhorn alt; Zugdealer thunderhorn main
```

Rules:

- use Blizzard's official realm slug; see the [Realm Slug Reference](realm-slugs.md);
- submit at most 20 entries per batch;
- separate entries with a semicolon or a new line;
- mark at most one Main in each batch;
- `Main|Alt` is optional and defaults to Alt.

Manual linking does not itself prove ownership. A later successful `/verify` can refresh matching linked characters as Battle.net verified.

## Modern Mythic+

`/season` displays the current dungeon rotation. Run `/key`, then choose a role, key level, and dungeon to create a persistent group card. If several characters are linked, ZugBot asks which one to use.

Group cards support Tank, Healer, and DPS joining, leaving, PUG slot management, owner controls, and Smart LFG. Active cards recover after a bot restart.

## Smart LFG notifications

Smart LFG is opt-in and configured per Discord server:

```text
/lfgnotify enable tank:true healer:false dps:true min_level:5 max_level:10
```

Choose any combination of Tank, Healer, and DPS and optional minimum or maximum key levels. Use `/lfgnotify settings` to review preferences, `/lfgnotify test` to test direct-message delivery, and `/lfgnotify disable` to opt out for that server.

## Guild Planner

Planner cards are synchronized with native Discord Scheduled Events and show live composition and grouped rosters.

### Role signups and characters

Tank, Healer, DPS, and Bench require at least one linked character:

- with one linked character, ZugBot selects it automatically;
- with multiple linked characters, Discord opens an ephemeral selector;
- the selector shows at most the first 25 linked characters, with the main first;
- the chosen character is snapshotted onto that occurrence.

The roster displays entries like `@DiscordMember (Character)`. The realm is added when needed to distinguish duplicate character names. Unlinking the character later does not erase the name already shown for an existing signup.

Maybe and Can't Attend are attendance states. They do not require a linked character or open the character selector. Changing any response replaces the existing response instead of creating a duplicate.

### Automatic reminders

ZugBot processes reminder windows at 24 hours and 1 hour before each event. Eligible recipients are the organizer, even without an RSVP, and members currently joined as Tank, Healer, DPS, or Bench.

Maybe and Can't Attend are excluded, as are people no longer in the Discord guild. Delivery also depends on Discord allowing ZugBot to DM the user; delivery and retries are not guaranteed. Every recurring occurrence has independent reminder history.

### Recurring events

Weekly events preserve the same guild-local weekday and wall-clock time. Monthly events preserve the original guild-local calendar day and wall-clock time. Month-end clamping does not move the anchor: January 31 becomes February 28 or 29, then returns to March 31.

Each occurrence is a separate event with its own Planner Event ID, Discord Scheduled Event, Planner card, RSVPs, character selections, and reminder history.

Editing one occurrence changes only that occurrence and does not move future cadence. Cancelling one occurrence cancels only that occurrence; it does not stop the series. Use `/event stoprecurrence planner_event_id:<id>` to stop future occurrences while leaving the current occurrence intact.

## Ready checks and fun

ZugBot also includes `/readycheck`, `/roll`, `/coinflip`, `/beer`, `/freebeer`, and `/zug`.
