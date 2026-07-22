# Sınır Güvenlik Sistemi

POH (Polis Özel Harekat) üniforması ve silah tespiti yapan görüntü işleme projesi.

## Amaç

Görüntüdeki kişileri tespit edip, üniforma ve silah durumuna göre sınıflandırmak:

```
POH üniforması var             -> DOST
POH üniforması yok + silah var -> TEHDİT
POH üniforması yok + silah yok -> sivil / bilinmeyen
```

**Önemli:** "Dost/düşman" eğitilen bir sınıf değildir. Model yalnızca *üniforma* ve *silah* tespit eder; dost/tehdit kararı kod tarafında kural olarak uygulanır. Bir kişinin "düşman" olduğu görüntüden öğrenilemez — ayırt edici özellik üniformadır.

## Veri Seti (`dataset/`)

| Bölüm | Görsel | Sınıf(lar) | Kaynak / Lisans |
|-------|--------|------------|-----------------|
| `dataset/train,valid,test` | 671 | Handgun, Knife, Rifle, Shotgun (+Missile, Sword, Tank) | Roboflow `weapon-detection-using-yolov8` — CC BY 4.0 |
| `dataset/police-dataset/` | 844 | police | Roboflow `police-detection` — CC BY 4.0 |
| `dataset/poh-uniform-toplama/` | 606 | poh_personel | Önceki askeri setten ayıklandı (`asker` -> `poh_personel`) |

Toplam ~2.100 görsel.

### Notlar

- CC BY 4.0 lisanslı bölümlerin atıf bilgisi `README.roboflow.txt` / `README.dataset.txt` dosyalarındadır, silmeyin.
- `poh-uniform-toplama/` görselleri çoğunlukla video karesi kaynaklıdır (near-duplicate). Eğitimden önce tekilleştirme (dedup) ve yeniden bölme gerekir; aksi halde train/test sızıntısı metrikleri şişirir.
- Alt setlerin sınıf şemaları henüz birleştirilmemiştir; her birinin kendi `data.yaml` dosyası vardır.

### Planlanan nihai sınıf şeması

```
0: poh_personel
1: Handgun
2: Knife
3: Rifle
4: Shotgun
```

## Yol Haritası

- [x] Silah veri seti
- [x] Polis üniforma veri seti
- [x] POH personel veri seti
- [ ] Veri setlerini tek şema altında birleştirme + dedup
- [ ] Model eğitimi (YOLO transfer learning)
- [ ] Dost/tehdit kural motoru
- [ ] Görüntü/video çıkarım uygulaması

## Durum

Bu bir **prototip / kavram kanıtı** çalışmasıdır. Eğitim verisi büyük oranda internet kaynaklı tanıtım ve tören görsellerinden oluştuğu için, gerçek saha koşullarında (güvenlik kamerası, uzak/bulanık görüntü) performans düşer. Gerçek dağıtım için farklı ve daha çeşitli veri gerekir.

## Geçmiş

Bu repoda önceden askeri temalı bir veri seti (`asker`, `Tufek`, `tabanca` vb. 2097 görsel) bulunuyordu. Proje POH odağına kaydığı için o set kaldırılmış, yerine yukarıdaki üç bölümlü veri seti eklenmiştir. Eski set git geçmişinde korunmaktadır.
