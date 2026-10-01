# Guild Planner

<div class="zug-doc-hero">
  <div>
    <div class="zug-kicker">Released in ZugBot 0.4.0 · Role signups in 0.5.0</div>
    <h2>Plan guild events without leaving Discord.</h2>
    <p>The Guild Planner combines ZugBot event cards with Discord Scheduled Events, guild-local timezones, persistent RSVP state, editing, cancellation, and restart recovery.</p>
  </div>
</div>

## What members see

The event card is the working surface for the guild. Members can respond without learning another calendar or opening another website.

<div class="zug-planner-demo-wrap">
  <div class="zug-discord-preview zug-discord-preview--docs">
    <div class="zug-preview-topline">
      <span class="zug-preview-dot"></span>
      Guild Planner
    </div>

    <div class="zug-preview-card">
      <h3>Heroic Raid Night</h3>
      <p>Progression night synchronized with Discord Scheduled Events.</p>

      <div class="zug-preview-meta">
        <div>
          <small>Starts</small>
          <strong>Friday · 8:00 PM</strong>
        </div>
        <div>
          <small>Composition</small>
          <strong>2 Tank · 4 Healer · 11 DPS</strong>
        </div>
      </div>

      <div class="zug-role-buttons">
        <span>Tank</span>
        <span>Healer</span>
        <span>DPS</span>
        <span>Bench</span>
      </div>

      <div class="zug-preview-roster">
        <div><b>Tanks:</b> @Member</div>
        <div><b>Healers:</b> @Member</div>
        <div><b>DPS:</b> @Member · +10 more</div>
        <div><b>Maybe:</b> @Member</div>
      </div>
    </div>
  </div>
</div>

!!! note "Current production behavior"
    ZugBot 0.5.0 supports **Tank**, **Healer**, **DPS**, **Bench**, **Maybe**, and **Can't Attend** responses. Character-aware Planner signups are still under development and are not described here as released behavior.

## Planner workflow

### Create an event

Run:

~~~text
/event create
~~~

Choose the event type, then enter the title, local start time, duration, and optional description.

ZugBot creates both:

- a persistent Planner card in the configured Raid / Events channel;
- a native Discord Scheduled Event.

The Planner card includes the event type, organizer, status, Discord timestamps, live composition, roster, a link to the native Discord event, and the complete Planner Event ID.

### Change your RSVP

For active events, members can select:

| Response | Meaning |
| --- | --- |
| **Tank** | Joined as Tank |
| **Healer** | Joined as Healer |
| **DPS** | Joined as DPS |
| **Bench** | Joined on the bench |
| **Maybe** | Not committed yet |
| **Can't Attend** | Not attending |

Changing your response updates the existing RSVP rather than creating a duplicate.

### Edit an event

Run:

~~~text
/event edit
~~~

Use the **Planner Event ID** shown directly on the event card.

The organizer, server owner, configured Admin, or configured Founder can edit the event. ZugBot keeps the Planner card and Discord Scheduled Event synchronized.

### Cancel an event

Run:

~~~text
/event cancel
~~~

Cancelled cards retain their roster and event information, switch to a cancelled state, and disable RSVP controls.

## Timezones

Run:

~~~text
/event timezone
~~~

ZugBot accepts IANA timezone names such as:

~~~text
America/New_York
Europe/London
America/Chicago
~~~

Event times are entered in the guild's configured timezone and stored internally in UTC. Discord timestamps then render correctly for each member's own local timezone.

## Permissions

ZugBot needs the following permissions for the configured Raid / Events channel:

- View Channel
- Send Messages
- Embed Links
- Manage Events

**Discord Administrator is not required.**

## Built for persistence

Planner events and RSVPs are stored in ZugBot's database. Persistent controls are reconstructed after a bot restart, and active Planner cards are reconciled when ZugBot comes back online.

This allows the Planner to behave like an operational guild tool instead of a temporary chat command.

## Related documentation

- [Member Guide](member-guide.md)
- [Guild Administration](admin-guide.md)
- [Command Reference](commands.md)
- [Roadmap](roadmap.md)
