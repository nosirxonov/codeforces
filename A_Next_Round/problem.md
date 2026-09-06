# A. Next Round

- **Manba:** https://codeforces.com/problemset/problem/158/A
- **Vaqt cheklovi:** time limit per test 3 seconds
- **Xotira cheklovi:** memory limit per test 256 megabytes

## O'zbekcha tarjima

### Masala sharti
“K-o‘rin egasining balliga teng yoki undan ko‘p ball to‘plagan ishtirokchi keyingi bosqichga o‘tadi, agar ishtirokchi ijobiy ball to‘plagan bo‘lsa...” — tanlov qoidalaridan ko‘chirma. Tanlovda jami n ta ishtirokchi qatnashdi ( n ≥ k ) va siz ularning ballarini allaqachon bilasiz. Qancha ishtirokchi keyingi bosqichga o'tishini hisoblang.

### Kirish ma'lumotlari (Input)
Kirishning birinchi qatori bitta boʻshliq bilan ajratilgan ikkita n va k ( 1 ≤ k ≤ n ≤ 50 ) butun sonlarini oʻz ichiga oladi. Ikkinchi qatorda boʻsh joydan ajratilgan n ta a 1 , a 2 , ..., a n ( 0 ≤ a i ≤ 100 ) sonlar mavjud, bu yerda a i i – oʻrinni olgan ishtirokchi toʻplagan balldir. Berilgan ketma-ketlik o'smaydi (ya'ni 1 dan n - 1 gacha bo'lgan barcha i uchun quyidagi shart bajariladi: a i ≥ a i + 1 ).

### Chiqish ma'lumotlari (Output)
Keyingi bosqichga o'tgan ishtirokchilar sonini chiqaring.

### Izoh (Note)
Birinchi misolda 5-o'rinni egallagan ishtirokchi 7 ball to'pladi. 6-o‘rindagi ishtirokchi ham 7 ochko jamg‘argani bois, 6 nafar o‘rin egalladi. Ikkinchi misolda hech kim ijobiy ball olmadi.

## Namunaviy testlar (Sample Tests)

### Test 1
**Input:**
```text
8 5
10 9 8 7 7 7 5 5
```
**Output:**
```text
6
```

### Test 2
**Input:**
```text
4 2
0 0 0 0
```
**Output:**
```text
0
```
