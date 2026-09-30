# Getting Started

ZugBot works through Discord slash commands and interactive buttons. Most members can begin using character, Guild Planner, and Mythic+ features once the bot is installed and the server has completed the relevant setup.

## For guild members

A good first session is:

1. Run `/link` to connect a World of Warcraft character to your Discord account.
2. Run `/profile` to view a linked character.
3. Use `/alts` to confirm your linked characters.
4. Check the guild's planner cards or Discord Scheduled Events for upcoming activities.
5. If you play Modern WoW Mythic+, run `/season` to see the active dungeon pool.
6. Use `/key` when you want to create a Mythic+ group.
7. Use `/lfgnotify enable` if you want ZugBot to DM you about eligible groups.

No unnecessary Battle.net sign-in is required for normal linked-character use.

## For server owners and administrators

Run:

```text
/setup
```

Basic setup requires:

- a **Bot Commands Channel**;
- a **Mythic/LFG Channel**;
- an enabled default game mode.

The setup interface can also configure:

- Raid Channel
- Announcement Channel
- default region
- Modern WoW enabled/disabled
- WoW: Forever enabled/disabled
- default game mode
- Admin role
- Founder role
- Moderator role
- Member role
- New Member role

!!! note
    Raid, announcement, and role mappings are optional for basic setup, but the Guild Planner requires a configured Raid Channel and guild administration/onboarding features require the relevant role configuration.

## Guild Planner setup

Set an IANA timezone for event entry:

```text
/event timezone America/New_York
```

Then create an event with:

```text
/event create
```

ZugBot creates a matching Discord Scheduled Event and posts the persistent planner card in the configured Raid Channel.

## Discord permissions

ZugBot should have only the permissions needed for the features your server uses.

Common requirements include:

- View Channel
- Send Messages
- Embed Links
- Read Message History
- Manage Roles when ZugBot is expected to assign or change configured guild roles
- Manage Events when Guild Planner is enabled

For role management, ZugBot's Discord role must be above the roles it needs to manage.

Do not grant Administrator solely to make setup easier. Guild Planner does **not** require Administrator permission.

## Onboarding

Servers can use a Rules & Vibes agreement as a simple gate for new members.

A common flow is:

```text
#welcome → #rules-and-vibes → I Agree → New Member role
```

The server owner or authorized leadership posts the active agreement with:

```text
/admin onboarding-post
```

The exact role names are chosen by each Discord server; ZugBot stores the role mapping rather than requiring fixed Discord role names.
