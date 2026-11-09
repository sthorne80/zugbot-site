# WoW: Forever

## The short version

ZugBot supports both **Modern WoW** and **WoW: Forever** characters. Use `/link` for either game.

- Modern characters have a character name and realm.
- Forever characters use their full character name and do not use a realm in ZugBot.
- Modern and Forever each have their own Main character.
- One `/verify` Battle.net authorization can refresh both character lists when Forever information is available.

Connecting Battle.net is optional. You can add Forever characters manually instead.

## Link a Forever character with Battle.net

1. Type `/verify` in Discord.
2. Click **Verify with Battle.net**.
3. Complete sign-in on Battle.net's own website.
4. Return to Discord and click **Finish Verification**.
5. Type `/link`.
6. If ZugBot asks which game you want, choose **WoW: Forever**. Forever-only servers open this flow directly.
7. Select one or more characters from the private list.
8. Click **Link Selected**.

The list contains Forever characters Battle.net confirmed belong to the account you authorized. Verification lasts 30 days. If you prefer not to connect Battle.net, use the manual steps below.

## Link a Forever character manually

Run `/link`. If ZugBot asks which game you want, choose **WoW: Forever**. Then click **Add Manually** and enter one full character name per line:

```text
Abrakadaver Salwyn
Pallyamorous Smitegeist
```

**Do not add a realm.** WoW: Forever does not use realm fields in ZugBot. The second word is part of the full character name, not a realm.

ZugBot checks the public Forever profile before adding the character. A manual link is still shown as **Unverified** because a public profile does not prove who owns it. A later `/verify` can change the link to Verified when Battle.net confirms ownership.

## Forever Main character

Modern and Forever have independent Main characters. Changing your Forever Main does not change your Modern Main, and changing your Modern Main does not change your Forever Main.

You can choose a Main while linking or use `/main` later. Leaving **Make Main** blank preserves the current Main for that game.

## View and manage Forever characters

- `/alts` lists Modern and Forever characters in separate sections.
- `/profile` shows a Forever character's public Blizzard profile without a realm.
- `/main` lets you choose the game and set that game's Main.
- `/unlink` lets you choose the game and remove the intended character safely.

## What is not a Forever feature yet

In current Production 0.10.0:

- `/key` is for Modern WoW Mythic+ characters only.
- Guild Planner role signups use Modern WoW linked characters only.

Forever character linking, verification, profiles, Mains, and character management are released. Forever dungeon grouping and Forever Planner signups are not currently released.
