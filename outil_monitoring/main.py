import time
import monitor
import reporter
import utils

def main():
    print("==========Démarrage du monitoring système...===========\n")
    
    while True:
        try:
            print("Collecte des données...\n")
            stats = monitor.collect_all()
            
            print(f"CPU: {stats['cpu']}% |\nRAM: {stats['ram']}% |\nDisque: {stats['disk']}%")
            
            reporter.generate_report(stats)
            
            alerts = utils.get_critical_alerts(stats['cpu'], stats['ram'], stats['disk'])
            
            if "Disque" in alerts:
                print("ALERT DISQUE ! Lancement du nettoyage...\n")
                utils.clean_disk()
            
            print("Attente de 60 secondes avant la prochaine vérification...\n")
            time.sleep(60)
            
        except KeyboardInterrupt:
            print("\nArrêt du programme.")
            break
        except Exception as e:
            print(f"Erreur principale: {e}")
            time.sleep(60)

if __name__ == "__main__":
    main()