# Guild Administration

Each Discord server keeps its own ZugBot setup, leadership roles, and activity information.

## Server setup

Run `/setup`. The Discord server owner or a member with Administrator or Manage Server permission can change setup.

ZugBot can store Bot Commands, Mythic/LFG, Raid, and Announcement channels; Modern WoW and WoW: Forever preferences; a default game mode and region; and five authority/membership roles.

!!! note "Battle.net region"
    ZugBot's configured Battle.net region controls `/character`, confirmed character lists, manual `/link` lookups, and realm suggestions. Changing a server's default region in `/setup` does not currently change these lookups.

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

Authorized leaders can post the current agreement with `/admin onboarding-post`. The **I Agree** button records acceptance and can give the configured New Member role. People who already have New Member or a higher configured role are not given an extra role. The panel still works after ZugBot restarts.

## Guild Planner

Planner uses the configured Raid channel and provides:

- `/event create`, `/event edit`, `/event cancel`, `/event stoprecurrence`, and `/event timezone`;
- One-time, Weekly recurring, and Monthly recurring schedules;
- native Discord Scheduled Events and restart-safe Planner cards;
- Tank, Healer, DPS, and Bench signups with linked-character selection;
- Maybe and Can't Attend states without character selection;
- automatic 24-hour and 1-hour reminders;
- separate event dates, signups, saved character choices, and reminder history;
- a way to stop future dates without cancelling the current event.

The organizer manages their event. The Discord server owner and configured ZugBot Admin and Founder roles can also manage guild events. Editing or cancelling one date does not move future dates.

### Planner permissions

ZugBot needs:

- View Channel
- Send Messages
- Embed Links
- Manage Events

Administrator is not required for normal Planner operation.

## Administrative utilities

`/debugdb` shows saved-item and running-process counts for the current Discord server. `/endkeys` closes active Mythic+ groups in the current server and disables their buttons.

## Role-management safety

Promotion, demotion, and onboarding assignment require **Manage Roles**, and ZugBot's Discord role must sit above each role it manages. Configured authority never bypasses Discord's hierarchy.
