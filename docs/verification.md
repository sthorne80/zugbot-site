# Battle.net Verification & Privacy

ZugBot can use Battle.net OAuth to verify that characters belong to the Discord member who is linking them. OAuth is optional: `/link` also supports manual bulk linking without a Battle.net sign-in.

!!! danger "Your Battle.net password does not go to ZugBot"
    ZugBot will never ask you to type your Battle.net password into Discord, zugbot.net, or a ZugBot form. Authentication happens on Battle.net's own site. Before entering credentials, verify that the browser is on a `battle.net` domain; ZugBot currently sends authorization through `oauth.battle.net`.

## How verification works

1. Run `/verify` in Discord.
2. Click **Verify with Battle.net**.
3. Your browser opens Battle.net's authorization flow.
4. Sign in on Battle.net and approve the requested access.
5. Battle.net redirects back to ZugBot's OAuth service. The service uses the short-lived authorization result to request the protected character list, then discards the sensitive OAuth material.
6. Return to Discord and click **Finish Verification**.
7. ZugBot stores a limited, sanitized verified character roster associated with your Discord user.
8. Run `/link`, select one or more currently unlinked characters from that verified roster, and click **Link Selected**. The panel paginates rosters with more than 25 eligible characters.

Verification is currently fresh for **30 days**. Running `/verify` again refreshes the roster and its verification window.

## What ZugBot stores

The persistent verified roster is intentionally limited to data needed to identify and link characters:

| Stored | Why |
| --- | --- |
| Discord user ID | Binds the verified roster to the member who completed verification |
| Region | Keeps roster identity scoped to the correct Battle.net region |
| Character and realm identity | Displays and matches characters for `/link` |
| Current character/realm identifiers when Battle.net supplies them | Additional evidence for the current snapshot; ZugBot does not treat them as permanent proof across realm transfers |
| Verification timestamps and expiry | Enforces the current 30-day freshness window |
| Server-derived normalized identity keys | Prevents duplicate or ambiguous character ownership records |

A fresh verification replaces that user's current regional roster. A character that disappears from a later Battle.net snapshot is no longer available as a current verified-roster choice. ZugBot does not automatically infer whether that means a rename, transfer, or deletion.

## What ZugBot does not persist

ZugBot does **not** persist:

- your Battle.net password;
- OAuth authorization codes;
- user OAuth access tokens;
- refresh tokens;
- the raw OAuth state value;
- raw Battle.net/UserInfo or protected-profile responses;
- OAuth request or response headers;
- sensitive callback parameters or URLs.

The OAuth service temporarily handles the authorization code and access token in memory because they are required to complete the OAuth exchange and fetch the protected character list. They are not written to the verified roster or stored for later use.

BattleTag/display-label information may exist only in the short-lived sanitized verification result while the OAuth session is waiting to be finished. It is **not copied into the persistent verified character roster**, and the temporary result is cleared when the completed verification is consumed.

## Linking from a verified roster

After `/verify`, ZugBot already has a fresh sanitized record of which characters Battle.net returned for your account. `/link` shows the currently unlinked entries from that roster for your Discord user. You can select several at once, move through pages when more than 25 are eligible, and deliberately choose a new Main. If you do not choose a Main, your existing Main remains unchanged.

When you submit the selection, ZugBot rechecks the roster rows, verifies that they are still fresh and belong to you, resolves the current public character profiles, and links the batch atomically. Either the full selected batch succeeds or none of it is applied. Every new link inherits the original roster verification timestamps and expiry. Linking later does **not** silently extend the 30-day verification window.

## Linking without OAuth

Run `/link`, then choose **Add Manually**. Enter one `CharacterName RealmSlug` per line. The separate **Make Main** field is optional; leaving it blank preserves your current Main.

Manual links remain unverified because manual entry does not prove account ownership. If you later complete `/verify`, exact matching manual links are upgraded to Battle.net verified.

## Phishing-safety checklist

Before signing in:

- start from ZugBot's `/verify` command in Discord;
- confirm the authorization page is on a `battle.net` domain;
- never send your password to a bot, Discord user, support ticket, or website form;
- never paste an OAuth code, raw state value, access token, or sensitive callback URL into Discord;
- if the domain looks wrong or the flow feels unexpected, close the page and restart `/verify` from Discord.

ZugBot support does not need your Battle.net password, OAuth token, authorization code, raw state value, or callback URL to troubleshoot verification.

## If verification expires

An expired roster cannot be used to create a newly verified link. Run `/verify` again to refresh ownership.

Existing linked characters are not automatically deleted just because the roster expires. Their displayed ownership state follows their stored verification freshness until it is refreshed.

For command instructions, see the [Member Guide](member-guide.md). For problems with the flow, see [Troubleshooting](troubleshooting.md).
