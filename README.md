# 🛡️ Bağlantı Noktası Taramaları & Liman Analizi

Bu proje, bir kuruluşun dış internete açtığı açık kapıları (bağlantı noktalarını) haritalamak ve analiz etmek için geliştirilmiştir.

## 🛠️ Uygulama Alanı / Örnekler
* **Nmap Kullanımı:** Hedef sistemlerdeki servis versiyonlarını ve işletim sistemlerini derinlemesine analiz eder.
* **Masscan Entegrasyonu:** Çok geniş IP aralıklarında internete açık limanları saniyeler içinde tespit eder.
* **Liman Analizi:** Açık bulunan bağlantı noktalarının hangi servisleri barındırdığını ve zafiyet risklerini raporlar.

## 🚀 Hızlı Kullanım
```bash
# Nmap modu ile detaylı analiz
python main.py -t 192.168.1.1 --mode nmap

# Masscan mantığı ile hızlı liman tespiti
python main.py -t 192.168.1.1 --mode masscan
