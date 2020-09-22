import random
from math import floor, tanh
from config import *


def probability(x, function):
    if function == 'tanh':
        return tanh(0.5 * x + 0.5)
    else:
        return 1 / (1 + x * 0.5)


def spider_trapped(history_nodes, current, function):
    history_nodes_reversed = history_nodes[::-1]
    try:
        last_time = history_nodes_reversed[1:].index(current)
        if function == 'repeat':
            prev_last_time = history_nodes_reversed[last_time+2]
            prev_current = history_nodes_reversed[1]
            if prev_current == prev_last_time:
                return True
            else:
                return False
        else:
            return random.random() < probability(last_time, function)
    except:
        return False


def finished(history):
    visited = set(history[:-1])
    return len(set(visited)) == nodes


def walk(G, prob_function):

    r = [1 / nodes for i in range(nodes)]
    r.append('')
    history_r = []

    # Data for counting method
    r_c = [0 for i in range(nodes)]
    r_c.append('')
    history_r_c = []

    history_nodes = []
    focus = floor(random.random() * nodes)

    history_nodes.append(focus)
    history_r.append(r.copy())
    history_r_c.append(r_c.copy())
    while not finished(history_nodes):

        # r_prime = [0 for i in range(nodes)]
        out = list(G[focus].keys())
        _in = [edge[0] for edge in G.in_edges(focus)]
        previous_r = history_r[-1]

        if not _in:
            r[focus] = 0
        else:
            for i in _in:
                r[focus] += previous_r[i] / len(G[i])

        r_c[focus] += 1

        if not out or spider_trapped(history_nodes, focus, prob_function):
            if not out:
                r[-1] = 'dead end'
                r_c[-1] = 'dead end'
            else:
                r[-1] = 'teleport'
                r_c[-1] = 'teleport'
            focus = random.choice(range(nodes))
            history_nodes.append(focus)
            history_r.append(r.copy())
            history_r_c.append(r_c.copy())
            r[-1] = ''
            r_c[-1] = ''
            continue

        focus = random.choice(out)
        history_nodes.append(focus)
        history_r.append(r.copy())
        history_r_c.append(r_c.copy())
    return r, history_r, r_c, history_r_c
