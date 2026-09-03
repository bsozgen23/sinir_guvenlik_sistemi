from ultralytics import YOLO
import os

def main():
    # Eğitilmiş en iyi ağırlığı (best.pt) yükle
    model_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'poh_tespit', 'optimizasyonlu_egitim', 'weights', 'best.pt')
    
    if not os.path.exists(model_path):
        print(f'HATA: Eğitilmiş model bulunamadı -> {model_path}')
        print('Lütfen önce train_poh.py ile eğitimi tamamlayın.')
        return
        
    model = YOLO(model_path)
    
    # Yeni denenecek resimlerin veya videoların olduğu klasör
    # Kullanıcı buraya kendi deneme klasörünün yolunu girebilir. Varsayılan olarak örnek bir klasör arayalım.
    kaynak_klasor = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'deneme_gorselleri')
    
    if not os.path.exists(kaynak_klasor):
        os.makedirs(kaynak_klasor)
        print(f"Uyarı: '{kaynak_klasor}' klasörü yoktu, oluşturuldu.")
        print("Lütfen bu klasörün içine tespit edilmesini istediğiniz yeni fotoğrafları atıp betiği tekrar çalıştırın.")
        return

    print(f"'{kaynak_klasor}' içerisindeki görseller taranıyor...")
    
    # Tahmin yap ve sonuçları kaydet
    results = model.predict(
        source=kaynak_klasor,
        conf=0.60,              # Güven eşiği: Sadece %60 üzeri emin olduklarını PÖH say (Yanlış tespiti keser)
        save=True,              # Sonuç görsellerini kaydet
        project='poh_tespit_ciktilar',
        name='tespit_edilenler', # Bu klasörün içine jpg olarak atılacak
        device=0
    )
    
    print("\nİşlem Tamamlandı!")
    print(f"Çıktı görselleri şu klasöre kaydedildi: poh_tespit_ciktilar/tespit_edilenler")

if __name__ == '__main__':
    main()
