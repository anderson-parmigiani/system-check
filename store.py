import platform

os, release = (platform.system(), platform.release())

if os == "Windows":
    from windows_tools import WindowsTools
    os_info = WindowsTools()
elif os == "Linux":
    from linux_tools import LinuxTools
    os_info = LinuxTools()
else:
    raise Exception("Sistema operativo no soportado: {}".format(os))