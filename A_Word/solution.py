# -*- coding: utf-8 -*-
# ====================================================================
# Masala nomi    : A. Word
# Masala havolasi: https://codeforces.com/problemset/problem/59/A
# Vaqt cheklovi  : time limit per test 2 seconds
# Xotira cheklovi: memory limit per test 256 megabytes
# ====================================================================


word = input()
u = 0
l = 0
for i in word:
    if i == i.upper():
        u += 1
    else:
        l += 1
if u > l:
    print(word.upper())
elif l > u:
    print(word.lower())
else:
    print(word.lower())
