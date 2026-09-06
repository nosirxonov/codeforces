# A. Stones on the Table

- **Manba:** https://codeforces.com/problemset/problem/266/A
- **Vaqt cheklovi:** time limit per test 2 seconds
- **Xotira cheklovi:** memory limit per test 256 megabytes

## O'zbekcha tarjima

### Masala sharti
Stolda ketma-ket n ta tosh bor, ularning har biri qizil, yashil yoki ko'k bo'lishi mumkin. Har qanday ikkita qo'shni tosh turli xil ranglarga ega bo'lishi uchun stoldan olinadigan minimal tosh sonini hisoblang. Agar ular orasida boshqa toshlar bo'lmasa, ketma-ket toshlar qo'shni hisoblanadi.

### Kirish ma'lumotlari (Input)
Birinchi qatorda butun son n (1 ≤ n ≤ 50) - stol ustidagi toshlar soni mavjud. Keyingi qatorda toshlarning ranglarini ifodalovchi s string mavjud. Biz chapdan o'ngga 1 dan n gacha raqamlangan qatordagi toshlarni ko'rib chiqamiz. Keyin i -chi belgi " R " ga teng bo'ladi, agar i - tosh qizil bo'lsa, " G ", agar u yashil bo'lsa va " B ", agar u ko'k bo'lsa.

### Chiqish ma'lumotlari (Output)
Bitta butun sonni chop eting - muammoning javobi.

## Namunaviy testlar (Sample Tests)

### Test 1
**Input:**
```text
3
RRG
```
**Output:**
```text
1
```

### Test 2
**Input:**
```text
5
RRRRR
```
**Output:**
```text
4
```

### Test 3
**Input:**
```text
4
BRBG
```
**Output:**
```text
0
```
