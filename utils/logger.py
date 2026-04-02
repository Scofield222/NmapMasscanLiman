from colorama import Fore, Style, init
import datetime

# Renkli çıktıları başlat
init(autoreset=True)

class Logger:
    @staticmethod
    def _get_time():
        return datetime.datetime.now().strftime("%H:%M:%S")

    def info(self, mesaj):
        print(f"[{Fore.CYAN}{self._get_time()}{Style.RESET_ALL}] {Fore.BLUE}[BİLGİ] {mesaj}")

    def success(self, mesaj):
        print(f"[{Fore.CYAN}{self._get_time()}{Style.RESET_ALL}] {Fore.GREEN}[BAŞARI] {mesaj}")

    def warning(self, mesaj):
        print(f"[{Fore.CYAN}{self._get_time()}{Style.RESET_ALL}] {Fore.YELLOW}[UYARI] {mesaj}")

    def error(self, mesaj):
        print(f"[{Fore.CYAN}{self._get_time()}{Style.RESET_ALL}] {Fore.RED}[HATA] {mesaj}")
