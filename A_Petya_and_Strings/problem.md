# A. Petya and Strings

- **Manba:** https://codeforces.com/problemset/problem/112/A
- **Vaqt cheklovi:** time limit per test 2 seconds
- **Xotira cheklovi:** memory limit per test 256 megabytes

## O'zbekcha tarjima

### Masala sharti
Kichkina Petya sovg'alarni yaxshi ko'radi. Onasi tug'ilgan kuni uchun bir xil o'lchamdagi ikkita ip sotib oldi. Satrlar katta va kichik lotin harflaridan iborat. Endi Petya bu ikki qatorni leksikografik jihatdan solishtirmoqchi. Harflarning holati muhim emas, ya'ni katta harf tegishli kichik harfga ekvivalent hisoblanadi. Petyaga solishtirishga yordam bering.

### Kirish ma'lumotlari (Input)
Birinchi ikkita satrning har birida sotib olingan satr mavjud. Satrlarning uzunligi 1 dan 100 gacha. Satrlar bir xil uzunlikda, shuningdek, katta va kichik lotin harflaridan iborat bo'lishi kafolatlanadi.

### Chiqish ma'lumotlari (Output)
Agar birinchi satr ikkinchisidan kichik bo'lsa, "-1" ni chop eting. Agar ikkinchi satr birinchisidan kichik bo'lsa, "1" ni chop eting. Agar satrlar teng bo'lsa, "0" ni chop eting. E'tibor bering, satrlarni taqqoslashda harflarning holati hisobga olinmaydi.

### Izoh (Note)
Agar leksikografik tartib (shuningdek, "lug'at tartibi" yoki "alifbo tartibi" sifatida ham tanilgan) haqida ko'proq rasmiy ma'lumot olishni istasangiz, quyidagi saytga tashrif buyurishingiz mumkin:

## Namunaviy testlar (Sample Tests)

### Test 1
**Input:**
```text
aaaa
aaaA
```
**Output:**
```text
0
```

### Test 2
**Input:**
```text
abs
Abz
```
**Output:**
```text
-1
```

### Test 3
**Input:**
```text
abcdefg
AbCdEfF
```
**Output:**
```text
1
```
