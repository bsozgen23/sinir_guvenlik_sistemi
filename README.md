# Sınır Güvenlik Sistemi

POH (Polis Özel Harekat) üniforması ve silah tespiti yapan görüntü işleme projesi.

## Amaç

Görüntüdeki kişileri tespit edip, üniforma ve silah durumuna göre sınıflandırmak:

```
POH üniforması var             -> DOST
POH üniforması yok + silah var -> TEHDİT
POH üniforması yok + silah yok -> sivil / bilinmeyen
```

**Önemli:** "Dost/düşman" eğitilen bir sınıf değildir. Model yalnızca *üniforma* ve *silah* tespit eder; dost/tehdit kararı kod tarafında kural olarak uygulanır. Ayırt edici özellik üniformadır.

## Yapı

Proje **iki ayrı model** olarak tasarlandı; her veri seti bağımsız eğitilir.

### `uniforma/` — üniforma tespiti (etiketli, hazır)

| Sınıf | Kutu | Kaynak |
|-------|------|--------|
| `poh_personel` | 1239 | Önceki askeri setten ayıklandı (`asker` -> `poh_personel`) |
| `police` | 2283 | Roboflow `police-detection` — CC BY 4.0 |

1450 görsel (train 1207 / valid 142 / test 101). Atıf: `uniforma/ATIF.txt`

### `silah/` — silah tespiti (etiketli, hazır)

| Sınıf | Kutu |
|-------|------|
| `Handgun` | 103 |
| `Knife` | 132 |
| `Rifle` | 109 |
| `Shotgun` | 140 |

371 görsel (train 258 / valid 77 / test 36). Roboflow `weapon-detection-using-yolov8` — CC BY 4.0. Atıf: `silah/ATIF.txt`

### `etiketlenecek/` — ham POH fotoğrafları (etiketsiz)

Ekip tarafından toplanan, **henüz etiketlenmemiş** POH görselleri. Roboflow Annotate ile `poh_personel` olarak etiketlenip `uniforma/` setine eklenecek.

| Klasör | Foto | Kaynak |
|--------|------|--------|
| `aa_poh_galeriler/` | 355 | Anadolu Ajansı galerileri |
| `aa_poh_haberleri/` | 210 | Anadolu Ajansı haberleri |
| `ig_profile_ozelharekatbaskanlik/` | 216 | Özel Harekat Başkanlığı (resmi hesap) |
| `tatbikat_videolarindan/` | 523 | Tatbikat videolarından kareler |

> Not: Bu görsellerin kaynak/kullanım hakları belgelenmelidir (özellikle Anadolu Ajansı telifli basın içeriğidir). Akademik kullanım için ilgili izinler alınmalı.

## Önemli Notlar

- CC BY 4.0 lisanslı bölümlerin atıf bilgisi klasörlerdeki `ATIF.txt` dosyalarındadır, silmeyin.
- `uniforma/` içindeki POH görselleri ve `etiketlenecek/tatbikat_videolarindan/` çoğunlukla video karesidir (near-duplicate). Eğitimden önce tekilleştirme (dedup) ve yeniden bölme gerekir; aksi halde train/test sızıntısı metrikleri olduğundan yüksek gösterir.
- Her hazır veri setinin kendi `data.yaml` dosyası vardır (YOLO formatı).

## Yol Haritası

- [x] Silah veri seti (`silah/`)
- [x] Üniforma veri seti (`uniforma/`)
- [x] Ham POH fotoğrafları toplandı (`etiketlenecek/`)
- [ ] `etiketlenecek/` görsellerini etiketle -> `uniforma/`ya ekle
- [ ] Dedup + yeniden bölme (near-duplicate)
- [ ] Silah modeli eğitimi (YOLO transfer learning)
- [ ] Üniforma modeli eğitimi
- [ ] Dost/tehdit kural motoru (iki modelin çıktısını birleştirir)
- [ ] Görüntü/video çıkarım uygulaması

## Durum

Bu bir **prototip / kavram kanıtı** çalışmasıdır. Eğitim verisi büyük oranda internet kaynaklı tanıtım/tören görsellerinden oluştuğu için, gerçek saha koşullarında (güvenlik kamerası, uzak/bulanık görüntü) performans düşer. Gerçek dağıtım için farklı ve daha çeşitli veri gerekir.
