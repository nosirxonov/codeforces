# -*- coding: utf-8 -*-
# ====================================================================
# Masala nomi    : A. Elephant
# Masala havolasi: https://codeforces.com/problemset/problem/617/A
# Vaqt cheklovi  : time limit per test 1 second
# Xotira cheklovi: memory limit per test 256 megabytes
# ====================================================================


n = int(input())
if n % 5 == 0:
    print(n // 5)
else:
    print(n // 5 + 1)
