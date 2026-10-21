# Getting Started

ZugBot works through Discord slash commands, buttons, and selectors. Once the bot is installed and basic server setup is complete, members can verify character ownership, link characters, coordinate groups, and join Planner events without another dashboard.

## For guild members

A good first session is:

1. Run `/link` with no arguments. ZugBot opens an ephemeral character-linking panel that only you can see.
2. If you have a fresh Battle.net-verified roster, select one or more currently unlinked characters and click **Link Selected**. Use the roster pages when you have more than 25 eligible characters.
3. To link without Battle.net, click **Add Manually**. Enter one `CharacterName RealmSlug` per line and optionally fill in the separate **Make Main** field.
4. Run `/profile` to view a linked character and `/alts` to check every linked character.
5. Run `/season` to see the active Modern Mythic+ dungeon pool.
6. Use `/key` to create a Mythic+ group.
7. Use `/lfgnotify enable` to opt into Smart LFG direct messages for your chosen roles and key range.
8. Use Guild Planner cards to sign up as Tank, Healer, DPS, or Bench with a linked character, or choose Maybe or Can't Attend.

Battle.net OAuth is optional. Run `/verify` when you want ZugBot to mark matching characters as Battle.net verified and make a fresh verified roster available in `/link`.

!!! warning "Battle.net sign-in safety"
    ZugBot will never ask you to enter your Battle.net password on zugbot.net or in Discord. When you choose **Verify with Battle.net** from `/verify` or the `/link` character-linking panel, ZugBot redirects your browser to Battle.net's own sign-in and authorization page. Before entering credentials, confirm the browser address is on a `battle.net` domain. After authorization, Battle.net redirects you back to ZugBot to finish verification. If a page requesting Battle.net credentials is hosted on zugbot.net, Discord, or any non-`battle.net` domain, do not enter them. Never paste passwords, OAuth authorization codes, raw state values, access or refresh tokens, or sensitive callback URLs into Discord. See [Battle.net Verification & Privacy](verification.md) for the full flow and retention details.

## Character and realm selection

`/link` takes no arguments. Its ephemeral panel shows currently unlinked characters from your fresh, verified Battle.net roster and lets you select several in one batch. Rosters with more than 25 eligible characters are paginated. You can deliberately choose one selected character as your new Main; otherwise, your existing Main stays unchanged.

Verified batch linking is atomic: either the selected batch links successfully or none of it does. Each linked character inherits the original verification timestamps and expiry, so linking later does not restart or extend the 30-day proof.

If you do not want to use OAuth—or do not have a fresh verified roster—choose **Add Manually**. Enter one `CharacterName RealmSlug` per line. The separate **Make Main** field is optional; leave it blank to preserve your current Main. Manual links remain unverified. A later `/verify` upgrades exact matching manual links to Battle.net verified.

`/character` is a public lookup and continues to use Blizzard-backed realm autocomplete. Start typing the realm's display name and select the suggestion; ZugBot submits Blizzard's official realm slug internally. Manual slug entry remains available for `/character`.

You generally need the [Realm Slug Reference](realm-slugs.md) only for `/link`'s manual entry, manual public lookups, or troubleshooting. The former `/linkmany` command has been retired; its manual batch workflow now lives inside `/link`.

!!! note "Deployment region"
    Character lookups, verified rosters, and realm suggestions use the ZugBot deployment's configured Blizzard region. A guild's `default_region` setting does not independently reroute these requests.

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
