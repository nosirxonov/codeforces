# -*- coding: utf-8 -*-
# ====================================================================
# Masala nomi    : A. Next Round
# Masala havolasi: https://codeforces.com/problemset/problem/158/A
# Vaqt cheklovi  : time limit per test 3 seconds
# Xotira cheklovi: memory limit per test 256 megabytes
# ====================================================================


n, k = map(int, input().split())
a = list(map(int, input().split()))
 
limit = a[k - 1]  # k-chi o‘rindagi ishtirokchining balli
count = 0
 
for score in a:
    if score >= limit and score > 0:
        count += 1
 
print(count)
