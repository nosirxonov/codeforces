# -*- coding: utf-8 -*-
# ====================================================================
# Masala nomi    : A. Helpful Maths
# Masala havolasi: https://codeforces.com/problemset/problem/339/A
# Vaqt cheklovi  : time limit per test 2 seconds
# Xotira cheklovi: memory limit per test 256 megabytes
# ====================================================================


txt = input()
l = []
for i in txt:
    if i == "+":
        continue
    else:
        l.append(i)
l = sorted(l)
print("+".join(l))
