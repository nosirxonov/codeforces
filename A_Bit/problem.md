# A. Bit++

- **Manba:** https://codeforces.com/problemset/problem/282/A
- **Vaqt cheklovi:** time limit per test 1 second
- **Xotira cheklovi:** memory limit per test 256 megabytes

## O'zbekcha tarjima

### Masala sharti
Bitlandning klassik dasturlash tili - Bit++. Bu til juda o'ziga xos va murakkab. Til shu qadar o'ziga xoski, u x deb nomlangan bitta o'zgaruvchiga ega. Bundan tashqari, ikkita operatsiya mavjud: Bit++ tilidagi bayonot ketma-ketlik bo'lib, aynan bitta amal va bitta x o'zgaruvchidan iborat. Bayonot bo'sh joysiz yoziladi, ya'ni u faqat " + ", " - ", " X ​​" belgilaridan iborat bo'lishi mumkin. Bayonotni bajarish uning tarkibidagi amalni qo'llash demakdir. Bit++ dagi dastur - bu buyruqlar ketma-ketligi, ularning har biri bajarilishi kerak. Dasturni bajarish deganda uning tarkibidagi barcha operatorlarni bajarish tushuniladi. Sizga Bit++ tilida dastur beriladi. x ning boshlang'ich qiymati 0 ga teng. Dasturni bajaring va uning yakuniy qiymatini toping (bu dastur bajarilgandagi o'zgaruvchining qiymati).

### Kirish ma'lumotlari (Input)
Birinchi qatorda bitta butun son n (1 ≤ n ≤ 150) - dasturdagi bayonotlar soni mavjud. Keyingi n satrda har bir bayonot mavjud. Har bir bayonotda aynan bitta operatsiya ( ++ yoki -- ) va aynan bitta x o'zgaruvchisi (« X » harfi bilan belgilanadi). Shunday qilib, bo'sh bayonotlar yo'q. Amaliyot va o'zgaruvchi istalgan tartibda yozilishi mumkin.

### Chiqish ma'lumotlari (Output)
Bitta butun sonni chop eting - x ning yakuniy qiymati.

## Namunaviy testlar (Sample Tests)

### Test 1
**Input:**
```text
1
++X
```
**Output:**
```text
1
```

### Test 2
**Input:**
```text
2
X++
--X
```
**Output:**
```text
0
```
