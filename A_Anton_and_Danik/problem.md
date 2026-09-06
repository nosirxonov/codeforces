# A. Anton and Danik

- **Manba:** https://codeforces.com/problemset/problem/734/A
- **Vaqt cheklovi:** time limit per test 1 second
- **Xotira cheklovi:** memory limit per test 256 megabytes

## O'zbekcha tarjima

### Masala sharti
Anton shaxmat o'ynashni yaxshi ko'radi, uning do'sti Danik ham. Bir marta ular ketma-ket n ta o'yin o'ynashgan. Har bir o'yinda kim g'olib bo'lgani ma'lum - Anton yoki Danik. Birorta o‘yin durang bilan yakunlanmadi. Endi Anton hayron, kim ko'proq o'yinda g'alaba qozonadi, u yoki Danik? Unga buni aniqlashga yordam bering.

### Kirish ma'lumotlari (Input)
Kirishning birinchi qatorida bitta butun son n ( 1 ≤ n ≤ 100 000 ) — oʻynalgan oʻyinlar soni mavjud. Ikkinchi qatorda n ta katta inglizcha "A" va "D" harflaridan iborat s qatori mavjud - har bir o'yin natijasi. Satrning i-belgisi, agar Anton i-o‘yinda g‘alaba qozongan bo‘lsa, “A” ga, i-o‘yinda Danik g‘alaba qozongan bo‘lsa, “D” ga teng.

### Chiqish ma'lumotlari (Output)
Agar Anton Danikdan ko'proq g'alaba qozongan bo'lsa, chiqishning yagona qatoriga "Anton" (tirnoqsiz) yozing. Agar Danik Antonga qaraganda ko'proq o'yinda g'alaba qozongan bo'lsa, chiqishning yagona qatoriga "Danik" (tirnoqsiz) yozing. Agar Anton va Danik bir xil miqdordagi o'yinlarda g'alaba qozongan bo'lsa, "Do'stlik" ni chop eting (tirnoqsiz).

### Izoh (Note)
Birinchi misolda Anton 6 o'yinda g'alaba qozongan, Danik esa atigi 1 ta o'yinda g'alaba qozongan. Demak, javob "Anton". Ikkinchi misolda Anton 3 o'yinda g'alaba qozondi va Danik 4 o'yinda g'alaba qozondi, shuning uchun javob "Danik". Uchinchi misolda Anton ham, Danik ham 3 ta o'yinda g'alaba qozonishdi va javob "Do'stlik".

## Namunaviy testlar (Sample Tests)

### Test 1
**Input:**
```text
6
ADAAAA
```
**Output:**
```text
Anton
```

### Test 2
**Input:**
```text
7
DDDAADA
```
**Output:**
```text
Danik
```

### Test 3
**Input:**
```text
6
DADADA
```
**Output:**
```text
Friendship
```
