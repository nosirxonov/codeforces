# -*- coding: utf-8 -*-
# ====================================================================
# Masala nomi    : B. Queue at the School
# Masala havolasi: https://codeforces.com/problemset/problem/266/B
# Vaqt cheklovi  : time limit per test 2 seconds
# Xotira cheklovi: memory limit per test 256 megabytes
# ====================================================================


n, x = map(int, input().split())
childs = list(input())

for _ in range(x):
    i = 0
    while i < n - 1:
        if childs[i] == 'B' and childs[i + 1] == 'G':
            childs[i], childs[i + 1] = childs[i + 1], childs[i]
            i += 2
        else:
            i += 1

print("".join(childs))
