from ultralytics import YOLO
import os
import yaml

def main():
    print('Model Test Ediliyor...')
    
    current_dir = os.path.dirname(os.path.abspath(__file__))
    model_path = os.path.join(current_dir, 'poh_tespit', 'optimizasyonlu_egitim', 'weights', 'best.pt')
    dataset_dir = os.path.join(current_dir, 'dataset')
    dataset_yaml = os.path.join(dataset_dir, 'data.yaml')
    
    if not os.path.exists(model_path):
        print(f'HATA: Model dosyası bulunamadı -> {model_path}')
        print('Önce train_poh.py dosyasını çalıştırarak eğitimi tamamlamalısınız.')
        return

    # test işlemi için de path güncelleyelim (emin olmak için)
    with open(dataset_yaml, 'r') as f:
        data_config = yaml.safe_load(f)
    data_config['path'] = dataset_dir
    with open(dataset_yaml, 'w') as f:
        yaml.dump(data_config, f, default_flow_style=False)

    model = YOLO(model_path)
    
    metrics = model.val(data=dataset_yaml, split='test')
    
    print('\n--- TEST SETİ BAŞARI SONUÇLARI ---')
    print(f"Hassasiyet (Precision - Yanlış Alarm Yapmama): %{metrics.results_dict['metrics/precision(B)'] * 100:.2f}")
    print(f"Duyarlılık (Recall - PÖH'leri Kaçırmama):     %{metrics.results_dict['metrics/recall(B)'] * 100:.2f}")
    print(f"Ortalama Başarı (mAP50):                      %{metrics.results_dict['metrics/mAP50(B)'] * 100:.2f}")
    print('----------------------------------\n')

if __name__ == '__main__':
    main()
