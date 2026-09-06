# -*- coding: utf-8 -*-
# ====================================================================
# Masala nomi    : A. Beautiful Year
# Masala havolasi: https://codeforces.com/problemset/problem/271/A
# Vaqt cheklovi  : time limit per test 2 seconds
# Xotira cheklovi: memory limit per test 256 megabytes
# ====================================================================


n = input()
r = int(n[:4])
t = True
while t:
    r += 1
    l = []
    l.append(r // 1000)
    l.append(r % 1000 // 100)
    l.append(r % 100 // 10)
    l.append(r % 10)
    l = set(l)
    if len(l) < 4:
        continue
    else:
        print(r)
        t = False
