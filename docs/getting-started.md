# Getting Started

ZugBot works through Discord slash commands and interactive buttons. Most members can begin using character and Mythic+ features immediately once the bot is installed and the server has completed basic setup.

## For guild members

A good first session is:

1. Run `/link` to connect a World of Warcraft character to your Discord account.
2. Run `/profile` to view a linked character.
3. Use `/alts` to confirm your linked characters.
4. If you play Modern WoW Mythic+, run `/season` to see the active dungeon pool.
5. Use `/key` when you want to create a Mythic+ group.
6. Use `/lfgnotify enable` if you want ZugBot to DM you about eligible groups.

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
    Raid, announcement, and role mappings are optional for basic setup, but guild administration and onboarding features require the relevant role configuration.

## Discord permissions

ZugBot should have only the permissions needed for the features your server uses.

Common requirements include:

- View Channel
- Send Messages
- Embed Links
- Read Message History
- Manage Roles when ZugBot is expected to assign or change configured guild roles

For role management, ZugBot's Discord role must be above the roles it needs to manage.

Do not grant Administrator solely to make setup easier.

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
