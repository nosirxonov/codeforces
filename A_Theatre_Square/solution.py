# -*- coding: utf-8 -*-
# ====================================================================
# Masala nomi    : A. Theatre Square
# Masala havolasi: https://codeforces.com/problemset/problem/1/A
# Vaqt cheklovi  : time limit per test 1 second
# Xotira cheklovi: memory limit per test 256 megabytes
# ====================================================================


n, m, a = map(int, input().split())
print(((n + a - 1) // a) * ((m + a - 1) // a))
