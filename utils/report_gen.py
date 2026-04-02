import json
import datetime
import os

class ReportGenerator:
    def __init__(self, hedef):
        self.hedef = hedef
        self.tarih = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    def json_rapor_olustur(self, analiz_verisi):
        """Liman analizi sonuçlarını JSON dosyasına kaydeder."""
        dosya_adi = f"liman_analizi_{self.hedef}_{self.tarih}.json"
        
        rapor_icerik = {
            "hedef": self.hedef,
            "tarama_tarihi": self.tarih,
            "bulgular": analiz_verisi,
            "araclar": ["Nmap", "Masscan Logic"]
        }

        try:
            with open(dosya_adi, "w", encoding="utf-8") as f:
                json.dump(rapor_icerik, f, indent=4, ensure_ascii=False)
            return dosya_adi
        except Exception as e:
            return f"Rapor hatası: {str(e)}"
