# Guild Administration

Each Discord server keeps its own ZugBot setup, leadership roles, and activity information.

## Server setup

Run `/setup` or open **Guild Setup** in the [Discord Activity](discord-activity.md). Server owners and members with **Manage Server** can inspect setup. Protected authority-role and posting-channel changes require additional checks.

ZugBot can store Bot Commands, Mythic/LFG, Raid, and Announcement channels; Modern WoW and WoW: Forever enablement; a default game mode and region; and five authority/membership roles.

`/setup` stores which game modes are enabled and requires an enabled default game mode. In Production 0.11.0, that stored default does not silently choose a `/link` flow when both games are enabled. Instead:

- if both Modern and Forever are enabled, `/link` asks the member which game they want;
- if only one game is enabled, `/link` opens that game's flow directly.

Enabling Forever enables Forever character linking, verification, profiles, Mains, and character management, as well as Forever dungeon groups and Guild Planner events.

`/key` remains Modern Mythic+ only. Forever dungeon LFG uses `/dungeon`; Planner role character selection uses the event's selected game mode.

!!! note "Battle.net region"
    ZugBot's configured Battle.net region controls `/character`, confirmed character lists, manual `/link` lookups, and realm suggestions. Changing a server's default region in `/setup` does not currently change these lookups.

## Five-role authority model

The configured hierarchy is:

```text
Admin > Founder > Moderator > Member > New Member
```

The Discord server chooses the actual roles mapped to those tiers. The guild owner is ZugBot's root authority even without the configured Admin role. Members with overlapping mapped roles are evaluated at their **highest valid tier**: Admin + Founder + Moderator resolves to Admin, and Founder + Moderator resolves to Founder. A Discord Administrator permission alone does not create an unconfigured ZugBot authority tier.

Normal progression is:

```text
New Member ⇄ Member ⇄ Moderator
```

Founder and Admin are protected tiers, not ordinary promotion steps. Use `/admin promote` and `/admin demote`, or the eligible Leadership workflow. ZugBot rechecks the actor's and bot's Discord permissions, mapped tiers, target protections, and hierarchy. Rank changes use scoped role edits and preserve unrelated roles; an incomplete or uncertain transition is audited instead of silently reported as successful.

## The graphical Leadership workspace

Authorized staff can open **Leadership** in the [Discord Activity](discord-activity.md). Available sections depend on current permissions and may include Overview, Members, Moderation, Cases, Onboarding, Announcements, and Server Tools.

The member directory, administrative audits, confidential staff notes, and casework are not public. Guild members can **Report an incident**; authorized reviewers can inspect eligible private records. Staff operations also check channel access, bot permissions, Discord role hierarchy, and guild scope.

!!! warning "Production moderation write policy"
    Formal moderation writes — warnings, warning rescissions, timeouts, timeout removals, kicks, bans, unbans, and formal case resolutions — are currently **disabled in Production**. Displaying Leadership or viewing a case does not enable those actions. Automatic Peon Champion Discord role assignment is also disabled.

### Protected Guild Setup

A valid configured Admin or the actual server owner must authorize protected posting-channel and lower-tier role mappings, in addition to Manage Server. Only the actual server owner can change the Admin or Founder mappings or repair incomplete role mappings. ZugBot refreshes authorization before saving so an already-open Activity or Discord /setup menu cannot bypass the checks. Region, timezone, and game preferences retain their existing Manage Server requirement.

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

Planner role character selection uses Modern or Forever linked characters based on the event's game mode in Production 0.11.0.

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

Promotion, demotion, and onboarding assignment require **Manage Roles**, and ZugBot's Discord role must sit above each role it manages. Configured authority never bypasses Discord's hierarchy. Equal- or higher-tier targets, protected roles, and unsafe transitions are refused. Staff should review the proposed addition/removal before confirming.
