# Guild Administration

ZugBot's administration features are guild-scoped. Configuration and progression in one Discord server do not automatically apply to another.

## Server setup

Run `/setup` inside the Discord server.

The server owner or a member with Discord **Administrator** or **Manage Server** permission can change setup.

### Channels

ZugBot can store:

- Bot Commands Channel
- Mythic/LFG Channel
- Raid Channel
- Announcement Channel

### Game preferences

ZugBot stores:

- default region
- whether Modern WoW is enabled
- whether WoW: Forever is enabled
- the default game mode

Modern and Forever configuration exists today, but current `/key` behavior is the Modern Mythic+ flow. A separate Forever dungeon-group system is planned rather than pretending Forever uses Retail Mythic+ keys.

## Five-role authority model

ZugBot's configured hierarchy is:

```text
Admin > Founder > Moderator > Member > New Member
```

The Discord server chooses which actual Discord roles map to those five tiers.

The guild owner is treated as root authority by ZugBot even without the configured Admin role.

### Normal progression

Normal member progression is:

```text
New Member ⇄ Member ⇄ Moderator
```

Founder and Admin are protected authority tiers and are not ordinary promotion steps.

Use:

- `/admin promote`
- `/admin demote`

ZugBot changes only the configured progression role involved in the transition. Discord's own role hierarchy and permission rules still apply.

## Rules & Vibes onboarding

Once the five authority roles are configured, authorized leadership can post the active onboarding agreement with:

```text
/admin onboarding-post
```

The panel contains a persistent **I Agree** button.

When an eligible new user accepts:

- the agreement acceptance is recorded;
- the configured New Member role can be assigned;
- users already at New Member or a higher configured tier are not given an extra progression role;
- the panel remains restart-safe.

A server can pair this with channel permissions so unroled newcomers initially see only a welcome/rules area.

## Administrative utilities

### `/debugdb`

Shows guild-scoped database/runtime counts useful for troubleshooting.

### `/endkeys`

Closes active Mythic+ groups for the invoking guild and disables their interaction buttons.

## Role-management safety

For promotion, demotion, or onboarding role assignment:

- ZugBot needs Discord **Manage Roles**;
- the ZugBot Discord role must be above roles it needs to change;
- configured authority checks do not bypass Discord's own hierarchy;
- invalid or unsafe configuration should fail closed rather than guessing.
