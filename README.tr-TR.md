# JoomTheme Gallery

[English](README.md) · [0.7.3 sürümü](https://github.com/joomtheme/JoomTheme-Gallery/releases/tag/v0.7.3) · [Paketi indir](https://github.com/joomtheme/JoomTheme-Gallery/releases/download/v0.7.3/pkg_jtgallery_v0.7.3.zip) · [Destek](https://github.com/joomtheme/JoomTheme-Gallery/issues) · [JoomTheme](https://joomtheme.com)

JoomTheme Gallery, tek kurulum paketiyle dağıtılan yerel bir Joomla 6 galeri eklentisidir:

- `com_jtgallery` — Atum ile uyumlu yönetim arayüzü üzerinden galeri, kategori ve görsel yönetimi.
- `mod_jtgallery` — seçilen galerinin görsellerini yayınlayan duyarlı site modülü.

Güncel kararlı sürüm **0.7.3**'tür.

## Gereksinimler

- Joomla 6.1.x (Joomla 6.1.3 ile test edilmiştir)
- PHP 8.3 veya üzeri
- JPEG, PNG ve WebP destekleyen, Joomla ile uyumlu bir görsel işleme ortamı

## Öne çıkanlar

- Joomla MVC, ACL, kategoriler, erişim seviyeleri ve çoklu dil filtreleriyle yerel bütünleşme
- Joomla ön yüz şablonlarıyla uyumlu duyarlı galeri düzenleri
- Atum uyumlu yönetim paneli ve liste görünümleri
- Orijinal, büyük, orta ve küçük görsel türevleri
- Varsayılan olarak etkin isteğe bağlı EXIF/GPS ve ek metadata temizliği
- Klavye ve dokunmatik kullanımına uygun, Bootstrap benzeri yumuşak arka planlı lightbox
- Bileşen ve site modülünü birlikte kuran tek Joomla paketi
- Joomla güncelleme sunucusu ve değişiklik günlüğü desteği

## Kurulum

1. [`pkg_jtgallery_v0.7.3.zip`](https://github.com/joomtheme/JoomTheme-Gallery/releases/download/v0.7.3/pkg_jtgallery_v0.7.3.zip) paketini [resmî sürüm sayfasından](https://github.com/joomtheme/JoomTheme-Gallery/releases/tag/v0.7.3) indirin.
2. Joomla yönetiminde **Sistem → Kurulum → Eklentiler** sayfasını açın.
3. Paketi yükleyin. Joomla bileşeni ve site modülünü birlikte kurar.
4. Bir galeri oluşturup görselleri ekleyin; ardından menü öğesi veya **JoomTheme Gallery** modülüyle yayınlayın.

Yeni bir paket mevcut kurulumun üzerine yüklendiğinde yerinde yükseltme yapılır.

## Otomatik güncellemeler

Paket aşağıdaki genel Joomla servislerini otomatik olarak kaydeder:

- Güncelleme akışı: [`updates/update.xml`](https://raw.githubusercontent.com/joomtheme/JoomTheme-Gallery/main/updates/update.xml)
- Joomla değişiklik günlüğü: [`updates/changelog.xml`](https://raw.githubusercontent.com/joomtheme/JoomTheme-Gallery/main/updates/changelog.xml)

Joomla, **Sistem → Güncelleme → Eklentiler** ekranından akışı denetler ve kurulumdan önce yayınlanan paketi SHA-256, SHA-384 ve SHA-512 karmalarıyla doğrular.

Kurulabilir paketler değişmez GitHub Release varlıkları olarak yayınlanır. GitHub'ın otomatik oluşturduğu kaynak kodu arşivleri Joomla kurulum paketi değildir.

## Belgeleme ve destek

- [Sürüm geçmişi](CHANGELOG.md)
- [Destek rehberi](SUPPORT.md)
- [Katkıda bulunma](CONTRIBUTING.md)
- [Güvenlik politikası](SECURITY.md)
- [Sorun bildirimleri](https://github.com/joomtheme/JoomTheme-Gallery/issues)

Güvenlik açıklarını lütfen güvenlik politikasında belirtilen özel kanaldan bildirin.

## Lisans

GNU Genel Kamu Lisansı sürüm 2 veya üzeri. Ayrıntılar için [LICENSE](LICENSE) dosyasına bakın.
