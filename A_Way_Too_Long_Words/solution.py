# -*- coding: utf-8 -*-
# ====================================================================
# Masala nomi    : A. Way Too Long Words
# Masala havolasi: https://codeforces.com/problemset/problem/71/A
# Vaqt cheklovi  : time limit per test 1 second
# Xotira cheklovi: memory limit per test 256 megabytes
# ====================================================================


n = int(input())
l = []
for i in range(n):
    w = input()
    if len(w) <= 10:
        l.append(w)
    else:
        f = w[0] + str(len(w) - 2) + w[len(w) - 1]
        l.append(f)
for j in l:
    print(j)
