# -*- coding: utf-8 -*-
# ====================================================================
# Masala nomi    : A. Word Capitalization
# Masala havolasi: https://codeforces.com/problemset/problem/281/A
# Vaqt cheklovi  : time limit per test 2 seconds
# Xotira cheklovi: memory limit per test 256 megabytes
# ====================================================================


word = input()
l = []
for i in word:
    l.append(i)
l[0] = l[0].upper()
print("".join(l))
