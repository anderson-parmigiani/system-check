from datetime import datetime
import socket
import psutil
import cpuinfo

class Tools:
    def __init__(self):
        self.stored_hostname = None
        self.stored_ip_address = None

    def hostname(self):
        self.stored_hostname = socket.gethostname()
        return self.stored_hostname

    def cpu(self):
        info = cpuinfo.get_cpu_info()
        return f"{info['brand_raw']}"

    def ram(self):
        total_memory = psutil.virtual_memory().total
        if total_memory < 1024 ** 2:
            return f"{round(total_memory / 1024, 2)} MB "
        else:
            return f"{round(total_memory / 1024 ** 3, 2)} GB "

    def disk_usage(self):
        disk_info = psutil.disk_usage('/')
        total_bytes = disk_info.total
        if total_bytes <= 1024 ** 3:
            total_mb = round(total_bytes / 1024, 2)
            return f"{total_mb} MB"
        else:
            total_gb = round(total_bytes / (1024 ** 3), 2)
            return f"{total_gb} GB"

    def last_boot(self):
        return f"Ultimo encendido {datetime.fromtimestamp(psutil.boot_time()).strftime("%d-%m-%Y %H:%M:%S")}"

    def get_ip_address(self):
        try:
            ip_address = socket.gethostbyname(self.stored_hostname)
            self.stored_ip_address = ip_address
            return self.stored_ip_address
        except socket.error:
            self.stored_ip_address = "n/d"
            return "n/d"

    def get_mac_address(self):
        ip_address = self.stored_ip_address

        if ip_address == "n/d":
            return "n/d"

        for interface, addresses in psutil.net_if_addrs().items():
            for addr in addresses:
                if addr.family == socket.AF_INET and addr.address == ip_address:
                    for addr in psutil.net_if_addrs()[interface]:
                        if addr.family == psutil.AF_LINK:
                            return addr.address

                        return "n/d"