# Guild Administration

ZugBot's setup, authority, and operational data are scoped to each Discord guild.

## Server setup

Run `/setup`. The Discord server owner or a member with Administrator or Manage Server permission can change setup.

ZugBot can store Bot Commands, Mythic/LFG, Raid, and Announcement channels; Modern WoW and WoW: Forever preferences; a default game mode and region; and five authority/membership roles.

!!! note "Blizzard region behavior"
    The bot deployment's configured Blizzard region controls `/character`, `/link`, and realm autocomplete requests. The guild `default_region` stored by `/setup` does not currently switch those Blizzard requests per guild.

## Five-role authority model

The configured hierarchy is:

```text
Admin > Founder > Moderator > Member > New Member
```

The Discord server chooses the actual roles mapped to those tiers. The guild owner is ZugBot's root authority even without the configured Admin role.

Normal progression is:

```text
New Member ⇄ Member ⇄ Moderator
```

Founder and Admin are protected tiers, not ordinary promotion steps. Use `/admin promote` and `/admin demote`; ZugBot changes only the relevant configured progression role. Discord's native role hierarchy still applies.

## Rules & Vibes onboarding

Authorized leadership can post the current agreement with `/admin onboarding-post`. Its persistent **I Agree** button records acceptance and can assign the configured New Member role. People already at New Member or above are not given an extra progression role, and the panel remains usable after restarts.

## Guild Planner

Planner uses the configured Raid channel and provides:

- `/event create`, `/event edit`, `/event cancel`, `/event stoprecurrence`, and `/event timezone`;
- One-time, Weekly recurring, and Monthly recurring schedules;
- native Discord Scheduled Events and restart-safe Planner cards;
- Tank, Healer, DPS, and Bench signups with linked-character selection;
- Maybe and Can't Attend states without character selection;
- automatic 24-hour and 1-hour reminders;
- independent occurrences, RSVPs, character snapshots, and reminder history;
- recurrence stopping without cancelling the current occurrence.

The organizer manages their event. The Discord guild owner and configured ZugBot Admin and Founder roles can also manage guild events. Editing or cancelling one recurring occurrence does not alter the future cadence.

### Planner permissions

ZugBot needs:

- View Channel
- Send Messages
- Embed Links
- Manage Events

Administrator is not required for normal Planner operation.

## Administrative utilities

`/debugdb` shows guild-scoped database and runtime counts. `/endkeys` closes active Mythic+ groups for the invoking guild and disables their buttons.

## Role-management safety

Promotion, demotion, and onboarding assignment require **Manage Roles**, and ZugBot's Discord role must sit above each role it manages. Configured authority never bypasses Discord's hierarchy.
