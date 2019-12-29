import os
import numpy as np
import itertools
import random

os.chdir('/Users/z00294n/algorithms_coursera')


def mincut(g):
    while len(g) > 2:
        c1 = np.random.randint(0, len(g))
        v_del = g.pop(c1)
        # print("v_del:", v_del)
        c2 = np.random.randint(1, len(v_del))
        v1, v2 = v_del[0], v_del[c2]
        # print("v1, v2:", v1, v2)
        while v2 in v_del:
            v_del.remove(v2)
        for i in range(len(g)):
            if g[i][0] == v2:
                g[i] += v_del
                # print('g[i]:', g[i])
                while v1 in g[i]:
                    g[i].remove(v1)
            for j in range(len(g[i])):
                g[i][j] = v2 if g[i][j] == v1 else g[i][j]
    return len(g[0])-1

N = 1000
cut = []
for i in range(N):
    l = []
    with open('kargerMinCut.txt', 'r') as f:
        for sent in f:
              a = sent.split('\t')
              l.append([int(i) for i in a if i != a[-1]])
    cut += [mincut(l)]

print(min(cut))
