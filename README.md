# 📦 PDF Compressor (10MB Limit)

Python ile geliştirilen bu program, PDF dosyalarını **görsel kaliteyi bozmadan** sıkıştırır ve dosya boyutunu **10 MB altına** düşürmeyi hedefler.
  
✅ EXE dosyasına dönüştürülebilir  
✅ Kullanıcı dostu pencere bildirimleri  
✅ Python ile geliştirildi

---

## 📥 EXE DOSYASINI İNDİR

🖥 Programın çalışır `.exe` versiyonunu aşağıdan indirebilirsin:

🔗 **[📥 EXE'yi İndir](https://drive.google.com/uc?id=1nYboyQu0Xb4iOB5LJg2g6tNjjF8rKZFI&export=download)**

> 📌 Not: Dosyayı indirdikten sonra EXE’yi çalıştırıp PDF dosyasını seçin.  
> Program otomatik olarak çıktı üretir.  
> ⚠ Programın çalışması için dosya içeriğini değiştirmeyin.

---

## 🧪 KULLANIM

### 💻 Python Dosyası Olarak

python pdf_compressor.py

Terminalde çalıştırıldığında dosya seçme penceresi açılır.



### 🖥 EXE Olarak
pdf_compressor.exe dosyasını çift tıkla

### 📁 Sıkıştırılmış dosya aynı klasöre şu şekilde kaydedilir:
ornekdosya.pdf → ornekdosya_compressed.pdf

### ⚙ KURULUM
Gerekli kütüphaneyi kurmak için:

pip install pikepdf

### 🔧 EXE OLUŞTURMA (Geliştiriciler İçin)
pip install pyinstaller

pyinstaller --onefile --noconsole pdf_compressor.py

➡ EXE çıktısı şu klasöre oluşur: dist/pdf_compressor.exe


### 📁 GİRDİ & ÇIKTI
Tür	Açıklama

Girdi	PDF dosyası (ör: belge.pdf)

Çıktı	Sıkıştırılmış PDF (belge_compressed.pdf)

### 💡 EKSTRA BİLGİ
Program, pikepdf kütüphanesi ile gereksiz objeleri ve meta verileri temizleyerek dosyayı optimize eder.

Görsel kaliteyi bozmadan sıkıştırma sağlar.

EXE versiyonu tkinter kütüphanesi ile pencere üzerinden kullanıcıya bilgi verir.

### 👨‍💻 Geliştirici
Enes Furkan Özdemir – 2025
📧 [GitHub Profilim](https://github.com/EnesFurkanOzdemir)

### 📜 Lisans
MIT License

Copyright (c) 2025 Enes Furkan Özdemir

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.