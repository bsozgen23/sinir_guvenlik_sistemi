from ultralytics import YOLO
import os

def main():
    print('Model Test Ediliyor...')
    
    # Eğitilmiş en iyi ağırlığı (best.pt) yükle
    model_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'poh_tespit', 'optimizasyonlu_egitim', 'weights', 'best.pt')
    dataset_yaml = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'dataset', 'data.yaml')
    
    if not os.path.exists(model_path):
        print(f'HATA: Model dosyası bulunamadı -> {model_path}')
        print('Önce train_poh.py dosyasını çalıştırarak eğitimi tamamlamalısınız.')
        return

    model = YOLO(model_path)
    
    # Test seti üzerinde modeli değerlendir
    metrics = model.val(data=dataset_yaml, split='test')
    
    # Yüzdelik olarak sonuçları ekrana bas
    print('\n--- TEST SETİ BAŞARI SONUÇLARI ---')
    print(f"Hassasiyet (Precision - Yanlış Alarm Yapmama): %{metrics.results_dict['metrics/precision(B)'] * 100:.2f}")
    print(f"Duyarlılık (Recall - PÖH'leri Kaçırmama):     %{metrics.results_dict['metrics/recall(B)'] * 100:.2f}")
    print(f"Ortalama Başarı (mAP50):                      %{metrics.results_dict['metrics/mAP50(B)'] * 100:.2f}")
    print('----------------------------------\n')

if __name__ == '__main__':
    main()
