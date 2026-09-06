# -*- coding: utf-8 -*-
# ====================================================================
# Masala nomi    : A. Beautiful Matrix
# Masala havolasi: https://codeforces.com/problemset/problem/263/A
# Vaqt cheklovi  : time limit per test 2 seconds
# Xotira cheklovi: memory limit per test 256 megabytes
# ====================================================================


mtr = []
for a in range(5):
    row = list(map(int, input().split()))
    mtr.append(row)
 
for i in range(5):
    for j in range(5):
        if mtr[i][j] == 1:
            x, y = i, j
 
print(abs(x - 2) + abs(y - 2))
