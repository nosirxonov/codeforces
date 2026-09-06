# -*- coding: utf-8 -*-
# ====================================================================
# Masala nomi    : A. Anton and Danik
# Masala havolasi: https://codeforces.com/problemset/problem/734/A
# Vaqt cheklovi  : time limit per test 1 second
# Xotira cheklovi: memory limit per test 256 megabytes
# ====================================================================


n = int(input())
w = input().strip()
a = 0
d = 0
for i in w:
    if i == "A":
        a += 1
    elif i == "D":
        d += 1
if a > d:
    print("Anton")
elif d > a:
    print("Danik")
else:
    print("Friendship")
