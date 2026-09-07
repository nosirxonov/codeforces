# -*- coding: utf-8 -*-
# ====================================================================
# Masala nomi    : A. Football
# Masala havolasi: https://codeforces.com/problemset/problem/96/A
# Vaqt cheklovi  : time limit per test 2 seconds
# Xotira cheklovi: memory limit per test 256 megabytes
# ====================================================================


n = input()

if "0000000" in n or "1111111" in n:
    print("YES")
else:
    print("NO")
