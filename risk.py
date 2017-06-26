#!/usr/bin/env python3

import itertools
import prettytable
import sys

# p_die is the sides of a die.
p_die = [1, 2, 3, 4, 5, 6]
max_a_dice = 3
max_d_dice = 2
html = False

# Returns a tuple containing the probabilistic result of a dice-throw battle.
#
# The return value is a 2-tuple, (AVG, PROBS), where AVG is the fraction
# specifying the average number of armies the attacker wins, overall, and where
# PROBS is a list of the probabilities for each outcome, with the 0th element
# being the probability of the attacker winning 0 armies, the 1st element being
# the probability of the attacker winning 1 army, etc.
#
# na: Number of dice the attacker throws.
# nd: Number of dice the defender throws.
#
def p_battle(na, nd):
    stake = min(na, nd)
    assert(1 <= na)
    assert(1 <= nd)
    win_table = [0] * (stake + 1)
    n_total_wins = 0
    a_perms = [sorted(x, reverse=True) for x in itertools.product(p_die, repeat=na)]
    d_perms = [sorted(x, reverse=True) for x in itertools.product(p_die, repeat=nd)]
    for a_throw, d_throw in itertools.product(a_perms, d_perms):
        n_subwins = sum(map(lambda i: 1 if a_throw[i] > d_throw[i] else 0, range(stake)))
        win_table[n_subwins] += 1
        n_total_wins += n_subwins
    sum_average = n_total_wins / len(a_perms) / len(d_perms) / min(na, nd)
    win_table = [n / len(a_perms) / len(d_perms) for n in win_table]
    return sum_average, [win_table[i] for i in range(stake, -1, -1)]

def main():
    columns = ['A/D', 'AVG']
    for i in range(1, min(max_a_dice, max_d_dice)+1):
        for j in range(0, i+1):
            columns.append('A{}D{}'.format(i-j, j))
    t = prettytable.PrettyTable(columns)
    for na in range(1, max_a_dice+1):
        for nd in range(1, max_d_dice+1):
            cells = ['{}/{}'.format(na, nd)]
            avg, probs = p_battle(na, nd)
            cells.append('{:5.2f}'.format(100*avg))
            stake = min(na, nd)
            for i in range((stake+1) * stake // 2 - 1):
                cells.append('')
            for i in range(stake + 1):
                cells.append('{:5.2f}'.format(100*probs[i]))
            while len(cells) < len(columns):
                cells.append('')
            t.add_row(cells)
    if html:
        print(t.get_html_string())
    else:
        print(t.get_string())

if __name__ == '__main__':
    def var(arg, label, default):
        if arg.startswith(label + '='):
            return eval(arg[len(label)+1:])
        return default
    for x in sys.argv:
        p_die = var(x, 'p_die', p_die)
        max_a_dice = var(x, 'max_a_dice', max_a_dice)
        max_d_dice = var(x, 'max_d_dice', max_d_dice)
        html = var(x, 'html', html)
    main()
