from tools import Tools
from store import os, release
import winreg

class WindowsTools(Tools):
    def __init__(self):
        super().__init__()
        self.stored_hostname = None

    def version(self):
        version_info = f"{os} {release}"

        try:
            with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows NT\CurrentVersion") as key:
                edition = winreg.QueryValueEx(key, "EditionID")[0]
                build = winreg.QueryValueEx(key, "CurrentBuild")[0]

                if edition == "Core":
                    version_info += f" Home ({build})"
                else:
                    version_info += f" {edition} ({build})"

        except Exception:
            version_info += " n/d"

        return version_info