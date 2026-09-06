# -*- coding: utf-8 -*-
# ====================================================================
# Masala nomi    : A. Petya and Strings
# Masala havolasi: https://codeforces.com/problemset/problem/112/A
# Vaqt cheklovi  : time limit per test 2 seconds
# Xotira cheklovi: memory limit per test 256 megabytes
# ====================================================================


a = input().strip()
b = input().strip()
 
if a.lower() < b.lower():
    print(-1)
elif a.lower() > b.lower():
    print(1)
else:
    print(0)
