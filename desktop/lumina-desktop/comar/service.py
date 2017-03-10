
from comar.service import *

serviceType = "local"
serviceConf = "lumina-desktop"
serviceDefault = "conditional"

serviceDesc = _({"en": "Lumina-desktop",
                 "tr": "Lumina-desktop"})

@synchronized
def start():
    startService(command="/usr/sbin/lumina-desktop",
                 args = config.get("args", "destroy"),
                 donotify=True)

@synchronized
def stop():
    stopService(command="/usr/sbin/lumina-desktop",
                donotify=True)

def ready():
    import os
    status = is_on()
    if status == "on" or (status == "conditional" and os.path.exists("/sys/coffee/ready")):
        start()

def status():
    return checkDaemon("/var/run/lumina-desktop.pid")

