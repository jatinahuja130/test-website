import psutil
import shutil

def check_disk_usage(x):
    du = shutil.disk_usage(x)
    free = du.free/du.total *100
    return free>15

def check_cpu_usage():
    usuage  = psutil.cpu_percent(1)
    return usuage>75


if not check_disk_usage("/") or check_cpu_usage():
    print("error")
else:
    print("OK!")
