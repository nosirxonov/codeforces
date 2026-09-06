# A. Nearly Lucky Number

- **Manba:** https://codeforces.com/problemset/problem/110/A
- **Vaqt cheklovi:** time limit per test 2 seconds
- **Xotira cheklovi:** memory limit per test 256 megabytes

## O'zbekcha tarjima

### Masala sharti
Petya omadli raqamlarni yaxshi ko'radi. Biz hammamiz bilamizki, omadli sonlar musbat butun sonlar bo'lib, ularning o'nli ko'rinishlarida faqat 4 va 7 baxtli raqamlari mavjud. Masalan, 47 , 744 , 4 raqamlari omadli, 5 , 17 , 467 raqamlari esa omadli emas. Afsuski, barcha raqamlar omadli emas. Petya raqamni deyarli omadli deb ataydi, agar undagi omadli raqamlar soni baxtli raqam bo'lsa. U n soni deyarli omadli raqammi, deb hayron bo'ladi.

### Kirish ma'lumotlari (Input)
Yagona qatorda n ( 1 ≤ n ≤ 10 18 ) butun son mavjud. S++ da 64-bitli raqamlarni oʻqish yoki yozish uchun %lld spetsifikatsiyasidan foydalanmang. Cin, cout oqimlari yoki %I64d spetsifikatsiyasidan foydalanish afzalroqdir.

### Chiqish ma'lumotlari (Output)
Agar n deyarli omadli raqam bo'lsa, "HA" deb bitta qatorga chop eting. Aks holda, "YO'Q" (tirnoqsiz) chop eting.

### Izoh (Note)
Birinchi namunada 3 ta omadli raqam mavjud (birinchi va oxirgi ikkita), shuning uchun javob "YO'Q". Ikkinchi namunada 7 ta omadli raqam bor, 7 omadli raqam, shuning uchun javob "HA". Uchinchi misolda omadli raqamlar yo'q, shuning uchun javob "YO'Q".

## Namunaviy testlar (Sample Tests)

### Test 1
**Input:**
```text
40047
```
**Output:**
```text
NO
```

### Test 2
**Input:**
```text
7747774
```
**Output:**
```text
YES
```

### Test 3
**Input:**
```text
1000000000000000000
```
**Output:**
```text
NO
```
