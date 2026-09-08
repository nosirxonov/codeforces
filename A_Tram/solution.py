# -*- coding: utf-8 -*-
# ====================================================================
# Masala nomi    : A. Tram
# Masala havolasi: https://codeforces.com/problemset/problem/116/A
# Vaqt cheklovi  : time limit per test 2 seconds
# Xotira cheklovi: memory limit per test 256 megabytes
# ====================================================================


n = int(input())

maxs = []
z = 0

for _ in range(n):
    a, b = map(int, input().split())
    x = z - a + b
    z = x
    maxs.append(z)

print(max(maxs))
