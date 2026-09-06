# -*- coding: utf-8 -*-
# ====================================================================
# Masala nomi    : A. Boy or Girl
# Masala havolasi: https://codeforces.com/problemset/problem/236/A
# Vaqt cheklovi  : time limit per test 1 second
# Xotira cheklovi: memory limit per test 256 megabytes
# ====================================================================


uname = input()
l = []
for i in uname:
    if i in l:
        continue
    else:
        l.append(i)
s = len(l)
if s % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
