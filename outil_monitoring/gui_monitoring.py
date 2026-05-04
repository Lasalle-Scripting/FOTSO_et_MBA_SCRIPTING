import customtkinter as ctk
import monitor
import utils
import reporter
import threading
import time

# Configuration du thème
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

class MonitoringApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Système Monitoring - Outil Scolaire")
        self.geometry("800x750")

        # Configuration de la grille
        self.grid_columnconfigure(0, weight=1)

        # --- Titre ---
        self.label_title = ctk.CTkLabel(self, text="Tableau de Bord Système", font=ctk.CTkFont(size=24, weight="bold"))
        self.label_title.grid(row=0, column=0, padx=20, pady=20)

        # --- Stats Frame ---
        self.stats_frame = ctk.CTkFrame(self)
        self.stats_frame.grid(row=1, column=0, padx=20, pady=10, sticky="ew")
        self.stats_frame.grid_columnconfigure(1, weight=1)

        # CPU
        self.cpu_label = ctk.CTkLabel(self.stats_frame, text="CPU: 0%", width=120)
        self.cpu_label.grid(row=0, column=0, padx=10, pady=10)
        self.cpu_bar = ctk.CTkProgressBar(self.stats_frame)
        self.cpu_bar.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
        self.cpu_bar.set(0)

        # RAM
        self.ram_label = ctk.CTkLabel(self.stats_frame, text="RAM: 0%", width=120)
        self.ram_label.grid(row=1, column=0, padx=10, pady=10)
        self.ram_bar = ctk.CTkProgressBar(self.stats_frame)
        self.ram_bar.grid(row=1, column=1, padx=10, pady=10, sticky="ew")
        self.ram_bar.set(0)

        # Disk
        self.disk_label = ctk.CTkLabel(self.stats_frame, text="Disque: 0%", width=120)
        self.disk_label.grid(row=2, column=0, padx=10, pady=10)
        self.disk_bar = ctk.CTkProgressBar(self.stats_frame)
        self.disk_bar.grid(row=2, column=1, padx=10, pady=10, sticky="ew")
        self.disk_bar.set(0)

        # --- Actions Frame ---
        self.actions_frame = ctk.CTkFrame(self)
        self.actions_frame.grid(row=2, column=0, padx=20, pady=10, sticky="ew")
        
        self.btn_clean = ctk.CTkButton(self.actions_frame, text="Nettoyer Disque", command=self.action_clean)
        self.btn_clean.grid(row=0, column=0, padx=20, pady=10)

        self.btn_optimize = ctk.CTkButton(self.actions_frame, text="Analyse Mémoire", command=self.action_optimize)
        self.btn_optimize.grid(row=0, column=1, padx=20, pady=10)

        # --- Advice Frame (Diagnostics) ---
        self.advice_frame = ctk.CTkScrollableFrame(self, label_text="Diagnostics & Solutions", height=200)
        self.advice_frame.grid(row=3, column=0, padx=20, pady=10, sticky="nsew")
        
        self.advice_content = ctk.CTkLabel(self.advice_frame, text="Analyse en cours...", justify="left", font=ctk.CTkFont(size=13), wraplength=700)
        self.advice_content.pack(padx=10, pady=10, fill="both")

        # --- Logs ---
        self.log_textbox = ctk.CTkTextbox(self, height=150)
        self.log_textbox.grid(row=4, column=0, padx=20, pady=20, sticky="nsew")
        self.log_textbox.insert("0.0", "Démarrage du monitoring...\n")

        # Lancement du thread de monitoring
        self.running = True
        self.thread = threading.Thread(target=self.update_stats_loop, daemon=True)
        self.thread.start()

    def add_log(self, message):
        timestamp = time.strftime("[%H:%M:%S] ")
        self.log_textbox.insert("end", f"{timestamp}{message}\n")
        self.log_textbox.see("end")

    def action_clean(self):
        self.add_log("Action utilisateur : Nettoyage du disque lancé...")
        count = utils.clean_disk()
        self.add_log(f"Succès : {count} fichiers supprimés/nettoyés.")

    def action_optimize(self):
        self.add_log("Action utilisateur : Analyse des processus gourmands...")
        heavy = utils.optimize_memory()
        if heavy:
            self.add_log(f"Processus lourds détectés : {', '.join(heavy)}")
        else:
            self.add_log("Aucun processus anormalement gourmand détecté.")

    def update_stats_loop(self):
        while self.running:
            try:
                stats = monitor.collect_all()
                self.after(0, lambda s=stats: self.refresh_ui(s))
                
                # Smart Advice (Diagnostics)
                diagnostics = utils.get_smart_advice(stats)
                self.after(0, lambda d=diagnostics: self.update_diagnostics_ui(d))
                
                # Auto-Alerts
                alerts = utils.get_critical_alerts(stats['cpu'], stats['ram'], stats['disk'])
                for alert in alerts:
                    self.after(0, lambda a=alert: self.add_log(f"ALERTE CRITIQUE : {a}"))
                
                reporter.generate_report(stats)
                
            except Exception as e:
                self.after(0, lambda err=e: self.add_log(f"Erreur : {err}"))
            
            time.sleep(10)

    def update_diagnostics_ui(self, diagnostics):
        if not diagnostics:
            self.advice_content.configure(text="✅ Système en bonne santé.\n\nConseil : Pensez à redémarrer votre PC une fois par semaine pour vider totalement la mémoire vive.", text_color="green")
            return

        full_text = ""
        for diag in diagnostics:
            full_text += f"⚠️ ALERTE {diag['type']}\n"
            full_text += f"   ➤ CAUSE : {diag['cause']}\n"
            full_text += f"   ➤ SOLUTION : {diag['solution']}\n\n"
        
        self.advice_content.configure(text=full_text.strip(), text_color=("red", "#ff6666"))

    def refresh_ui(self, stats):
        # CPU
        self.cpu_label.configure(text=f"CPU: {stats['cpu']}%")
        self.cpu_bar.set(stats['cpu'] / 100)
        self.cpu_bar.configure(progress_color="red" if stats['cpu'] > utils.THRESHOLD_CPU else "blue")

        # RAM
        self.ram_label.configure(text=f"RAM: {stats['ram']}%")
        self.ram_bar.set(stats['ram'] / 100)
        self.ram_bar.configure(progress_color="red" if stats['ram'] > utils.THRESHOLD_RAM else "blue")

        # Disk
        self.disk_label.configure(text=f"Disque: {stats['disk']}%")
        self.disk_bar.set(stats['disk'] / 100)
        self.disk_bar.configure(progress_color="red" if stats['disk'] > utils.THRESHOLD_DISK else "blue")

if __name__ == "__main__":
    app = MonitoringApp()
    app.mainloop()
