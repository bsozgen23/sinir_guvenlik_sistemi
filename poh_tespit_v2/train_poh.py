from ultralytics import YOLO
import os

def main():
    print('PÖH Tespit Sistemi Eğitimine Başlanıyor...')
    
    # 1. Ön eğitilmiş Large modeli yükle (Eğer yoksa internetten indirir)
    model = YOLO('yolov8l.pt') 

    # 2. Üst Düzey Optimizasyonlarla Eğitimi Başlat
    # Veri setinin yolu data.yaml içinde belirtilmiştir.
    # Scriptin çalıştığı yer neresi olursa olsun doğru yaml yolunu bulmak için mutlak yol kullanalım:
    dataset_yaml = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'dataset', 'data.yaml')
    
    results = model.train(
        data=dataset_yaml,
        epochs=300,
        imgsz=1024,             # Yüksek donanım (RTX 4500 vs) için yüksek çözünürlük
        batch=16,               # VRAM durumuna göre bunu 8, 16 veya 32 yapabilirsiniz
        optimizer='AdamW',      # En iyi ağırlık güncelleyici
        cos_lr=True,            # Cosine learning rate
        lr0=0.001,              # Başlangıç öğrenme hızı
        patience=50,            # 50 epoch boyunca gelişim olmazsa eğitimi kes
        project='poh_tespit',
        name='optimizasyonlu_egitim',
        
        # Veri Artırma (Augmentation) Ayarları - Ezberlemeyi önler
        mosaic=1.0,             
        mixup=0.2,
        hsv_h=0.015, 
        hsv_s=0.7, 
        hsv_v=0.4,
        
        # Eğer GPU'nuz varsa device=0 kullanır, yoksa otomatik seçer
        device=0 
    )
    
    print('Eğitim Başarıyla Tamamlandı!')
    
if __name__ == '__main__':
    main()
