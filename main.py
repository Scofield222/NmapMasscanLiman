import argparse
from core.scanner import LimanScanner
from core.analyzer import LimanAnalyzer
from utils.logger import Logger

def main():
    log = Logger()
    parser = argparse.ArgumentParser(description="Liman Analizi ve Port Tarama Sistemi")
    parser.add_argument("-t", "--target", required=True, help="Hedef IP/Domain")
    parser.add_argument("--mode", choices=['nmap', 'masscan'], default='nmap', help="Tarama modu")
    args = parser.parse_args()

    scanner = LimanScanner()
    
    # Seçilen moda göre tarama (Nmap veya Masscan mantığı)
    if args.mode == 'nmap':
        sonuclar = scanner.nmap_scan(args.target)
    else:
        sonuclar = scanner.masscan_logic(args.target, "1-10000")

    # Liman Analizi Aşaması
    analyzer = LimanAnalyzer(sonuclar)
    rapor = analyzer.analiz_et()

    log.success(f"\n--- {args.target} İÇİN LİMAN ANALİZ RAPORU ---")
    for r in rapor:
        print(f"[*] Liman: {r['liman']} | Servis: {r['servis']} | Versiyon: {r['versiyon']} | Durum: {r['durum']}")

if __name__ == "__main__":
    main()
