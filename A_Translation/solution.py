# -*- coding: utf-8 -*-
# ====================================================================
# Masala nomi    : A. Translation
# Masala havolasi: https://codeforces.com/problemset/problem/41/A
# Vaqt cheklovi  : time limit per test 1 second
# Xotira cheklovi: memory limit per test 256 megabytes
# ====================================================================


a = input()
b = input()
if a == b[::-1]:
    print("YES")
else:
    print("NO")
