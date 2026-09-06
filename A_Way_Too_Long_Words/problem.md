# A. Way Too Long Words

- **Manba:** https://codeforces.com/problemset/problem/71/A
- **Vaqt cheklovi:** time limit per test 1 second
- **Xotira cheklovi:** memory limit per test 256 megabytes

## O'zbekcha tarjima

### Masala sharti
Ba'zida "mahalliylashtirish" yoki "xalqarolashtirish" kabi ba'zi so'zlar shunchalik uzunki, ularni bir matnda ko'p marta yozish juda charchatadi. Keling, juda uzun so'zni ko'rib chiqaylik, agar uning uzunligi 10 belgidan ortiq bo'lsa. Barcha juda uzun so'zlar maxsus qisqartma bilan almashtirilishi kerak. Bu qisqartma shunday qilingan: biz so'zning birinchi va oxirgi harfini yozamiz va ularning orasiga birinchi va oxirgi harflar orasidagi harflar sonini yozamiz. Bu raqam o'nlik tizimda va hech qanday bosh noldan iborat emas. Shunday qilib, "lokalizatsiya" "l10n", "xalqarolashtirish" esa "i18n" deb yoziladi. Sizga qisqartmalar bilan so'zlarni o'zgartirish jarayonini avtomatlashtirish tavsiya etiladi. Bunda juda uzun so'zlar qisqartma bilan almashtirilishi va juda uzun bo'lmagan so'zlar hech qanday o'zgarishlarga duch kelmasligi kerak.

### Kirish ma'lumotlari (Input)
Birinchi qatorda n ( 1 ≤ n ≤ 100 ) butun son mavjud. Quyidagi n qatorning har biri bitta so‘zdan iborat. Barcha so'zlar kichik lotin harflaridan iborat bo'lib, uzunligi 1 dan 100 tagacha belgidan iborat.

### Chiqish ma'lumotlari (Output)
n qatorni chop eting. i - qatorda kiritilgan ma'lumotlardan i - so'zni almashtirish natijasi bo'lishi kerak.

## Namunaviy testlar (Sample Tests)

### Test 1
**Input:**
```text
4
word
localization
internationalization
pneumonoultramicroscopicsilicovolcanoconiosis
```
**Output:**
```text
word
l10n
i18n
p43s
```
