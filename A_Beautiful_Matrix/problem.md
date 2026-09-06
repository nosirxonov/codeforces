# A. Beautiful Matrix

- **Manba:** https://codeforces.com/problemset/problem/263/A
- **Vaqt cheklovi:** time limit per test 2 seconds
- **Xotira cheklovi:** memory limit per test 256 megabytes

## O'zbekcha tarjima

### Masala sharti
Sizda 24 ta nol va bitta bitta raqamdan iborat 5 × 5 matritsa bor. Matritsa satrlarini 1 dan 5 gacha raqamlar bo'yicha yuqoridan pastga indekslaymiz, matritsa ustunlarini chapdan o'ngga 1 dan 5 gacha raqamlar bilan indekslaymiz. Bitta harakatda siz matritsaga quyidagi ikkita o'zgartirishdan birini qo'llashingiz mumkin: Agar matritsaning bitta raqami uning o'rtasida joylashgan bo'lsa (uchinchi qator va uchinchi ustunning kesishmasida joylashgan katakda) matritsa chiroyli ko'rinadi deb o'ylaysiz. Matritsani chiroyli qilish uchun zarur bo'lgan minimal harakatlar sonini hisoblang.

### Kirish ma'lumotlari (Input)
Kiritish besh satrdan iborat bo'lib, har bir satr beshta butun sonni o'z ichiga oladi: kirishning i - qatoridagi j -chi butun son matritsaning i - qator va j - ustun kesishmasida joylashgan elementini ifodalaydi. Matritsa 24 ta nol va bitta bitta raqamdan iborat ekanligi kafolatlangan.

### Chiqish ma'lumotlari (Output)
Bitta butun sonni chop eting - matritsani chiroyli qilish uchun zarur bo'lgan minimal harakatlar soni.

## Namunaviy testlar (Sample Tests)

### Test 1
**Input:**
```text
0 0 0 0 0
0 0 0 0 1
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
```
**Output:**
```text
3
```

### Test 2
**Input:**
```text
0 0 0 0 0
0 0 0 0 0
0 1 0 0 0
0 0 0 0 0
0 0 0 0 0
```
**Output:**
```text
1
```
