# -*- coding: utf-8 -*-
# ====================================================================
# Masala nomi    : A. Nearly Lucky Number
# Masala havolasi: https://codeforces.com/problemset/problem/110/A
# Vaqt cheklovi  : time limit per test 2 seconds
# Xotira cheklovi: memory limit per test 256 megabytes
# ====================================================================


n = input().strip()
x = 0
for i in n:
    if i == "7" or i == "4":
        x += 1
if x == 7 or x == 4:
    print("YES")
else:
    print("NO")
