# -*- coding: utf-8 -*-
# ====================================================================
# Masala nomi    : A. Stones on the Table
# Masala havolasi: https://codeforces.com/problemset/problem/266/A
# Vaqt cheklovi  : time limit per test 2 seconds
# Xotira cheklovi: memory limit per test 256 megabytes
# ====================================================================


n = int(input())
t = input()
x = ""
y = 0
for i in t:
    if x == i:
        y += 1
    else:
        x = i
print(y)
