# Guild Planner

<div class="zug-doc-hero">
  <div>
    <div class="zug-kicker">Released Planner · Current behavior through ZugBot 0.9.x</div>
    <h2>Plan guild events without leaving Discord.</h2>
    <p>Guild Planner combines persistent event cards with native Discord Scheduled Events, linked-character role signups, reminders, recurrence, guild-local timezones, and restart recovery.</p>
  </div>
</div>

## What members see

The Planner card is the working surface for the guild. It shows event details, Discord-localized times, live composition, and a roster. Entries are displayed as `@DiscordMember (Character)`, with the realm included when duplicate character names need disambiguation.

The available responses are Tank, Healer, DPS, Bench, Maybe, and Can't Attend.

## Create an event

Run `/event create`. Discord presents command options in this order:

1. **recurrence** — One-time, Weekly recurring, or Monthly recurring;
2. **event_type** — the kind of guild event.

The modal then asks for:

- Title
- Local start (`YYYY-MM-DD HH:MM`)
- Duration, such as `90m`, `2h`, or `1h 30m`
- optional Description

Its title reflects the selected recurrence: **Create One-Time Event**, **Create Weekly Event**, or **Create Monthly Event**.

ZugBot creates a unique Planner card in the configured Raid/Events channel and a native Discord Scheduled Event.

## Role signups

Tank, Healer, DPS, and Bench are role-based attendance and require a linked character. One linked character is selected automatically. With more than one, an ephemeral selector shows up to 25 linked characters, main first.

Maybe and Can't Attend record attendance state only; they do not require or select a character. Choosing another response updates the existing RSVP.

The selected character name, realm name, and realm slug are snapshotted onto the occurrence. Later unlinking does not remove the character name from that existing signup.

## Reminders

Automatic reminder windows are 24 hours and 1 hour before the event. ZugBot attempts a DM to the organizer and members currently signed up as Tank, Healer, DPS, or Bench. Maybe, Can't Attend, and people no longer in the Discord guild are excluded.

Discord privacy settings and DM availability determine whether delivery succeeds. ZugBot does not promise delivery or retries. Each occurrence maintains its own reminder history.

## Weekly and monthly recurrence

Weekly recurrence preserves the configured guild-local weekday and wall-clock time. Monthly recurrence preserves the original guild-local calendar day and wall-clock time.

For dates near month end, the shorter month is clamped without moving the original anchor:

```text
January 31 → February 28/29 → March 31
```

Every occurrence is independent, with its own Planner Event ID, Discord Scheduled Event, Planner card, RSVPs and linked-character selections, and reminder history.

Editing one occurrence does not change future cadence. Cancelling one occurrence cancels only that occurrence, and the series continues.

## Stop recurrence

Run:

```text
/event stoprecurrence planner_event_id:<id>
```

This stops future occurrences and leaves the current occurrence intact. The card changes to **Weekly — Stopped** or **Monthly — Stopped**. Repeating the command is safe; ZugBot reports that recurrence was already stopped and reconciles the card when possible.

## Edit or cancel an occurrence

Use `/event edit planner_event_id:<id>` or `/event cancel planner_event_id:<id>`. The organizer, Discord server owner, or configured ZugBot Admin or Founder can manage an event.

Editing changes only the selected occurrence. Cancelling retains its roster and information, disables signup controls, and cancels its native Scheduled Event. Neither action stops or shifts a recurring series.

## Timezones and daylight saving time

Use `/event timezone` to configure an IANA timezone, for example:

```text
America/New_York
America/Chicago
Europe/London
UTC
```

Members see Discord timestamps in their own local timezone. Recurrence preserves the guild-local wall-clock time as daylight saving time changes. If a configured local time is invalid during a DST transition, ZugBot does not silently shift it to another time.

## Permissions and persistence

ZugBot needs View Channel, Send Messages, Embed Links, and Manage Events for the configured Raid/Events channel. Discord Administrator is not required.

Events, RSVPs, character snapshots, reminders, and recurrence state persist. Active cards and controls are restored after a bot restart.

## Related documentation

- [Member Guide](member-guide.md)
- [Guild Administration](admin-guide.md)
- [Command Reference](commands.md)
- [Troubleshooting](troubleshooting.md)
