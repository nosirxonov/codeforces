# A. Wrong Subtraction

- **Manba:** https://codeforces.com/problemset/problem/977/A
- **Vaqt cheklovi:** time limit per test 1 second
- **Xotira cheklovi:** memory limit per test 256 megabytes

## O'zbekcha tarjima

### Masala sharti
Kichkina qiz Tanya raqamni bittaga kamaytirishni o'rganmoqda, lekin u ikki yoki undan ortiq raqamdan iborat bo'lgan raqamni noto'g'ri qiladi. Tanya quyidagi algoritm bo'yicha raqamdan bittani ayiradi: Sizga $$$n$$$ butun son berilgan. Tanya undan $$$k$$$ marta bittasini ayiradi. Sizning vazifangiz barcha $$$k$$$ ayirishlardan keyin natijani chop etishdir. Natija ijobiy butun son bo'lishi kafolatlanadi.

### Kirish ma'lumotlari (Input)
Kirishning birinchi qatorida ikkita butun son $$$n$$$ va $$$k$$$ ($$$2 \le n \le 10^9$$$, $$$1 \le k \le 50$$$) mavjud — Tanya olib tashlaydigan raqam va mos ravishda ayirishlar soni.

### Chiqish ma'lumotlari (Output)
Bitta butun sonni chop eting — $$$n$$$ ning bir $$$k$$$ marta kamayishi natijasi. Natija ijobiy butun son bo'lishi kafolatlanadi.

### Izoh (Note)
Birinchi misol quyidagi ketma-ketlikka mos keladi: $$$512 \rightarrow 511 \rightarrow 510 \rightarrow 51 \rightarrow 50$$$.

## Namunaviy testlar (Sample Tests)

### Test 1
**Input:**
```text
512 4
```
**Output:**
```text
50
```

### Test 2
**Input:**
```text
1000000000 9
```
**Output:**
```text
1
```
