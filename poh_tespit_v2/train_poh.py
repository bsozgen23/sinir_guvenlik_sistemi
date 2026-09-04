from ultralytics import YOLO
import os
import yaml

def main():
    print('PÖH Tespit Sistemi Eğitimine Başlanıyor...')
    
    # 1. Ön eğitilmiş Large modeli yükle
    model = YOLO('yolo11l.pt') 

    # 2. data.yaml yolunu sistemdeki mutlak yola göre otomatik güncelle (Path hatasını engellemek için)
    current_dir = os.path.dirname(os.path.abspath(__file__))
    dataset_dir = os.path.join(current_dir, 'dataset')
    dataset_yaml = os.path.join(dataset_dir, 'data.yaml')
    
    with open(dataset_yaml, 'r') as f:
        data_config = yaml.safe_load(f)
    
    # path değişkenini bu bilgisayardaki tam konuma ayarla
    data_config['path'] = dataset_dir
    
    with open(dataset_yaml, 'w') as f:
        yaml.dump(data_config, f, default_flow_style=False)

    print(f'Veri seti yolu otomatik ayarlandı: {dataset_dir}')

    # 3. Üst Düzey Optimizasyonlarla Eğitimi Başlat
    results = model.train(
        data=dataset_yaml,
        epochs=300,
        imgsz=1024,
        batch=16,
        optimizer='AdamW',
        cos_lr=True,
        lr0=0.001,
        patience=50,
        project='poh_tespit',
        name='optimizasyonlu_egitim',
        mosaic=1.0,
        mixup=0.2,
        hsv_h=0.015,
        hsv_s=0.7,
        hsv_v=0.4,
        device=0 
    )
    
    print('Eğitim Başarıyla Tamamlandı!')
    
if __name__ == '__main__':
    main()
