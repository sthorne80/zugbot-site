# Getting Started

ZugBot works through Discord slash commands, buttons, and selectors. Once the bot is installed and basic server setup is complete, members can link characters, coordinate groups, and join Planner events without another account or dashboard.

## For guild members

A good first session is:

1. Run `/link`, type your character name, begin typing the realm name, and choose the human-readable realm suggestion. Select whether the character is your **Main** or an **Alt**.
2. Run `/profile` to view a linked character and `/alts` to check every linked character.
3. Run `/season` to see the active Modern WoW Mythic+ dungeon pool.
4. Use `/key` to create a Mythic+ group.
5. Use `/lfgnotify enable` to opt into Smart LFG direct messages for your chosen roles and key range.
6. Use Guild Planner cards to sign up as Tank, Healer, DPS, or Bench with a linked character, or choose Maybe or Can't Attend.

No Battle.net sign-in is required for normal linked-character use.

### Realm selection

`/character` and `/link` use Blizzard-backed realm autocomplete. Start typing the realm's display name and select the suggestion; ZugBot submits Blizzard's official realm slug internally. Manual slug entry still works if autocomplete is temporarily unavailable.

You generally need the [Realm Slug Reference](realm-slugs.md) only for `/linkmany`, manual entry, or troubleshooting.

!!! note "Deployment region"
    Character lookups and realm suggestions use the ZugBot deployment's configured Blizzard region. A guild's `default_region` setting does not independently reroute `/character` or `/link` requests.

## For server owners and administrators

Run `/setup` inside the Discord server.

Basic setup requires a **Bot Commands Channel**, a **Mythic/LFG Channel**, and an enabled default game mode. The setup interface can also configure Raid and Announcement channels, game preferences, and the Admin, Founder, Moderator, Member, and New Member roles.

Raid, announcement, and role mappings are optional for basic setup, but the related Planner, administration, and onboarding features require their relevant configuration.

## Discord permissions

Common permissions include View Channel, Send Messages, Embed Links, Read Message History, Manage Events for Guild Planner, and Manage Roles for configured role assignment and progression.

For role management, ZugBot's Discord role must be above every role it needs to manage. Do not grant Administrator solely to simplify setup; Guild Planner does not require it.

## Onboarding

Servers can use a Rules & Vibes agreement as a gate for new members:

```text
#welcome → #rules-and-vibes → I Agree → New Member role
```

Authorized leadership posts the current agreement with `/admin onboarding-post`. Each server chooses its actual role names; ZugBot stores the mappings rather than requiring fixed names.
