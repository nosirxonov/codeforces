# A. Bear and Big Brother

- **Manba:** https://codeforces.com/problemset/problem/791/A
- **Vaqt cheklovi:** time limit per test 1 second
- **Xotira cheklovi:** memory limit per test 256 megabytes

## O'zbekcha tarjima

### Masala sharti
Limak ayiqlarning eng kattasi bo'lishni yoki hech bo'lmaganda ukasi Bobdan kattaroq bo'lishni xohlaydi. Hozirda Limak va Bobning vazni a va b. Limakning vazni akasining vaznidan kichikroq yoki unga teng ekanligi kafolatlangan. Limak juda ko'p ovqatlanadi va uning vazni har yili uch barobar, Bobning vazni esa har yili ikki baravar ko'payadi. To'liq necha yildan keyin Limak Bobdan qat'iy kattaroq (qat'iy og'irroq) bo'ladi?

### Kirish ma'lumotlari (Input)
Kirishning yagona qatorida ikkita butun a va b ( 1 ≤ a ≤ b ≤ 10 )  — mos ravishda Limakning vazni va Bobning vazni mavjud.

### Chiqish ma'lumotlari (Output)
Limak Bobdan qat'iy kattaroq bo'ladigan yillar sonini bildiruvchi bitta butun sonni chop eting.

### Izoh (Note)
Birinchi namunada Limakning vazni 4, Bob esa 7 ta vaznga ega. Bir yildan so'ng ularning vazni mos ravishda 4·3 = 12 va 7·2 = 14 ni tashkil qiladi (bir og'irlik uch barobar, ikkinchisi esa ikki barobar). Limak hali Bobdan katta emas. Ikkinchi yildan keyin og'irliklar 36 va 28 ni tashkil qiladi, shuning uchun birinchi vazn ikkinchisidan kattaroqdir. Limak ikki yildan keyin Bobdan kattaroq bo'ldi, shuning uchun siz 2 ni chop etishingiz kerak. Ikkinchi misolda, Limak va Bobning keyingi yillardagi vaznlari: 12 va 18 , keyin 36 va 36 , va nihoyat 108 va 72 (uch yildan keyin). Javob 3. Esingizda bo'lsin, Limak Bobdan kattaroq bo'lishni xohlaydi va u teng vazn bilan qoniqmaydi. Uchinchi namunada Limak birinchi yildan keyin Bobdan kattaroq bo'ladi. Keyin ularning vazni 3 va 2 bo'ladi.

## Namunaviy testlar (Sample Tests)

### Test 1
**Input:**
```text
4 7
```
**Output:**
```text
2
```

### Test 2
**Input:**
```text
4 9
```
**Output:**
```text
3
```

### Test 3
**Input:**
```text
1 1
```
**Output:**
```text
1
```
