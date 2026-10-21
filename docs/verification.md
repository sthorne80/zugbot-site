# Battle.net Verification & Privacy

Battle.net verification is optional. It lets ZugBot confirm which WoW characters are on your Battle.net account. If you do not want to connect Battle.net, you can still use `/link` and choose **Add Manually**.

!!! danger "Enter your Battle.net password only on Battle.net"
    ZugBot will never ask you to type your Battle.net password on zugbot.net or in Discord. When you click **Verify with Battle.net**, your browser is sent to Battle.net's own sign-in and approval page. Before entering your password, check that the browser address is on a `battle.net` domain. After you approve access, Battle.net sends you back to ZugBot to finish. If a page on zugbot.net, Discord, or any other non-`battle.net` domain asks for your Battle.net password, do not enter it.

## How to verify and link characters

1. Run `/verify` in Discord.
2. Click **Verify with Battle.net**.
3. Check that the browser address is on a `battle.net` domain.
4. Sign in to Battle.net and approve access.
5. Battle.net sends you back to ZugBot.
6. Return to Discord and click **Finish Verification**.
7. Type `/link` and press Enter. You do not need to fill anything in first.
8. In the private panel that only you can see, choose one or more characters and click **Link Selected**.

If you have more than 25 characters, use the page buttons to see the rest. **Make Main** is optional; leave it blank to keep your current Main.

ZugBot's confirmation currently lasts **30 days**. Run `/verify` again when you want to renew it.

## Simple privacy summary

ZugBot keeps enough information to remember which WoW characters were confirmed on your Battle.net account and when that confirmation expires.

- The confirmation currently lasts 30 days.
- ZugBot does not save your Battle.net password.
- ZugBot does not keep the temporary sign-in credentials or tokens used while connecting to Battle.net.
- Your BattleTag or display label is not kept in the long-term confirmed-character list.

## Linking several characters

If you verified with Battle.net, `/link` shows your characters that are not linked yet. You can select several at once.

ZugBot adds the whole group together. If one character cannot be added, none of them are added and your links stay unchanged. Fix the problem and try again. Linking characters later does not restart or extend the 30-day confirmation period.

## Linking without Battle.net

Type `/link` and press Enter, then choose **Add Manually**. Enter one character on each line in this format:

```text
CharacterName RealmSlug
CharacterName RealmSlug
```

**Make Main** is optional. Leave it blank to keep your current Main.

Manual links show as Unverified because typing a character name does not prove that it belongs to your Battle.net account. If you run `/verify` later, ZugBot can change exact matches to Verified characters.

The old `/linkmany` command no longer exists. Its job is now inside `/link`.

## Sign-in safety checklist

- Start from ZugBot's `/verify` command in Discord.
- After clicking **Verify with Battle.net**, check that the sign-in page is on a `battle.net` domain.
- Never enter your Battle.net password on zugbot.net, in Discord, or on another non-`battle.net` domain.
- Never paste passwords, sign-in codes, tokens, or sensitive return links into Discord or a support message.
- If the address looks wrong or anything feels unexpected, close the page and restart `/verify` from Discord.

ZugBot support does not need your Battle.net password or any sign-in code, token, or return link to help you.

## If verification expires

After 30 days, run `/verify` again before creating new Verified links. Existing linked characters are not automatically removed when the confirmation expires.

## Technical details (optional)

This section uses technical terms for readers who want to know exactly what is kept.

The long-term confirmed-character list contains:

| Stored | Why |
| --- | --- |
| Discord user ID | Connects the confirmed list to the Discord member who completed verification |
| Battle.net region | Keeps characters matched to the correct region |
| Character and realm names | Shows and matches characters in `/link` |
| Current character and realm IDs, when Battle.net provides them | Adds evidence for the current list; these IDs are not treated as permanent proof after a realm transfer |
| Confirmation time and expiration time | Applies the current 30-day limit |
| Server-created matching keys | Prevents duplicate or unclear character records |

A new verification replaces the user's previous list for that region. If a character is missing from a later Battle.net list, it is no longer offered as a currently confirmed choice. ZugBot does not guess whether the character was renamed, transferred, or deleted.

During sign-in, ZugBot briefly handles the Battle.net authorization code and access token in memory so it can request the protected character list. ZugBot does not write those temporary credentials to the confirmed-character list or save them for later use. It also does not save refresh tokens, the raw OAuth state value, raw Battle.net account responses, request or response headers, or sensitive callback details.

A BattleTag or display label may appear briefly while the sign-in is being completed. It is not copied into the long-term confirmed-character list, and the temporary result is cleared after verification finishes.

For command instructions, see the [Member Guide](member-guide.md). For problems with the flow, see [Troubleshooting](troubleshooting.md).
