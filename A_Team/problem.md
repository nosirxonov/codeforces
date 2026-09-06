# A. Team

- **Manba:** https://codeforces.com/problemset/problem/231/A
- **Vaqt cheklovi:** time limit per test 2 seconds
- **Xotira cheklovi:** memory limit per test 256 megabytes

## O'zbekcha tarjima

### Masala sharti
Bir kuni Petya, Vasya va Tonya uchta eng yaxshi do'stlar bir jamoa tuzishga va dasturlash tanlovlarida qatnashishga qaror qilishdi. Ishtirokchilarga odatda dasturlash musobaqalarida bir nechta muammolar taklif qilinadi. Boshlanishdan ancha oldin do'stlar muammoni hal qilishga qaror qilishdi, agar ulardan kamida ikkitasi yechimga ishonch hosil qilsa. Aks holda, do'stlar muammoning echimini yozmaydi. Ushbu tanlov ishtirokchilarga n ta muammolarni taklif qiladi. Har bir muammo uchun biz bilamiz, qaysi do'st yechimiga ishonch hosil qiladi. Do'stlarga yechimini yozadigan muammolar sonini topishga yordam bering.

### Kirish ma'lumotlari (Input)
Birinchi kiritish qatorida bitta butun son n ( 1 ≤ n ≤ 1000 ) mavjud - tanlovdagi muammolar soni. Keyin n qatorda har birida uchta butun son mavjud, har bir butun son 0 yoki 1 ga teng. Agar qatordagi birinchi raqam 1 ga teng bo'lsa, Petya muammoning echimiga ishonch hosil qiladi, aks holda u ishonch hosil qilmaydi. Ikkinchi raqam Vasyaning yechimga qarashini, uchinchi raqam Tonyaning nuqtai nazarini ko'rsatadi. Chiziqlardagi raqamlar bo'shliqlar bilan ajratilgan.

### Chiqish ma'lumotlari (Output)
Bitta butun sonni chop eting - do'stlar tanlovda bajaradigan muammolar soni.

### Izoh (Note)
Birinchi misolda Petya va Vasya birinchi masalani qanday hal qilishni bilishlariga va ularning uchtasi ikkinchi masalani qanday hal qilishni bilishlariga aminlar. Bu ular ushbu muammolar uchun echimlar yozishlarini anglatadi. Faqat Petya uchinchi muammoning yechimiga ishonch hosil qiladi, lekin bu etarli emas, shuning uchun do'stlar buni qabul qilmaydi. Ikkinchi misolda do'stlar faqat ikkinchi muammoni hal qilishadi, chunki Vasya va Tonya yechimga ishonch hosil qilishadi.

## Namunaviy testlar (Sample Tests)

### Test 1
**Input:**
```text
3
1 1 0
1 1 1
1 0 0
```
**Output:**
```text
2
```

### Test 2
**Input:**
```text
2
1 0 0
0 1 1
```
**Output:**
```text
1
```
