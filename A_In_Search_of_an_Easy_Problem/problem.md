# A. In Search of an Easy Problem

- **Manba:** https://codeforces.com/problemset/problem/1030/A
- **Vaqt cheklovi:** time limit per test 1 second
- **Xotira cheklovi:** memory limit per test 256 megabytes

## O'zbekcha tarjima

### Masala sharti
Turnirga tayyorgarlik ko'rayotganda, Codeforces koordinatorlari birinchi muammoni iloji boricha osonlashtirishga harakat qilishadi. Bu safar koordinator ba'zi muammoni tanladi va $$$n$$$ odamlardan ularning fikrlarini so'radi. Har bir inson bu muammoni oson yoki qiyin deb javob berdi. Agar ushbu $$$n$$$ odamlardan kamida bittasi muammo qiyin deb javob bergan bo'lsa, koordinator muammoni o'zgartirishga qaror qiladi. Berilgan javoblar uchun muammo etarlicha oson yoki yo'qligini tekshiring.

### Kirish ma'lumotlari (Input)
Birinchi qatorda bitta butun son $$$n$$$ ($$$1 \le n \le 100$$$) mavjud — oʻz fikrlarini bildirish soʻralgan odamlar soni. Ikkinchi qatorda $$$n$$$ butun sonlar mavjud, har bir butun son $$$0$$$ yoki $$$1$$$. Agar $$$i$$$-inchi butun son $$$0$$$ bo'lsa, $$$i$$$-chi odam muammoni oson deb hisoblaydi; agar $$$1$$$ bo'lsa, $$$i$$$-chi odam muammoni qiyin deb hisoblaydi.

### Chiqish ma'lumotlari (Output)
Bitta so'zni chop eting: agar muammo barcha javoblarga ko'ra oson bo'lsa, "OSON" yoki muammoni qiyin deb hisoblaydigan kamida bitta odam bo'lsa, "QIYIN". Siz istalgan registrdagi har bir harfni chop etishingiz mumkin: "EASY", "olay", "EaSY" va "eAsY" hammasi to'g'ri qayta ishlanadi.

### Izoh (Note)
Birinchi misolda uchinchi shaxs bu qiyin muammo ekanligini aytadi, shuning uchun uni almashtirish kerak. Ikkinchi misolda muammo yagona odam uchun oson, shuning uchun uni almashtirish shart emas.

## Namunaviy testlar (Sample Tests)

### Test 1
**Input:**
```text
3
0 0 1
```
**Output:**
```text
HARD
```

### Test 2
**Input:**
```text
1
0
```
**Output:**
```text
EASY
```
