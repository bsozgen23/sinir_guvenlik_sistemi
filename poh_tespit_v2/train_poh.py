from ultralytics import YOLO
import os
import yaml

def make_paths_absolute(txt_name, dataset_dir):
    rel_path = os.path.join(dataset_dir, txt_name)
    abs_path = os.path.join(dataset_dir, f'abs_{txt_name}')
    
    if not os.path.exists(rel_path):
        return None
        
    with open(rel_path, 'r') as f:
        lines = f.read().splitlines()
        
    abs_lines = []
    for line in lines:
        if line.strip():
            # Create an absolute path for each image
            abs_img_path = os.path.join(dataset_dir, line.strip())
            # Replace backslashes with forward slashes for safety in YOLO
            abs_lines.append(abs_img_path.replace('\\', '/'))
            
    with open(abs_path, 'w') as f:
        f.write('\n'.join(abs_lines))
        
    return f'abs_{txt_name}'

def main():
    print('PÖH Tespit Sistemi Eğitimine Başlanıyor...')
    
    # 1. Ön eğitilmiş Large modeli yükle
    model = YOLO('yolo11l.pt') 

    # 2. Path hatasını TAMAMEN çözmek için TXT dosyalarının içini Mutlak Yol (Absolute Path) ile doldur
    current_dir = os.path.dirname(os.path.abspath(__file__))
    dataset_dir = os.path.join(current_dir, 'dataset')
    dataset_yaml = os.path.join(dataset_dir, 'data.yaml')
    
    # Mutlak yollu txt dosyalarını oluştur
    abs_train = make_paths_absolute('train.txt', dataset_dir)
    abs_val = make_paths_absolute('val.txt', dataset_dir)
    abs_test = make_paths_absolute('test.txt', dataset_dir)
    
    with open(dataset_yaml, 'r') as f:
        data_config = yaml.safe_load(f)
    
    # path değişkenini ve txt dosyalarını mutlak yola göre ayarla
    data_config['path'] = dataset_dir.replace('\\', '/')
    if abs_train: data_config['train'] = abs_train
    if abs_val: data_config['val'] = abs_val
    if abs_test: data_config['test'] = abs_test
    
    with open(dataset_yaml, 'w') as f:
        yaml.dump(data_config, f, default_flow_style=False)

    print('Resim yolları %100 mutlak yola (Absolute Path) çevrildi ve path hatası çözüldü!')

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
