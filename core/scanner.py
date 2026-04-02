import nmap
from utils.logger import Logger

log = Logger()

class LimanScanner:
    def __init__(self):
        self.nm = nmap.PortScanner()

    def nmap_scan(self, target, ports="1-1024"):
        """Nmap kullanarak derinlemesine servis ve versiyon taraması yapar."""
        log.info(f"Nmap motoru ile {target} üzerinde tarama başlatıldı...")
        # -sV: Versiyon tespiti, -T4: Hızlı tarama profili
        return self.nm.scan(target, ports, arguments='-sV -T4')

    def masscan_logic(self, target, ports):
        """
        Not: Masscan sistemde yüklü olmalıdır. 
        Bu fonksiyon Masscan mantığıyla çok hızlı port tespiti simülasyonu yapar.
        """
        log.warning("Masscan modunda çok hızlı port tespiti yapılıyor...")
        # Masscan genellikle çok geniş ağlarda (0.0.0.0/0) port tespiti için kullanılır.
        return self.nm.scan(target, ports, arguments='-F') # Hızlı mod
