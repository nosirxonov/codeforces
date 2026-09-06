# -*- coding: utf-8 -*-
# ====================================================================
# Masala nomi    : A. Young Physicist
# Masala havolasi: https://codeforces.com/problemset/problem/69/A
# Vaqt cheklovi  : time limit per test 2 seconds
# Xotira cheklovi: memory limit per test 256 megabytes
# ====================================================================


n = int(input())
 
sx = sy = sz = 0
 
for _ in range(n):
    x, y, z = map(int, input().split())
    sx += x
    sy += y
    sz += z
 
if sx == 0 and sy == 0 and sz == 0:
    print("YES")
else:
    print("NO")
