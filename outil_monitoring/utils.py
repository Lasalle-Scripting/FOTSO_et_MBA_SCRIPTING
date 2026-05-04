import os
import shutil
import datetime
import tempfile
import psutil

THRESHOLD_CPU = 80.0
THRESHOLD_RAM = 90.0
THRESHOLD_DISK = 95.0

def get_critical_alerts(cpu, ram, disk):
    alerts = []
    if cpu > THRESHOLD_CPU:
        alerts.append("CPU")
    if ram > THRESHOLD_RAM:
        alerts.append("RAM")
    if disk > THRESHOLD_DISK:
        alerts.append("Disque")
    return alerts

def clean_disk():
    folders_to_clean = [tempfile.gettempdir()]
    
    # Ajout optionnel du cache des navigateurs courants (chemins Windows standards)
    user_profile = os.environ.get('USERPROFILE')
    if user_profile:
        folders_to_clean.append(os.path.join(user_profile, 'AppData', 'Local', 'Google', 'Chrome', 'User Data', 'Default', 'Cache'))
        folders_to_clean.append(os.path.join(user_profile, 'AppData', 'Local', 'Microsoft', 'Edge', 'User Data', 'Default', 'Cache'))

    files_deleted = 0
    for folder in folders_to_clean:
        if not os.path.exists(folder):
            continue
        try:
            for filename in os.listdir(folder):
                file_path = os.path.join(folder, filename)
                try:
                    if os.path.isfile(file_path) or os.path.islink(file_path):
                        os.unlink(file_path)
                        files_deleted += 1
                    elif os.path.isdir(file_path):
                        shutil.rmtree(file_path)
                except Exception:
                    pass
        except Exception:
            pass
    return files_deleted

def optimize_memory():
    """Identifie les processus lourds."""
    heavy_processes = []
    try:
        for proc in psutil.process_iter(['name', 'memory_percent']):
            try:
                if proc.info['memory_percent'] > 5.0:
                    heavy_processes.append(proc.info['name'])
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                pass
    except Exception:
        pass
    return sorted(list(set(heavy_processes)))[:3]

def get_smart_advice(stats):
    diagnostics = []
    
    # Diagnostic CPU
    if stats['cpu'] > THRESHOLD_CPU:
        heavy_cpu = []
        try:
            for proc in psutil.process_iter(['name', 'cpu_percent']):
                if proc.info['cpu_percent'] > 10.0:
                    heavy_cpu.append(proc.info['name'])
        except: pass
        cause = f"Usage intensif par : {', '.join(heavy_cpu[:2])}" if heavy_cpu else "Multiples processus en arrière-plan."
        diagnostics.append({
            "type": "CPU",
            "cause": cause,
            "solution": "Fermez les applications non utilisées ou suspendez les mises à jour en cours."
        })

    # Diagnostic RAM
    if stats['ram'] > THRESHOLD_RAM:
        heavy_ram = optimize_memory()
        cause = f"Saturation par : {', '.join(heavy_ram)}" if heavy_ram else "Trop d'applications ouvertes simultanément."
        diagnostics.append({
            "type": "RAM",
            "cause": cause,
            "solution": "Redémarrez votre navigateur ou utilisez le bouton 'Analyse Mémoire' pour identifier les coupables."
        })

    # Diagnostic Disque
    if stats['disk'] > THRESHOLD_DISK:
        diagnostics.append({
            "type": "Disque",
            "cause": "Accumulation de fichiers temporaires et cache de navigation.",
            "solution": "Cliquez sur 'Nettoyer Disque' pour libérer immédiatement de l'espace."
        })
    
    return diagnostics
