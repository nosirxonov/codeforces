# -*- coding: utf-8 -*-
# ====================================================================
# Masala nomi    : A. Bear and Big Brother
# Masala havolasi: https://codeforces.com/problemset/problem/791/A
# Vaqt cheklovi  : time limit per test 1 second
# Xotira cheklovi: memory limit per test 256 megabytes
# ====================================================================


a, b = map(int, input().split())
x = 0
while a <= b:
    a = a * 3
    b = b * 2
    x += 1
print(x)
