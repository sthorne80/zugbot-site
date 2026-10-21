# Guild Planner

<div class="zug-doc-hero">
  <div>
    <div class="zug-kicker">Released Planner · Current through ZugBot 0.9.x</div>
    <h2>Plan guild events without leaving Discord.</h2>
    <p>Guild Planner combines event cards with Discord Scheduled Events, linked-character role signups, reminders, repeating schedules, guild time zones, and cards that return after a restart.</p>
  </div>
</div>

## What members see

The Planner card is where members use the event. It shows event details, each member's local time, current role counts, and the signup list. Entries appear as `@DiscordMember (Character)`. ZugBot adds the realm when two characters have the same name.

The available responses are Tank, Healer, DPS, Bench, Maybe, and Can't Attend.

## Create an event

Run `/event create`. Discord asks for:

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

Tank, Healer, DPS, and Bench require a linked character. One linked character is selected automatically. With more than one, a private list that only you can see shows up to 25 linked characters, Main first.

Maybe and Can't Attend only record whether someone plans to come. They do not require or select a character. Choosing another response replaces the earlier choice.

ZugBot saves the selected character name and realm with that event date. Unlinking the character later does not remove the name from the existing signup.

## Reminders

Automatic reminder windows are 24 hours and 1 hour before the event. ZugBot attempts a DM to the organizer and members currently signed up as Tank, Healer, DPS, or Bench. Maybe, Can't Attend, and people no longer in the Discord guild are excluded.

Discord privacy settings determine whether ZugBot can send the direct message, so delivery cannot be guaranteed. Each event date keeps its own reminder history.

## Weekly and monthly recurrence

Weekly events stay on the same weekday and local time for the guild. Monthly events stay on the same day of the month and local time.

For dates near the end of a month, ZugBot uses the last available day in a shorter month and returns to the chosen date when possible:

```text
January 31 → February 28/29 → March 31
```

Each date is a separate event with its own Planner Event ID, Discord Scheduled Event, Planner card, signups, linked-character choices, and reminder history.

Editing one event date does not change future dates. Cancelling one event date cancels only that date, and the series continues.

## Stop recurrence

Run:

```text
/event stoprecurrence planner_event_id:<id>
```

This stops future dates and leaves the current event in place. The card changes to **Weekly — Stopped** or **Monthly — Stopped**. Running the command again is safe. ZugBot says that repeating events were already stopped and updates the card when possible.

## Edit or cancel one event date

Use `/event edit planner_event_id:<id>` or `/event cancel planner_event_id:<id>`. The organizer, Discord server owner, or configured ZugBot Admin or Founder can manage an event.

Editing changes only the selected date. Cancelling keeps its signup list and information, disables the signup buttons, and cancels its Discord Scheduled Event. Neither action stops or moves the rest of the repeating series.

## Timezones and daylight saving time

Use `/event timezone` to configure an IANA timezone, for example:

```text
America/New_York
America/Chicago
Europe/London
UTC
```

Members see event times in their own time zone. Repeating events stay at the same local time for the guild when daylight saving time changes. If a chosen local time does not exist when the clocks change, ZugBot does not quietly move it to another time.

## Permissions and persistence

ZugBot needs View Channel, Send Messages, Embed Links, and Manage Events for the configured Raid/Events channel. Discord Administrator is not required.

Events, signups, saved character names, reminders, and repeating schedules are kept. Active cards and buttons return after a bot restart.

## Related documentation

- [Member Guide](member-guide.md)
- [Guild Administration](admin-guide.md)
- [Command Reference](commands.md)
- [Troubleshooting](troubleshooting.md)
