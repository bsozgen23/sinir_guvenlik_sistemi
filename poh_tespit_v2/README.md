# PÖH Tespit Sistemi v2 (Optimizasyonlu YOLO Eğitim Ortamı)

Bu klasör, Polis Özel Harekat (PÖH) tespiti için tamamen optimize edilmiş eğitim, test ve çıkarım (inference) betiklerini barındırır. Eski projeyle karışmaması için ayrı bir klasör (poh_tespit_v2) olarak tasarlanmıştır.

## İçerik
- dataset/: 1301 görselden oluşan, data leakage (veri sızıntısı) engellenerek Train/Val/Test olarak bölünmüş, %100 temiz ve arkaplan görsellerini barındıran asıl YOLO veri setiniz.
- 	rain_poh.py: Modeli AdamW, Cosine Annealing, Hyperparameter ayarlarıyla ve 1024 çözünürlükle eğiten betik (Nvidia RTX 4500 & i9 gibi güçlü sistemler için ayarlanmıştır).
- 	est_poh.py: Eğitim bitince test veri seti (hiç görülmemiş 41 görsel) üzerinden modelin başarısını % (yüzde) cinsinden ekrana basan betik.
- inference_poh.py: Yeni fotoğrafları/videoları verip modeli deneyeceğiniz betik. Kutuları çizerek klasöre kaydeder.

## Nasıl Kullanılır? (Diğer Güçlü Bilgisayarda)

1. Bu depoyu o bilgisayara indirin (git clone).
2. Gerekli kütüphaneleri kurun: pip install ultralytics
3. Eğitimi başlatın:
   `ash
   python train_poh.py
   `
4. Eğitim (300 epoch) bitince test başarısını % olarak görmek için:
   `ash
   python test_poh.py
   `
5. Kendi fotoğraflarınızda denemek için fotoğrafları deneme_gorselleri klasörüne atın ve çalıştırın:
   `ash
   python inference_poh.py
   `
   Çizilmiş fotoğraflar poh_tespit_ciktilar/tespit_edilenler klasöründe oluşacaktır.
