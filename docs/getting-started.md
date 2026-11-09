# Getting Started

ZugBot works through Discord slash commands, buttons, and private selectors. You do not need another dashboard.

## First choose your game

ZugBot supports two kinds of characters:

**Modern WoW**

- characters have a character name and realm;
- example: `Zugdealer` on `Thunderhorn`.

**WoW: Forever**

- characters use their full character name;
- no realm is required;
- example: `Abrakadaver Salwyn`.

## Your first character link

1. Type `/link` and press Enter.
2. If ZugBot asks which game you want, choose **Modern WoW** or **WoW: Forever**. Servers with only one enabled game open that flow directly.
3. In the private panel only you can see, choose characters Battle.net already confirmed, choose **Verify with Battle.net**, or click **Add Manually**.
4. Select or enter the characters you want to link.
5. Optionally choose a Main. Leave **Make Main** blank to keep the current Main for that game.
6. Run `/alts` to confirm your linked characters.

Modern and Forever have separate Main characters. Changing one does not change the other.

### If you do not want to connect Battle.net

Battle.net verification is optional. Run `/link`. If ZugBot asks which game you want, choose the intended game. Then click **Add Manually**.

- For Modern, enter one `CharacterName RealmSlug` per line. Realm slugs are explained later in the [Modern manual-link guide](member-guide.md#modern-manual-linking).
- For Forever, enter one full character name per line, such as `Abrakadaver Salwyn`. **Do not add a realm.**

Manual links show as Unverified. This means ZugBot found the public character but has not confirmed that the Battle.net account belongs to the Discord user. A later `/verify` can upgrade matching links.

### If you want Battle.net verification

1. Run `/verify`.
2. Click **Verify with Battle.net**.
3. Sign in only on Battle.net's own website and approve access.
4. Return to Discord and click **Finish Verification**.
5. Run `/link`. If ZugBot asks which game you want, choose it. Then select characters and click **Link Selected**.

One authorization refreshes both your Modern and Forever lists when Forever information is available. The confirmation lasts 30 days.

!!! warning "Battle.net sign-in safety"
    ZugBot never asks you to type your Battle.net password on zugbot.net or in Discord. Enter it only when the browser address is on a `battle.net` domain. Never paste passwords, sign-in codes, tokens, or sensitive return links into Discord. See [Battle.net Verification & Privacy](verification.md).

## What to try next

- `/profile` shows a linked Modern or Forever profile.
- `/alts` lists characters by game mode.
- `/season` shows the current Modern Mythic+ dungeon pool.
- `/key` creates a Modern WoW Mythic+ group.
- `/dungeon` creates a WoW: Forever dungeon group; choose your role and dungeon, then use the card to manage signups.
- `/event create` can schedule Modern or Forever events with character signups matching that game mode.

## For server owners and administrators

Run `/setup` inside the Discord server. Basic setup requires a **Bot Commands Channel**, a **Mythic/LFG Channel**, and an enabled default game mode.

The setup panel can enable Modern WoW, WoW: Forever, or both, and requires an enabled default game mode. When both games are enabled, `/link` still asks the member which game they want. When only one is enabled, `/link` opens that game directly. Enabling Forever provides Forever character linking, verification, profiles, `/dungeon` grouping, and Forever Guild Planner events. `/key` remains Modern WoW-only.

Raid, announcement, and role mappings are optional for basic setup, but their related Planner, administration, and onboarding features require the relevant configuration.

## Discord permissions

Common permissions include View Channel, Send Messages, Embed Links, Read Message History, Manage Events for Guild Planner, and Manage Roles for configured role assignment.

ZugBot's Discord role must be above every role it manages. Do not grant Administrator solely to simplify setup; Guild Planner does not require it.

## Onboarding

Authorized leaders can post the server's Rules & Vibes agreement with `/admin onboarding-post`. The **I Agree** button records acceptance and can give the configured New Member role.
