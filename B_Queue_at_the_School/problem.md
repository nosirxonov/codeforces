# B. Queue at the School

- **Manba:** https://codeforces.com/problemset/problem/266/B
- **Vaqt cheklovi:** time limit per test 2 seconds
- **Xotira cheklovi:** memory limit per test 256 megabytes

## O'zbekcha tarjima

### Masala sharti
Tanaffus vaqtida maktab o‘quvchilari, o‘g‘il-qizlar oshxonada n kishidan iborat navbat hosil qilishdi. Dastlab bolalar oshxonaga kirish tartibida turishdi. Biroq, bir muncha vaqt o'tgach, yigitlar navbatda turgan qizlarning oldida turishlarini o'zlarini noqulay his qilishdi va ular har soniyada qizlarni oldinga siljitishga ruxsat berishdi. Keling, jarayonni aniqroq tasvirlab beraylik. Aytaylik, navbatdagi pozitsiyalar 1 dan n gacha butun sonlar bilan ketma-ket raqamlangan, bunda birinchi navbatda 1-pozitsiyadagi odam xizmat qiladi. Keyin, agar x vaqtida o'g'il bola i - o'rinda, qiz bola ( i + 1) - o'rinda tursa, x + 1 vaqtida i - o'rinda qiz, ( i + 1) - o'g'il bola bo'ladi. Vaqt soniyalarda ko'rsatilgan. Siz bolalarning boshlang'ich pozitsiyasini oldingiz. t soniyadan keyin navbat qanday ko'rinishini aniqlang.

### Kirish ma'lumotlari (Input)
Birinchi qatorda ikkita tamsayı n va t (1 ≤ n , t ≤ 50) mavjud boʻlib, ular navbatdagi bolalar sonini va keyin siz topishingiz kerak boʻlgan tartibga oʻtish vaqtini bildiradi. Keyingi qatorda maktab o'quvchilarining dastlabki tartibini ifodalovchi s satri mavjud. Agar navbatdagi i - o'rinda o'g'il bola bo'lsa, s qatorning i - belgisi " B " ga teng, aks holda i - belgisi " G " ga teng.

### Chiqish ma'lumotlari (Output)
Chop etish satri a , u t soniyadan keyin tartibni tavsiflaydi. Agar kerakli vaqtdan keyin i-pog'onada o'g'il bo'lsa, u holda i-chi a belgisi "B" ga, aks holda "G" ga teng bo'lishi kerak.

## Namunaviy testlar (Sample Tests)

### Test 1
**Input:**
```text
5 1
BGGBG
```
**Output:**
```text
GBGGB
```

### Test 2
**Input:**
```text
5 2
BGGBG
```
**Output:**
```text
GGBGB
```

### Test 3
**Input:**
```text
4 1
GGGB
```
**Output:**
```text
GGGB
```
