# -*- coding: utf-8 -*-
# ====================================================================
# Masala nomi    : A. Wrong Subtraction
# Masala havolasi: https://codeforces.com/problemset/problem/977/A
# Vaqt cheklovi  : time limit per test 1 second
# Xotira cheklovi: memory limit per test 256 megabytes
# ====================================================================


n, k = map(int, input().split())
while k != 0:
    if n % 10 == 0:
        n = n // 10
        k = k - 1
    else:
        n = n - 1
        k = k - 1
print(n)
