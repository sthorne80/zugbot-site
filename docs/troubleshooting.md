# Troubleshooting

## A slash command is missing

Discord command registration can take a little time after a bot update.

First:

1. confirm ZugBot is online;
2. try another known command such as `/about`;
3. reopen Discord if the command picker appears stale.

If the missing command was only announced on the roadmap, it may not be released yet.

## `/key` says I have no linked characters

Run `/link` first, then try `/key` again.

Use `/alts` to confirm what ZugBot currently has linked to your Discord account.

## My character lookup fails

Check:

- character spelling;
- realm spelling/slug;
- whether the character is publicly available through Blizzard's APIs.

Temporary Blizzard API problems can also cause lookups to fail.

## I am not receiving Smart LFG DMs

Run:

```text
/lfgnotify settings
```

Then test delivery with:

```text
/lfgnotify test
```

If the test fails, check your Discord privacy settings for that server.

## Onboarding does not assign the New Member role

Server leadership should check:

- all five ZugBot authority/membership roles are configured;
- ZugBot has **Manage Roles**;
- ZugBot's Discord role is above the configured New Member role;
- the active onboarding panel is the current one.

## Promote/demote fails

Check both ZugBot configuration and Discord's native role hierarchy.

The command will not bypass Discord permissions simply because a user has authority inside ZugBot.

## `/version` shows `unknown` for branch or commit

The bot can still be running normally. Those fields are runtime diagnostics and depend on the production process being able to execute Git in its environment.

## Something still looks wrong

Use `/about` to confirm ZugBot is responding and `/version` to capture the running version.

When reporting a problem, include:

- the command you ran;
- the error message shown by ZugBot;
- the running version;
- whether the issue affects one user or the whole server.
