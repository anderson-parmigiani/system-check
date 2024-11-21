from tools import Tools

class LinuxTools(Tools):
    def __init__(self):
        super().__init__()

    def version(self):
        try:
            with open("/etc/os-release") as f:
                os_info = f.readlines()
                for line in os_info:
                    if line.startswith("NAME="):
                        name = line.split("=")[1].strip().strip('"')
                    elif line.startswith("VERSION_ID="):
                        version_id = line.split("=")[1].strip().strip('"')

            version_info = f"{name} ({version_id})"

        except Exception:
            version_info += " n/d"

        return version_info