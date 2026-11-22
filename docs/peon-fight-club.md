# Peon Fight Club

**Released · ZugBot Activity → Fun → Peon Fight Club**

Challenge a guildmate to a ridiculous D20 tavern duel. Two peons start with **30 HP**, secretly choose their moves, and watch ZugBot resolve the round once both players have acted. The bot saves combat history, victory commentary, trophies, and records.

## Challenge a guildmate

1. Launch the [Discord Activity](discord-activity.md) and open **Fun**.
2. Choose an eligible channel where both fighters and ZugBot can post and read message history.
3. Under Peon Fight Club, search for an opponent. Optionally select a linked Retail WoW or WoW: Forever character as your costume.
4. Click **Challenge to Peon Fight Club**. The selected Discord channel receives the battle message.
5. Only the challenged player can **Accept Challenge** or **Decline Challenge**.

**New challenges expire after 24 hours** if unanswered. An existing challenge retains its original saved deadline. Before acceptance, the challenger can click **Cancel Challenge**, confirm, and immediately free the pair for another challenge. Cancellations and declines award no wins or losses.

## Choose a move each round

| Move | Effect |
| --- | --- |
| **Attack** | Roll a D20 using the damage table below |
| **Defend** | Forego attacking and halve incoming damage (rounded down) |
| **Special** | Brewfest Shovel Swing adds **3 damage** to a successful attack; two full rounds must pass before it can be used again |
| **Recover** | Forego attacking and recover up to **4 HP**, capped at 30, before incoming damage |

| D20 | Outcome | Damage |
| --- | --- | ---: |
| 1 | Critical failure | 0 |
| 2–9 | Miss | 0 |
| 10–14 | Hit | 6 |
| 15–19 | Strong hit | 9 |
| 20 | Critical hit | 14 |

Both choices are private until the round resolves. Then the dice, results, HP, and commentary are recorded in the **Combat Journal**. **Each active round has a 15-minute deadline.**

The fight ends at a knockout or after at most 15 rounds. If both survive round 15, higher HP wins; equal HP is a draw. Simultaneous knockouts are draws. A forfeit awards a win to the opponent.

## Resume, cancel, or restore after a deleted message

Your match is saved independently of its Discord message.

1. Return to **Fun → Peon Fight Club → Fights and results**.
2. Click **Refresh fights**, select your fight, and use the pagination controls if needed.
3. For a pending challenge you sent, choose **Cancel Challenge** and confirm.
4. For a missing Discord battle message, a participating fighter can choose **Restore Battle Message**. ZugBot verifies channel access and that the original message was deleted before posting a replacement.
5. An active match retains its current HP, round, locked private choices, and history. Restoring does not reset its deadline.

If Discord cannot confirm whether a message was delivered, ZugBot avoids automatically reposting and risking duplicates. Eligible fighters can still use the Activity where their saved fight state permits it.

## Championship and Hall of Fame

Qualifying decisive victories can award the **Reigning Peon Champion** trophy, a title that lasts **24 hours** and may be renewed or transferred. The **Hall of Fame** shows battle records and previous champions. Open **View Combat Journal** to replay saved rounds.

Only fighters may submit their own actions. Spectators can view battle records only if they can view the originating channel and read its message history. Private choices remain hidden until the round resolves.

Champion titles are currently **cosmetic**: automatic Discord role assignment is not enabled in Production. The game has no cash stakes or real-world prizes.

See [Troubleshooting](troubleshooting.md) or [Discord Activity](discord-activity.md) for more help.
