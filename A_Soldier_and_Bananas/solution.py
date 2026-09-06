# -*- coding: utf-8 -*-
# ====================================================================
# Masala nomi    : A. Soldier and Bananas
# Masala havolasi: https://codeforces.com/problemset/problem/546/A
# Vaqt cheklovi  : time limit per test 1 second
# Xotira cheklovi: memory limit per test 256 megabytes
# ====================================================================


k, n, w = map(int, input().split())
s = 0
for i in range(w + 1):
    s += i * k
if n >= s:
    print(0)
else:
    print(s - n)
