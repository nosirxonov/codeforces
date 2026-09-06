# -*- coding: utf-8 -*-
# ====================================================================
# Masala nomi    : A. Team
# Masala havolasi: https://codeforces.com/problemset/problem/231/A
# Vaqt cheklovi  : time limit per test 2 seconds
# Xotira cheklovi: memory limit per test 256 megabytes
# ====================================================================


n = int(input())
x = 0
for i in range(n):
    m = list(map(int, input().split()))
    if m.count(1) >= 2:
        x = x + 1
print(x)
