# A. Tram

- **Manba:** https://codeforces.com/problemset/problem/116/A
- **Vaqt cheklovi:** time limit per test 2 seconds
- **Xotira cheklovi:** memory limit per test 256 megabytes

## O'zbekcha tarjima

### Masala sharti
Lineer Kingdom aynan bitta tramvay liniyasiga ega. U tramvay harakati tartibida 1 dan n gacha raqamlangan n ta bekatga ega. I - bekatda a i yo'lovchilar tramvaydan chiqishadi, b i yo'lovchilar esa unga kirishadi. Tramvay birinchi bekatga yetguncha bo‘sh. Bundan tashqari, tramvay oxirgi bekatga kelganda, barcha yo'lovchilar bo'sh bo'lishi uchun chiqib ketishadi. Sizning vazifangiz tramvayning minimal sig'imini hisoblashdir, shunda tramvay ichidagi odamlar soni istalgan vaqtda bu sig'imdan oshmaydi. E'tibor bering, har bir bekatda barcha chiquvchi yo'lovchilar tramvayga kirishdan oldin chiqib ketishadi.

### Kirish ma'lumotlari (Input)
Birinchi qatorda bitta raqam n ( 2 ≤ n ≤ 1000 ) - tramvay bekatlari soni mavjud. Keyin n qator keladi, har birida ikkita tamsayı a i va b i (0 ≤ a i, b i ≤ 1000) mavjud — i - bekatda tramvaydan chiqqan yo'lovchilar soni va i - bekatda tramvayga kirgan yo'lovchilar soni. To'xtash joylari tramvayning harakatlanish tartibida birinchi to'xtash joyidan oxirgi bekatgacha beriladi.

### Chiqish ma'lumotlari (Output)
Tramvayning mumkin bo'lgan minimal sig'imini bildiruvchi bitta butun sonni chop eting (0 ruxsat berilgan).

### Izoh (Note)
Birinchi misol uchun 6 ta sig'im etarli: Tramvay ichidagi yo'lovchilar soni hech qachon 6 dan oshmaganligi sababli, 6 ta sig'im etarli. Bundan tashqari, tramvayning sig'imi 6 dan kam bo'lishi mumkin emas. Demak, 6 to'g'ri javob.

## Namunaviy testlar (Sample Tests)

### Test 1
**Input:**
```text
4
0 3
2 5
4 2
4 0
```
**Output:**
```text
6
```
