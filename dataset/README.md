# Sınır Güvenlik Tespiti - Veri Seti

POH (Polis Özel Harekat) üniforma + silah tespiti projesi için birleştirilmiş YOLO veri seti.

## İçerik

| Klasör | Görsel | Sınıf(lar) | Kaynak / Lisans |
|--------|--------|------------|-----------------|
| `train/ valid/ test/` (kök) | 671 | Handgun, Knife, Rifle, Shotgun (+Missile, Sword, Tank) | Roboflow `weapon-detection-using-yolov8` — CC BY 4.0 |
| `police-dataset/` | 844 | police | Roboflow `police-detection` — CC BY 4.0 |
| `poh-uniform-toplama/` | 606 | poh_personel | Eski askeri setten ayıklandı (asker → poh_personel) |

Toplam ~2.100 görsel.

## Notlar

- Kök ve `police-dataset/` klasörleri CC BY 4.0 lisanslıdır; her klasördeki `README.roboflow.txt` / `README.dataset.txt` dosyaları atıf/lisans bilgisini içerir, silmeyin.
- `poh-uniform-toplama/` görselleri çoğunlukla video karesi kaynaklı (near-duplicate); eğitimden önce tekilleştirme (dedup) + yeniden bölme önerilir.
- Sınıf şemaları henüz birleştirilmedi; her alt setin kendi `data.yaml` dosyası var. Eğitim aşamasında tek şemaya indirgenecek.

## Planlanan nihai sınıf şeması

```
0: poh_personel
1: Handgun
2: Knife
3: Rifle
4: Shotgun
```

"Düşman/dost" ayrımı eğitilen bir sınıf değil, kod tarafında kural olarak uygulanır:
POH üniforması var → dost; yok + silah var → tehdit.
