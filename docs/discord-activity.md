# Discord Activity — Guild Command Center

**Released in Production · November 2026**

ZugBot now has a graphical Guild Command Center that runs **inside Discord**, alongside its existing slash commands and buttons. You can explore guild activity, plan events, coordinate groups, manage characters, play Tavern games, and — if authorized — access staff tools.

!!! info "Launch in Discord, not on this website"
    zugbot.net is the documentation site. To launch the Activity, ZugBot must be installed and enabled in your Discord server.

## Launch ZugBot

1. Open a supported Discord server and a channel that allows Activities.
2. Open the **App Launcher**, choose **ZugBot**, and launch the Activity.
3. If Discord asks, authorize the limited **identify** and **guilds** scopes.
4. Navigate using the Activity's sidebar. It only shows features you have permission to use.

Ordinary members do not need developer access or App Tester status to launch the released Activity in an approved server.

## Explore the Guild Hall

| Section | What it provides |
| --- | --- |
| **Dashboard** | Upcoming events, Retail Mythic+ groups, WoW: Forever groups, your characters, and game-world configuration |
| **Events** | Guild calendar, event details, role signups, and authorized one-time, weekly, or monthly event management |
| **Groups** | Retail WoW Mythic+ coordination and WoW: Forever dungeon groups |
| **Characters** | Your linked roster, optional Battle.net verification, and public character lookup with explicit Discord posting |
| **Fun** | Peon wisdom, dice, coins, beer, **ZugBot's Brewfest Keg**, and **Peon Fight Club** |
| **Report an incident** | Submit a guild-scoped report for authorized staff review |
| **Leadership** | Permission-controlled directory, casework, onboarding, announcements, and eligible server operations |
| **Guild Setup** | Guild configuration, with additional safeguards for protected channel and authority-role changes |

## Choose where to post

Fun posts, public character cards, and battle challenges use channels you select. ZugBot checks both your Discord access and the bot's permissions. It will not silently post your private Activity draft or offer an inaccessible channel.

## Staff access is permission-controlled

A member with overlapping configured roles receives the **highest valid configured authority tier**. ZugBot then checks the actual Discord permissions, bot permissions, role hierarchy, channel overrides, and specific operation policy. Discord Administrator permission alone does not supply an unconfigured ZugBot tier.

**Formal moderation writes are disabled in the current Production deployment**, including warnings, rescissions, timeouts, kicks, bans, unbans, and formal case resolutions. Authorized staff reads, incident reporting, and other eligible tools remain available. Optional automatic Peon Champion Discord role assignment is disabled too.

For more, see the [Guild Administration guide](admin-guide.md).

## Related guides

- [Getting Started](getting-started.md) — first launch, setup, and linking
- [Member Guide](member-guide.md) — characters, groups, and notifications
- [Guild Planner](planner.md) — event scheduling and recurring dates
- [Peon Fight Club](peon-fight-club.md) — rules, championship, cancel, and restore
- [Troubleshooting](troubleshooting.md) — access and gameplay problems
- [Privacy Policy](privacy.md) — handling of Discord and guild data

**AI chat is not yet a released ZugBot Activity feature.** The [Roadmap](roadmap.md) distinguishes planned local AI from available functionality.
