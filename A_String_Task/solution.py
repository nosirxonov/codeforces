# -*- coding: utf-8 -*-
# ====================================================================
# Masala nomi    : A. String Task
# Masala havolasi: https://codeforces.com/problemset/problem/118/A
# Vaqt cheklovi  : time limit per test 2 seconds
# Xotira cheklovi: memory limit per test 256 megabytes
# ====================================================================


a = input().lower()
x = ""
for i in a:
    if i == 'a' or i == 'o' or i == 'y' or i == 'e' or i == 'u' or i == 'i':
        continue
    else:
        x = x + '.' + i
print(x)
