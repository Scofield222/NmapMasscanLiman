class LimanAnalyzer:
    def __init__(self, raw_data):
        self.raw_data = raw_data

    def analiz_et(self):
        """Bulunan açık kapıları (limanları) güvenlik açısından analiz eder."""
        analiz_sonuclari = []
        for host in self.raw_data.get('scan', {}):
            for proto in self.raw_data['scan'][host].all_protocols():
                ports = self.raw_data['scan'][host][proto].keys()
                for port in ports:
                    data = self.raw_data['scan'][host][proto][port]
                    analiz_sonuclari.append({
                        "liman": port,
                        "servis": data.get('name'),
                        "versiyon": data.get('version'),
                        "durum": data.get('state')
                    })
        return analiz_sonuclari
