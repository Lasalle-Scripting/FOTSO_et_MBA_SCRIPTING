import psutil

def get_disk_usage():
    try:
        usage = psutil.disk_usage('C:')
        return round(usage.percent, 2)
    except Exception as e:
        print(f"Erreur disque: {e}")
        return 0.0

def get_ram_usage():
    try:
        ram = psutil.virtual_memory()
        return round(ram.percent, 2)
    except Exception as e:
        print(f"Erreur RAM: {e}")
        return 0.0

def get_cpu_usage():
    try:
        cpu = psutil.cpu_percent(interval=1)
        return round(cpu, 2)
    except Exception as e:
        print(f"Erreur CPU: {e}")
        return 0.0

def collect_all():
    return {
        'cpu': get_cpu_usage(),
        'ram': get_ram_usage(),
        'disk': get_disk_usage()
    }