# Battle.net Verification & Privacy

Battle.net verification is optional. It lets ZugBot confirm which Modern WoW and WoW: Forever characters are on the Battle.net account you authorize. If you prefer not to connect Battle.net, use `/link` and choose **Add Manually**.

!!! danger "Enter your Battle.net password only on Battle.net"
    ZugBot never asks you to type your Battle.net password on zugbot.net or in Discord. After you click **Verify with Battle.net**, enter your password only when the browser address is on a `battle.net` domain. Never paste passwords, sign-in codes, tokens, or sensitive return links into Discord.

## Verify and link characters

1. Run `/verify` in Discord.
2. Click **Verify with Battle.net**.
3. Check that the sign-in page is on a `battle.net` domain.
4. Sign in and approve access.
5. Return to Discord and click **Finish Verification**.
6. Run `/link`.
7. If ZugBot asks which game you want, choose **Modern WoW** or **WoW: Forever**. Servers with one enabled game open that flow directly.
8. Select characters and click **Link Selected**.

One authorization refreshes both character lists when Blizzard's Forever information is available. If Forever cannot be refreshed temporarily, Modern verification can still finish and existing Forever verification is left unchanged.

Lists longer than 25 characters have page buttons. Verification lasts **30 days**. Linking a character later does not extend that period.

## What Verified and Unverified mean

**Verified** means Battle.net confirmed that character was on the account authorized by the Discord user during a current verification period.

**Unverified** means the character was added manually. ZugBot checks that the public character exists, but a public profile alone does not prove ownership.

Existing links are not automatically removed when verification expires. Run `/verify` again to refresh ownership confirmation.

## Link without Battle.net

Run `/link`. If ZugBot asks which game you want, choose the intended game. Then click **Add Manually**.

Modern format:

```text
CharacterName RealmSlug
```

Forever format:

```text
Abrakadaver Salwyn
```

Forever uses the full character name and no realm. See the [WoW: Forever guide](forever.md).

## Simple privacy summary

- ZugBot never collects or stores your Battle.net password.
- OAuth authorization codes and access tokens stay in memory and are not persisted.
- Raw OAuth state and raw Battle.net account responses are not persisted.
- BattleTag and the temporary display label are not stored in the long-term character roster.
- Temporary protected verification results are cleared after they are used.
- The OAuth API and Discord bot are isolated services with separate responsibilities.
- Logs record sanitized lifecycle status and counts, not codes, tokens, raw state, BattleTag, or raw account responses.

## Sign-in safety checklist

- Start from `/verify` in Discord.
- Enter your password only on a `battle.net` address.
- Never send support your password, sign-in code, token, or sensitive return link.
- If the address looks wrong, close the page and restart `/verify` from Discord.

## Technical details: stored character data

The long-term confirmed-character roster keeps only bounded information needed to offer and reconcile characters:

| Stored | Why |
| --- | --- |
| Discord user ID | Connects the confirmed list to the Discord member who verified |
| Battle.net region | Keeps the roster in the correct region |
| Modern character name and realm information | Displays and matches Modern characters |
| Modern character and realm IDs, when available | Helps identify the current Modern roster entry |
| Forever full display name | Displays the Forever character |
| Forever stable Blizzard character ID | Matches Forever ownership even if the visible name changes |
| Verification and expiration times | Applies the 30-day confirmation period |
| Server-created matching keys | Prevents duplicate or ambiguous records |

Forever characters do not have a realm field in ZugBot. Forever ownership reconciliation uses Blizzard's stable character ID rather than treating the visible full name as permanent identity.

A successful refresh replaces the relevant current roster. A temporary Forever API failure does not erase or extend existing Forever verification. Temporary OAuth material remains memory-only and is cleared after the verification flow completes.

For step-by-step character instructions, see the [Member Guide](member-guide.md). For problems, see [Troubleshooting](troubleshooting.md).
