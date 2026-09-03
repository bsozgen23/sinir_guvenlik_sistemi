# Birleştirilmiş uniformed_person etiket veri seti

Bu paket beş CVAT XML dışa aktarımını ve bunlarla eşleşen 1301 özgün görseli birleştirir. Birleştirme sırası: **Şeyda → Hasan → Songül → Dilara → Aslı**.
Görseller [paylaşılan GitHub deposunun etiketlenecek klasöründen](https://github.com/bsozgen23/sinir_guvenlik_sistemi/tree/15ec49907c2db1c280881af6f12f2597478129be/etiketlenecek) alınmıştır. Depodaki diğer hazır veri setleri bu birleştirmenin parçası değildir.

## Şeyda dosyasına uygulanan sınır

CVAT'taki 259 numaralı kare dâhil tutuldu (0–259; toplam 260 kayıt).
Son korunan görsel: `aa_poh_galeriler/aa_poh_galeriler_g16_018.jpg`.
Sınırdan sonraki 1044 görsel kaydı çıkarıldı. Çıkarılan kayıtlarda toplam 8 kutu vardı; istenen sınır esas alındı.
Korunan Şeyda görsel blokları kaynak XML ile bayt düzeyinde aynıdır. Diğer dört kaynağın tüm mevcut kayıtları ve etiketleri korundu. Orijinal ZIP dosyaları değiştirilmedi.

## İçerik

Toplam 1301 görsel kaydı, 4566 kutu ve tek sınıf: `uniformed_person`.
1015 kayıtta kutu var; 286 kayıtta kutu yok. Korunması istenen aralıklardaki boş kayıtlar da olduğu gibi tutulmuştur. Yeniden etiketleme veya etiket kalitesine ilişkin bir karar uygulanmamıştır.

| Kaynak | Korunan görsel kaydı | Kutu | Kutusuz kayıt |
|---|---:|---:|---:|
| şeyda.zip | 260 | 618 | 39 |
| hasan.zip | 259 | 684 | 73 |
| songül.zip | 261 | 1524 | 20 |
| dilara.zip | 261 | 509 | 70 |
| aslı.zip | 260 | 1231 | 84 |

- `annotations.xml`: birleştirilmiş CVAT for images 1.1 etiketleri. Görsel adları, boyutları, kutu koordinatları ve kutu özellikleri korunmuştur. Birleştirilmiş görsel kimlikleri 0'dan başlayarak benzersizleştirilmiştir. Yerel birleşim için meta görev kimliği 0'dır; mevcut bir CVAT sunucu görevini belirtmez.
- `kaynaklar/seyda_259a_kadar.xml`: Şeyda dosyasının kesilmiş kopyası; diğer dört XML aynı klasörde değiştirilmeden saklanır.
- `yolo/labels/`: YOLO nesne tespiti etiketleri. Sınıf kimliği 0'dır. Alt klasör yapısı görsel yollarıyla aynıdır; boş kayıtların etiket dosyası da boştur.
- `yolo/images/`: etiketlerle bire bir eşleşen 1301 orijinal JPG; dosya adları ve dosya içerikleri değiştirilmemiştir.
- `yolo/classes.txt`: sınıf adı.
- `yolo/tum_gorseller.txt`: tüm görsellerin beklenen göreli yolları; eğitim/doğrulama bölünmesi değildir.
- `yolo/data.yaml.example`: eğitim/doğrulama bölünmesi yapıldıktan sonra düzenlenecek örnek ayar.
- `coco/annotations.json`: aynı kayıtların COCO nesne tespiti biçimi; sınıf kimliği 1'dir. Segmentasyon maskesi yoktur. Kutuların CVAT özellikleri `attributes` alanında saklanır.
- `gorsel_eslestirme.csv`: birleşik kimlik, kaynak ZIP, kaynak kare kimliği, özgün dosya yolu ve kutu sayısı.
- `seyda_cikarilan_kayitlar.csv`: Şeyda kaynağından çıkarılan kayıtların listesi; bu liste eğitim girdisi değildir.
- `veri_seti_ozeti.json`: sayımlar, kaynak dosyaların SHA-256 değerleri ve doğrulama sonuçları.

## Kullanım

ZIP'i açın. YOLO için görseller `yolo/images/`, etiketler `yolo/labels/` içindedir. Örnek görsel: `yolo/images/aa_poh_galeriler/aa_poh_galeriler_g00_000.jpg`; karşılık gelen etiket: `yolo/labels/aa_poh_galeriler/aa_poh_galeriler_g00_000.txt`.

CVAT'a aktarmak için `yolo/images/` altındaki görsellerden, alt klasör yollarını koruyarak bir görev oluşturun ve kökteki `annotations.xml` dosyasını CVAT for images 1.1 olarak içe aktarın. COCO dosyasındaki `file_name` değerlerinin görsel kökü `yolo/images/` klasörüdür.

Veri tek bir bütün olarak birleştirildi; eğitim/doğrulama/test ayrımı uygulanmadı. Eğitim öncesinde uygun listeleri oluşturup `data.yaml.example` dosyasındaki yolları düzenleyerek dosyayı `data.yaml` adıyla kaydedin. Aynı videoya ait benzer kareleri eğitim ve değerlendirme bölümlerine dağıtmayan bir ayrım kullanın.

## Korunan kaynak özellikleri ve doğrulama

Hasan XML'inde 129 ve 169 numaralı kaynak kare kayıtları zaten yoktur; eklenmemiştir. Kaynakta mevcut aynı koordinatlı tekrar kutular (Şeyda 155, Songül 113) değiştirilmeden korunmuştur. Bunlar otomatik olarak silinmemiştir.

Korunan tüm kutular ve görsel özellikleri kaynaklarla karşılaştırıldı. Görsel yolları ve birleşik kimlikler benzersizdir; kutular görsel sınırları içindedir. YOLO dönüşümünde geri hesaplanan koordinat farkı 0,000001 pikselden küçüktür. Her JPG'nin bütünlüğü, GitHub dosyasıyla aynı içeriğe sahip olduğu ve boyutlarının CVAT XML'iyle eşleştiği doğrulandı. Kaynak ZIP'lerin SHA-256 değerleri değişmemiştir.
