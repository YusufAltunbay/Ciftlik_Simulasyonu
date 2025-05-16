# 🎮 Oyun Raporu – `oyun.py`

## 👥 Proje Ekibi

- **Ad Soyad 1**: [Kamil AY 22253051]
- **Ad Soyad 2**: [Yusuf ALTUNBAY 22253072]
- **Ad Soyad 3**: [Abdurrahman EKİN 22253078]



---

## 📄 Genel Bilgi

Bu dosya, Python’un `pygame` kütüphanesi kullanılarak geliştirilmiş bir çiftlik temalı 2D oyun uygulamasıdır. Oyunda; bitki yetiştirme, hayvan bakımı, ürün toplama ve satışı gibi temel çiftlik mekanikleri bir araya getirilmiştir.

---

## 🧱 Kullanılan Sınıflar

- **`Player`**
- **`Tile`**
- **`Plant`**
- **`Inventory`**
- **`Menu` (Satın alma, satış)**
- **`Level`, `FarmLevel`**
- **`Transition`, `Overlay`, `Sky`**

---

## 🌀 Ana Oyun Döngüsü

```python
while running:
    for event in pygame.event.get():
        ...
    screen.blit(background, ...)
    draw_farm()
    draw_buildings()
    pygame.display.update()
    clock.tick(60)
```

---

## 🎨 Kullanılan Görseller

Aşağıda projede kullanılan tüm görseller listelenmiştir:

### Ürünler & Tohumlar
- `Wheat_Seeds.png`
- `Corn_Seeds.png`
- `Carrot_Seeds.png`
- `Beet_Seeds.png`
- `Strawberry_Seeds.png`
- `Sunflower_Seeds.png`
- `Wheat_Stage_5.png`
- `Corn_Stage_6.png`
- `Carrot_Stage_4.png`
- `Beet_Stage_5.png`
- `Strawberry_Stage_6.png`
- `Sunflower_Stage_6.png`
- `Milk_TR.png`
- `Egg.png`
- `flour.jpg`
- `Mayonnaise.png`
- `Cheese.png`
- `Oil.png`
- `Sugar.png`
- `Pink_Cake.png`
- `Cookie.png`
- `Ice_cream.png`
- `ayran.webp`

### Arka Plan ve Zemin
- `Flooring_50.png`
- `Flooring_62.png`
- `Flooring_58.png`
- `arka_plan.jpg`
- `yol.png`
- `ahır_iç_son.png`
- `kümes_iç.png`

### Yapılar
- `144px-Deluxe_Barn.png`
- `144px-Coop.png`
- `imalathane2.png`
- `bakkal.png`
- `Araba.png`

### Karakterler ve Hayvanlar
- `adamsag.png`
- `adamsol.png`
- `arkadanbak.png`
- `öndenbakış.png`
- `White_Cow.png`
- `White_Chicken.png`
- `tavuk.png`
- `ağac.png`

---

## 🔊 Kullanılan Ses Dosyaları

- `Chicken Sound Effect.mp3`
- `İnek Sesi.ogg.opus`
- `Satın Alım Satım.mp3`
- `Korna.mp3`
- `Oyun Ana Ekran.mp3`
- `Oyun Müziği.mp3`
- `ekin_toplama.wav`

---

## 🎮 Kullanıcı Etkileşimleri

- **Yön Tuşları / WASD**: Hareket
- **Boşluk / B**: Hayvan etkileşimi (besleme / ürün toplama)
- **Enter**: Yapılarla etkileşim
- **C**: Envanter

---

## 🧩 Oyun Mekanikleri

### Tarım Sistemi
- Tarla sürme, tohum ekme, sulama ve hasat.

### Hayvancılık
- Tavuklardan yumurta, ineklerden süt toplama ve besleme sistemi.

### Market / Satış Sistemi
- Ürün satışı, tohum satın alma.
- Kamyon animasyonu ile satış bildirimi.

### İmalathane
- Ürün işleme (yoğurt, peynir, pasta vb.)
- Gereken malzemeler ve zaman bazlı üretim sistemi.

### Envanter
- Minecraft benzeri slot tabanlı yapı.

---

## ⏳ Zaman ve Animasyonlar

- Sulama sonrası zamanla ürün büyümesi.
- Hayvan beslenmesi sonrası yumurta/süt üretimi.
- Ağaçlar, araçlar ve karakter için animasyonlar.

---

## 💰 Ekonomik Sistem

- Ürün satışıyla gelir elde edilir.
- Gelir ile yeni tohumlar alınabilir.
- İmalathane ürünleri daha yüksek fiyata satılabilir.

---

## ✅ Sonuç

Bu proje, `pygame` kullanılarak geliştirilen kapsamlı bir çiftlik simülasyonudur. Oyuncuya tarım, hayvancılık, ticaret ve üretim gibi birden fazla oyun deneyimi sunmaktadır.

---
