# -*- coding: utf-8 -*-
# ====================================================================
# Masala nomi    : A. Bit++
# Masala havolasi: https://codeforces.com/problemset/problem/282/A
# Vaqt cheklovi  : time limit per test 1 second
# Xotira cheklovi: memory limit per test 256 megabytes
# ====================================================================


n = int(input())
x = 0
for i in range(n):
    s = input()
    if s == "X++" or s == "++X":
        x = x + 1
    elif s == "X--" or s == "--X":
        x = x - 1
 
print(x)
