# _Risk_ odds

The board game _Risk_ generally favors an aggressive strategy, partly
owing to the rules defining battle outcomes based on dice throws.
However, small changes in these rules can lead to drastically different
results.

## Classic rules

Using classic _Risk_ rules, the attacker has the advantage per roll if
and only if the attacker throws more dice than the defender. Here's a
table showing the probabilities per throw.

```
+-----+-------+-------+-------+-------+-------+-------+
| A/D |  AVG  |  A1D0 |  A0D1 |  A2D0 |  A1D1 |  A0D2 |
+-----+-------+-------+-------+-------+-------+-------+
| 1/1 | 41.67 | 41.67 | 58.33 |       |       |       |
| 1/2 | 25.46 | 25.46 | 74.54 |       |       |       |
| 2/1 | 57.87 | 57.87 | 42.13 |       |       |       |
| 2/2 | 38.97 |       |       | 22.76 | 32.41 | 44.83 |
| 3/1 | 65.97 | 65.97 | 34.03 |       |       |       |
| 3/2 | 53.95 |       |       | 37.17 | 33.58 | 29.26 |
+-----+-------+-------+-------+-------+-------+-------+
```

### How to read the table

The way to read the table is to first determine the row by taking the
number of dice the attacker throws and the number of dice the defender
throws. For example, if the attacker throws two dice and the defender
throws one die, then use the row with `2/1` in its `A/D` column.

In that row, the `AVG` cell specifies the average number of armies the
attacker will win per 100 army deaths. *A bigger number is better for
the attacker.* For example, if the `AVG` value is `57.87`, then, over
the course of the attacker and defender losing a combined total of 100
armies, the defender will average losing 57.87 armies and attacker will
average losing the other 42.13 armies. As another example, an `AVG`
value of `75.00` suggests that the attack will lose about one army for
every three armies the defender loses.

The other columns specify the probabilities of specific outcomes,
expressed as percentages. For example, a value of `60.00` in the `A1D0`
column would mean that there is a 60% chance per roll that the attacker
will win one army and lose none. Whereas, a `70.00` value in the `A1D1`
column would mean that there is a 70% chance per roll that the attacker
and defender will each lose one army.

## Non-standard game configurations

### Using more dice

One simple change to _Risk_ is to allow the attacker and/or defender to
roll more dice. Here's a table showing probabilities for using as many
as four dice per attacker and defender.

```
+-----+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+
| A/D |  AVG  |  A1D0 |  A0D1 |  A2D0 |  A1D1 |  A0D2 |  A3D0 |  A2D1 |  A1D2 |  A0D3 |  A4D0 |  A3D1 |  A2D2 |  A1D3 |  A0D4 |
+-----+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+
| 1/1 | 41.67 | 41.67 | 58.33 |       |       |       |       |       |       |       |       |       |       |       |       |
| 1/2 | 25.46 | 25.46 | 74.54 |       |       |       |       |       |       |       |       |       |       |       |       |
| 1/3 | 17.36 | 17.36 | 82.64 |       |       |       |       |       |       |       |       |       |       |       |       |
| 1/4 | 12.59 | 12.59 | 87.41 |       |       |       |       |       |       |       |       |       |       |       |       |
| 2/1 | 57.87 | 57.87 | 42.13 |       |       |       |       |       |       |       |       |       |       |       |       |
| 2/2 | 38.97 |       |       | 22.76 | 32.41 | 44.83 |       |       |       |       |       |       |       |       |       |
| 2/3 | 25.33 |       |       | 12.59 | 25.48 | 61.93 |       |       |       |       |       |       |       |       |       |
| 2/4 | 17.66 |       |       |  7.59 | 20.13 | 72.27 |       |       |       |       |       |       |       |       |       |
| 3/1 | 65.97 | 65.97 | 34.03 |       |       |       |       |       |       |       |       |       |       |       |       |
| 3/2 | 53.95 |       |       | 37.17 | 33.58 | 29.26 |       |       |       |       |       |       |       |       |       |
| 3/3 | 36.90 |       |       |       |       |       | 13.76 | 21.47 | 26.47 | 38.30 |       |       |       |       |       |
| 3/4 | 25.02 |       |       |       |       |       |  7.33 | 14.84 | 23.41 | 54.42 |       |       |       |       |       |
| 4/1 | 70.74 | 70.74 | 29.26 |       |       |       |       |       |       |       |       |       |       |       |       |
| 4/2 | 62.49 |       |       | 45.91 | 33.16 | 20.93 |       |       |       |       |       |       |       |       |       |
| 4/3 | 50.84 |       |       |       |       |       | 25.11 | 26.29 | 24.60 | 24.00 |       |       |       |       |       |
| 4/4 | 35.21 |       |       |       |       |       |       |       |       |       |  8.74 | 15.12 | 18.90 | 22.72 | 34.52 |
+-----+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+
```

An interesting case is the 3/3 roll, which significantly disfavors the
attacker compared to the standard 3/2 roll, with the `AVG` down from
**53.95** to **36.90**. Of course, the defender would need at least
three armies in their territory to be eligible for this roll, but this
one difference could tip the equilibrium for the winning strategy from
aggressiveness to defensiveness. It's hard to say.

### Using different dice

#### _Betrayal at House on the Hill_

What about replacing _Risk_'s standard six-sided dice with the dice from
_Betrayal at House on the Hill_? In that game, the dice are six-sided
but show only the three values 0, 1, and 2, with each number appearing
on two faces. Here's the table, again calculated for allowing more dice.

```
+-----+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+
| A/D |  AVG  |  A1D0 |  A0D1 |  A2D0 |  A1D1 |  A0D2 |  A3D0 |  A2D1 |  A1D2 |  A0D3 |  A4D0 |  A3D1 |  A2D2 |  A1D3 |  A0D4 |
+-----+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+
| 1/1 | 33.33 | 33.33 | 66.67 |       |       |       |       |       |       |       |       |       |       |       |       |
| 1/2 | 18.52 | 18.52 | 81.48 |       |       |       |       |       |       |       |       |       |       |       |       |
| 1/3 | 11.11 | 11.11 | 88.89 |       |       |       |       |       |       |       |       |       |       |       |       |
| 1/4 |  7.00 |  7.00 | 93.00 |       |       |       |       |       |       |       |       |       |       |       |       |
| 2/1 | 48.15 | 48.15 | 51.85 |       |       |       |       |       |       |       |       |       |       |       |       |
| 2/2 | 28.40 |       |       | 13.58 | 29.63 | 56.79 |       |       |       |       |       |       |       |       |       |
| 2/3 | 17.28 |       |       |  7.00 | 20.58 | 72.43 |       |       |       |       |       |       |       |       |       |
| 2/4 | 10.84 |       |       |  3.70 | 14.27 | 82.03 |       |       |       |       |       |       |       |       |       |
| 3/1 | 55.56 | 55.56 | 44.44 |       |       |       |       |       |       |       |       |       |       |       |       |
| 3/2 | 41.98 |       |       | 24.28 | 35.39 | 40.33 |       |       |       |       |       |       |       |       |       |
| 3/3 | 25.10 |       |       |       |       |       |  5.76 | 16.05 | 25.93 | 52.26 |       |       |       |       |       |
| 3/4 | 16.26 |       |       |       |       |       |  2.97 |  9.79 | 20.30 | 66.94 |       |       |       |       |       |
| 4/1 | 59.67 | 59.67 | 40.33 |       |       |       |       |       |       |       |       |       |       |       |       |
| 4/2 | 50.34 |       |       | 31.14 | 38.41 | 30.45 |       |       |       |       |       |       |       |       |       |
| 4/3 | 37.24 |       |       |       |       |       | 12.21 | 23.59 | 27.89 | 36.31 |       |       |       |       |       |
| 4/4 | 22.79 |       |       |       |       |       |       |       |       |       |  2.48 |  8.78 | 15.73 | 23.41 | 49.60 |
+-----+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+
```

These dice tip the odds in the defender's favor for the 3/2 roll, down
from **53.95** in classic _Risk_ to **41.98**. In other words, the
attacker is trading about three armies for the defender's two.

Again, I wonder if this is a difference that would change the winning
strategy from offense to defense. Notice, however, that the 3/1 roll is
still favorable for the attacker—though only slightly so—which may be
important when the attacker is steamrolling through territories defended
with only one army, as is common in the end game.

#### Fair coin

Let's replace the standard six-sided dice with two-sided dice—otherwise
known as fair coins. Here's the table, calculated for allowing up to
four coins per player.

```
+-----+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+
| A/D |  AVG  |  A1D0 |  A0D1 |  A2D0 |  A1D1 |  A0D2 |  A3D0 |  A2D1 |  A1D2 |  A0D3 |  A4D0 |  A3D1 |  A2D2 |  A1D3 |  A0D4 |
+-----+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+
| 1/1 | 25.00 | 25.00 | 75.00 |       |       |       |       |       |       |       |       |       |       |       |       |
| 1/2 | 12.50 | 12.50 | 87.50 |       |       |       |       |       |       |       |       |       |       |       |       |
| 1/3 |  6.25 |  6.25 | 93.75 |       |       |       |       |       |       |       |       |       |       |       |       |
| 1/4 |  3.12 |  3.12 | 96.88 |       |       |       |       |       |       |       |       |       |       |       |       |
| 2/1 | 37.50 | 37.50 | 62.50 |       |       |       |       |       |       |       |       |       |       |       |       |
| 2/2 | 18.75 |       |       |  6.25 | 25.00 | 68.75 |       |       |       |       |       |       |       |       |       |
| 2/3 | 10.94 |       |       |  3.12 | 15.62 | 81.25 |       |       |       |       |       |       |       |       |       |
| 2/4 |  6.25 |       |       |  1.56 |  9.38 | 89.06 |       |       |       |       |       |       |       |       |       |
| 3/1 | 43.75 | 43.75 | 56.25 |       |       |       |       |       |       |       |       |       |       |       |       |
| 3/2 | 29.69 |       |       | 12.50 | 34.38 | 53.12 |       |       |       |       |       |       |       |       |       |
| 3/3 | 15.62 |       |       |       |       |       |  1.56 |  9.38 | 23.44 | 65.62 |       |       |       |       |       |
| 3/4 |  9.90 |       |       |       |       |       |  0.78 |  5.47 | 16.41 | 77.34 |       |       |       |       |       |
| 4/1 | 46.88 | 46.88 | 53.12 |       |       |       |       |       |       |       |       |       |       |       |       |
| 4/2 | 37.50 |       |       | 17.19 | 40.62 | 42.19 |       |       |       |       |       |       |       |       |       |
| 4/3 | 24.48 |       |       |       |       |       |  3.91 | 16.41 | 28.91 | 50.78 |       |       |       |       |       |
| 4/4 | 13.67 |       |       |       |       |       |       |       |       |       |  0.39 |  3.12 | 10.94 | 21.88 | 63.67 |
+-----+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+
```

This further exaggerates favor for the defender, decreasing the
`AVG` from **53.95** in classic _Risk_ down to **29.69**—roughly
equivalent to the attacker trading seven armies for every three from the
defender. Even the 3/1 case has an unfavorable `AVG` for the attacker,
at **43.75**, making even a steamroll maneuver costly.

I struggle to imagine this scenario not leading to stalemate, with
players amassing huge armies on their borders and no rational player
willing to engage on offense. Hence, I dub this “Zapp Brannigan _Risk_,”
where victory is possible only with overwhelming numbers and a
willingness to send wave after wave of your men at the enemy.
