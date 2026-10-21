# Troubleshooting

## A slash command is missing

Discord command registration can take time after an update. Confirm ZugBot is online, try `/about`, and reopen Discord if its command picker looks stale. Roadmap items are not necessarily released commands.

## Realm autocomplete is empty

`/character` realm suggestions are cached from Blizzard's official realm index. A refresh can be temporarily affected by Blizzard API availability, and suggestions follow the ZugBot deployment's configured Blizzard region.

For `/character`, autocomplete failure does not disable manual slug entry. Enter the official slug directly and use the [Realm Slug Reference](realm-slugs.md) to check it. The guild `default_region` setting does not independently reroute character requests or suggestions.

## `/link` does not show verified characters

`/link` takes no arguments and opens an ephemeral panel. Its verified picker shows currently unlinked characters from your fresh Battle.net roster.

Run `/verify`, complete the Battle.net authorization, and click **Finish Verification**. Then try `/link` again. Characters already linked to your Discord account are normally excluded from suggestions.

If a fresh verification succeeded but the picker remains empty, Blizzard character data may be temporarily unavailable or every available roster character may already be linked. You can still choose **Add Manually** without OAuth.

## I am worried `/verify` is phishing

Start verification only from ZugBot's `/verify` command in Discord.

ZugBot will **never ask for your Battle.net password** in Discord, on zugbot.net, or in a ZugBot form. The sign-in page should be hosted by Battle.net; ZugBot currently sends authorization through `oauth.battle.net`.

Do not paste your password, OAuth authorization code, raw state value, access token, or the full sensitive callback URL into Discord or a support message. If the browser shows an unexpected domain, close the page and restart `/verify` from Discord.

See [Battle.net Verification & Privacy](verification.md) for what ZugBot receives temporarily and what it stores.

## Character not found

For `/character`, check the character spelling, the selected realm, and whether the character is available through Blizzard's API. If autocomplete is unavailable, verify the manual slug in the [Realm Slug Reference](realm-slugs.md). Temporary Blizzard API problems can also affect lookups.

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

With more than one linked character, Discord opens an ephemeral selector. ZugBot exposes at most 25 characters in that selector, with your main first. Use `/alts` to inspect the full linked list.

## A Planner reminder was not received

Confirm that the user is the organizer or is currently signed up as Tank, Healer, DPS, or Bench. Maybe and Can't Attend do not receive reminders. The user must still belong to the Discord guild, and their Discord DM/privacy settings must allow ZugBot to message them.

Reminder delivery is not guaranteed, and ZugBot does not promise retries.

## A recurring event did not behave as expected

Cancelling an occurrence is not the same as stopping recurrence. Cancellation affects only that occurrence and the series continues. To stop future occurrences while leaving the current occurrence intact, run:

```text
/event stoprecurrence planner_event_id:<id>
```

The card should show **Weekly — Stopped** or **Monthly — Stopped**. Monthly events anchored on the 29th, 30th, or 31st can clamp to the end of a shorter month and later return to the original anchor day.

Editing an occurrence changes only that occurrence and does not move the series cadence.

## Smart LFG DMs are missing

Run `/lfgnotify settings`, then `/lfgnotify test`. If the test fails, check Discord privacy settings for that server.

## Onboarding or progression fails

For onboarding, confirm that all five roles are configured, ZugBot has Manage Roles, its role is above New Member, and the active onboarding panel is current. For promotion or demotion, also check Discord's native hierarchy; ZugBot authority does not bypass it.

## `/version` shows `unknown` for branch or commit

The bot may still be operating normally. Branch and commit are runtime diagnostics, and they depend on the production process being able to execute Git in its environment.

## Something still looks wrong

Use `/about` to confirm ZugBot responds and `/version` to capture the release. When reporting a problem, include the command, error, running version, and whether it affects one user or the whole server.

Contact [support@zugbot.net](mailto:support@zugbot.net) for help. Do not send passwords, tokens, OAuth codes, state values, or sensitive callback URLs.
