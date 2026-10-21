# Getting Started

ZugBot works through Discord slash commands, buttons, and selectors. Once the bot is installed and basic server setup is complete, members can verify character ownership, link characters, coordinate groups, and join Planner events without another dashboard.

## For guild members

A good first session is:

1. Run `/verify` in Discord and click **Verify with Battle.net**.
2. Sign in only on Battle.net's own authorization site. After the browser confirms the authorization, return to Discord and click **Finish Verification**.
3. Run `/link`, start typing a verified character or realm, choose the character from autocomplete, and select whether it is your **Main** or an **Alt**.
4. Run `/profile` to view a linked character and `/alts` to check every linked character.
5. Run `/season` to see the active Modern Mythic+ dungeon pool.
6. Use `/key` to create a Mythic+ group.
7. Use `/lfgnotify enable` to opt into Smart LFG direct messages for your chosen roles and key range.
8. Use Guild Planner cards to sign up as Tank, Healer, DPS, or Bench with a linked character, or choose Maybe or Can't Attend.

!!! warning "Battle.net sign-in safety"
    ZugBot will **never ask for your Battle.net password** in Discord, on zugbot.net, or in a ZugBot form. Enter Battle.net credentials only on Battle.net's own site. Never paste passwords, OAuth authorization codes, raw state values, tokens, or sensitive callback URLs into Discord. See [Battle.net Verification & Privacy](verification.md) for the full flow and retention details.

## Character and realm selection

`/link` searches your fresh, verified Battle.net character roster. Characters already linked to your Discord account are normally excluded from its suggestions. If the verified roster is missing or has expired, run `/verify` again.

`/character` is a public lookup and continues to use Blizzard-backed realm autocomplete. Start typing the realm's display name and select the suggestion; ZugBot submits Blizzard's official realm slug internally. Manual slug entry remains available for `/character`.

`/linkmany` remains a manual multi-link workflow and uses official realm slugs. You generally need the [Realm Slug Reference](realm-slugs.md) only for `/linkmany`, manual public lookups, or troubleshooting.

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
