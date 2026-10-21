# Troubleshooting

## A slash command is missing

Discord command registration can take time after an update. Confirm ZugBot is online, try `/about`, and reopen Discord if its command picker looks stale. Roadmap items are not necessarily released commands.

## Realm suggestions are empty

`/character` realm suggestions come from Blizzard's official realm list. They may be temporarily unavailable if Blizzard is having a problem. Suggestions use ZugBot's configured Battle.net region.

If the suggestions do not appear, enter the realm's official slug yourself and use the [Realm Slug Reference](realm-slugs.md) to check it. Changing a server's default region does not change these lookups.

## `/link` does not show verified characters

Type `/link` and press Enter; you do not need to fill anything in first. ZugBot opens a private panel that only you can see. If you connected Battle.net in the last 30 days, it shows your characters that are not linked yet.

Run `/verify`, click **Verify with Battle.net**, finish the steps on Battle.net, and click **Finish Verification** in Discord. Then try `/link` again. Characters already linked to your Discord account do not normally appear in the list.

If verification worked but the list is still empty, Blizzard's character information may be temporarily unavailable, or all available characters may already be linked. You can still choose **Add Manually** without connecting Battle.net.

## I am worried `/verify` is phishing

Start verification from ZugBot's `/verify` command in Discord, then click **Verify with Battle.net**.

Your browser should leave ZugBot and open Battle.net's own sign-in and approval page. ZugBot will **never ask you to type your Battle.net password on zugbot.net or in Discord**. Before entering your password, check that the browser address is on a `battle.net` domain. After you approve access, Battle.net sends you back to ZugBot.

If a page on zugbot.net, Discord, or another non-`battle.net` domain asks for your Battle.net password, do not enter it. Never paste your password, sign-in code, token, or sensitive return link into Discord or a support message. If the address looks wrong, close the page and restart `/verify` from Discord.

See [Battle.net Verification & Privacy](verification.md) for what ZugBot receives temporarily and what it stores.

## Character not found

For `/character`, check the character spelling and selected realm. If realm suggestions are unavailable, check the slug in the [Realm Slug Reference](realm-slugs.md). A temporary Blizzard problem can also affect lookups.

For `/link`'s verified picker, refresh with `/verify` and select the character from your roster. For **Add Manually**, check the character spelling and official realm slug, with one `CharacterName RealmSlug` entry per line.

## Manual linking fails

Run `/link`, choose **Add Manually**, and use the official realm slug from the [Realm Slug Reference](realm-slugs.md). Enter one character per line:

```text
CharacterName RealmSlug
CharacterName RealmSlug
```

Do not add `Main` or `Alt` to those lines. To change your Main, use the separate optional **Make Main** field; leave it blank to preserve your existing Main. Manual links remain unverified until a later `/verify` upgrades exact matches.

## `/key` says I have no linked characters

Run `/link` and use either the verified picker or **Add Manually**, then use `/alts` to check your linked characters before trying `/key` again.

## Planner role signup says to link first

Tank, Healer, DPS, and Bench require a linked character. Run `/link`, then use `/alts` to confirm the character is available. Battle.net verification is optional. Maybe and Can't Attend do not require a linked character.

## The Planner character selector is missing a character

With more than one linked character, Discord opens a private list that only you can see. It shows at most 25 characters, with your Main first. Use `/alts` to see every linked character.

## A Planner reminder was not received

Confirm that the user is the organizer or is currently signed up as Tank, Healer, DPS, or Bench. Maybe and Can't Attend do not receive reminders. The user must still belong to the Discord guild, and their Discord DM/privacy settings must allow ZugBot to message them.

Reminder delivery is not guaranteed, and ZugBot does not promise retries.

## A recurring event did not behave as expected

Cancelling one event date is not the same as stopping a repeating series. Cancelling affects only that date, and the series continues. To stop future dates while leaving the current event in place, run:

```text
/event stoprecurrence planner_event_id:<id>
```

The card should show **Weekly — Stopped** or **Monthly — Stopped**. A monthly event set for the 29th, 30th, or 31st moves to the last day of a shorter month, then returns to the original day when possible.

Editing one event date changes only that date and does not move future events.

## Smart LFG DMs are missing

Run `/lfgnotify settings`, then `/lfgnotify test`. If the test fails, check Discord privacy settings for that server.

## Onboarding or progression fails

For onboarding, confirm that all five roles are configured, ZugBot has Manage Roles, its role is above New Member, and the active onboarding panel is current. For promotion or demotion, also check Discord's native hierarchy; ZugBot authority does not bypass it.

## `/version` shows `unknown` for branch or commit

The bot may still be operating normally. Branch and commit are runtime diagnostics, and they depend on the production process being able to execute Git in its environment.

## Something still looks wrong

Use `/about` to confirm ZugBot responds and `/version` to capture the release. When reporting a problem, include the command, error, running version, and whether it affects one user or the whole server.

Contact [support@zugbot.net](mailto:support@zugbot.net) for help. Do not send passwords, sign-in codes, tokens, or sensitive return links.
