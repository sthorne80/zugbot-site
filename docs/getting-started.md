# Getting Started

ZugBot works through Discord slash commands, buttons, and selectors. Once the bot is installed and basic server setup is complete, members can verify character ownership, link characters, coordinate groups, and join Planner events without another dashboard.

## For guild members

A good first session is:

1. Type `/link` and press Enter. You do not need to fill anything in first. ZugBot opens a private character-linking panel that only you can see.
2. If you have connected Battle.net in the last 30 days, choose one or more of your characters and click **Link Selected**. If you have more than 25 characters, use the page buttons to see the rest.
3. To link without connecting Battle.net, click **Add Manually**. Enter one `CharacterName RealmSlug` per line. **Make Main** is optional; leave it blank to keep your current Main.
4. Run `/profile` to view a linked character and `/alts` to check every linked character.
5. Run `/season` to see the active Modern Mythic+ dungeon pool.
6. Use `/key` to create a Mythic+ group.
7. Use `/lfgnotify enable` to opt into Smart LFG direct messages for your chosen roles and key range.
8. Use Guild Planner cards to sign up as Tank, Healer, DPS, or Bench with a linked character, or choose Maybe or Can't Attend.

Connecting Battle.net is optional. Run `/verify` if you want ZugBot to confirm which characters are on your Battle.net account. Matching manual links can become Verified after you finish.

!!! warning "Battle.net sign-in safety"
    ZugBot will **never ask you to type your Battle.net password on zugbot.net or in Discord**. When you click **Verify with Battle.net**, your browser is sent to Battle.net's own sign-in and approval page. Before entering your password, check that the address is on a `battle.net` domain. After you approve access, Battle.net sends you back to ZugBot. If any page on zugbot.net, Discord, or another non-`battle.net` domain asks for your Battle.net password, do not enter it. Never paste passwords, sign-in codes, tokens, or sensitive return links into Discord. See [Battle.net Verification & Privacy](verification.md) for more details.

## Character and realm selection

Type `/link` and press Enter; you do not need to fill anything in first. The private panel shows characters that are not linked yet. If you connected Battle.net in the last 30 days, you can select several characters from the list. If there are more than 25, use the page buttons to move through the list. **Make Main** is optional; leave it blank to keep your current Main.

When you link several characters, ZugBot adds the whole group together. If one character cannot be added, none of them are added and your links stay unchanged. Fix the problem and try again. Linking characters later does not restart the 30-day confirmation period.

If you do not want to connect Battle.net, choose **Add Manually**. Enter one `CharacterName RealmSlug` per line. Manual links show as Unverified. If you run `/verify` later, ZugBot can change exact matches to Verified characters.

`/character` is a public lookup. Start typing the realm name and choose it from the suggestions. If suggestions are unavailable, you can type the realm's official slug yourself.

You generally need the [Realm Slug Reference](realm-slugs.md) only when adding characters manually, doing a manual public lookup, or troubleshooting. The old `/linkmany` command no longer exists because its job is now inside `/link`.

!!! note "Battle.net region"
    Character lookups, confirmed character lists, and realm suggestions currently use ZugBot's configured Battle.net region. Changing a server's default region does not change these lookups.

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
