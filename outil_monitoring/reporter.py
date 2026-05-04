import datetime
import utils

def generate_report(stats):
    try:
        filename = "system_report.txt"
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        alerts = utils.get_critical_alerts(stats['cpu'], stats['ram'], stats['disk'])
        
        with open(filename, 'w') as f:
            f.write("===== RAPPORT SYSTEME =====\n\n")
            f.write(f"Date : {now}\n\n")
            
            cpu_status = "(critique)" if stats['cpu'] > utils.THRESHOLD_CPU else "(normal)"
            f.write(f"CPU : {stats['cpu']}% {cpu_status}\n")
            
            ram_status = "(critique)" if stats['ram'] > utils.THRESHOLD_RAM else "(normal)"
            f.write(f"RAM : {stats['ram']}% {ram_status}\n")
            
            disk_status = "(critique)" if stats['disk'] > utils.THRESHOLD_DISK else "(normal)"
            f.write(f"Disque : {stats['disk']}% {disk_status}\n")
            
            f.write("\nRecommandations :\n")
            if not alerts:
                f.write("- Aucune action nécessaire.\n")
            else:
                if "CPU" in alerts:
                    f.write("- Vérifier les processus actifs.\n")
                if "RAM" in alerts:
                    f.write("- Redémarrer les services gourmands.\n")
                if "Disque" in alerts:
                    f.write("- Libérer de l'espace disque.\n")
        
        print(f"Rapport généré : {filename}\n")
        
    except Exception as e:
        print(f"Erreur rapport: {e}")