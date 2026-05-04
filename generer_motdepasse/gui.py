import customtkinter as ctk
import pyperclip
from generator import generer_mot_de_passe
from checker import verifier_complexite

# Configuration du thème
ctk.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

class PasswordApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("pwd - Générateur de Mots de Passe")
        self.geometry("500x600")

        # Configuration de la grille
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure((0, 1), weight=1)

        # --- Section Génération ---
        self.gen_frame = ctk.CTkFrame(self)
        self.gen_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        self.gen_frame.grid_columnconfigure(0, weight=1)

        self.label_gen = ctk.CTkLabel(self.gen_frame, text="Générateur de Mot de Passe", font=ctk.CTkFont(size=20, weight="bold"))
        self.label_gen.grid(row=0, column=0, padx=20, pady=10)

        self.longueur_label = ctk.CTkLabel(self.gen_frame, text="Longueur: 12")
        self.longueur_label.grid(row=1, column=0, padx=20, pady=5)

        self.slider = ctk.CTkSlider(self.gen_frame, from_=8, to=20, number_of_steps=12, command=self.update_slider_label)
        self.slider.set(12)
        self.slider.grid(row=2, column=0, padx=20, pady=10, sticky="ew")

        self.btn_generer = ctk.CTkButton(self.gen_frame, text="Générer", command=self.generer_action)
        self.btn_generer.grid(row=3, column=0, padx=20, pady=10)

        self.entry_mdp = ctk.CTkEntry(self.gen_frame, placeholder_text="Mot de passe généré", width=300, justify="center")
        self.entry_mdp.grid(row=4, column=0, padx=20, pady=10)

        self.btn_copier = ctk.CTkButton(self.gen_frame, text="Copier", width=100, fg_color="transparent", border_width=2, command=self.copier_action)
        self.btn_copier.grid(row=5, column=0, padx=20, pady=5)

        # --- Section Vérification ---
        self.check_frame = ctk.CTkFrame(self)
        self.check_frame.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")
        self.check_frame.grid_columnconfigure(0, weight=1)

        self.label_check = ctk.CTkLabel(self.check_frame, text="Testeur de Sécurité", font=ctk.CTkFont(size=20, weight="bold"))
        self.label_check.grid(row=0, column=0, padx=20, pady=10)

        self.entry_test = ctk.CTkEntry(self.check_frame, placeholder_text="Entrez un mot de passe à tester", width=300)
        self.entry_test.grid(row=1, column=0, padx=20, pady=10)
        self.entry_test.bind("<KeyRelease>", self.verifier_action)

        self.lbl_resultat = ctk.CTkLabel(self.check_frame, text="Force : -", font=ctk.CTkFont(weight="bold"))
        self.lbl_resultat.grid(row=2, column=0, padx=20, pady=5)

        self.txt_feedback = ctk.CTkTextbox(self.check_frame, height=100)
        self.txt_feedback.grid(row=3, column=0, padx=20, pady=10, sticky="nsew")

    def update_slider_label(self, value):
        self.longueur_label.configure(text=f"Longueur: {int(value)}")

    def generer_action(self):
        longueur = int(self.slider.get())
        mdp = generer_mot_de_passe(longueur)
        self.entry_mdp.delete(0, "end")
        self.entry_mdp.insert(0, mdp)
        
        # Lancer la vérification sur le mdp généré
        self.entry_test.delete(0, "end")
        self.entry_test.insert(0, mdp)
        self.verifier_action()

    def copier_action(self):
        mdp = self.entry_mdp.get()
        if mdp:
            pyperclip.copy(mdp)
            self.btn_copier.configure(text="Copié !")
            self.after(2000, lambda: self.btn_copier.configure(text="Copier"))

    def verifier_action(self, event=None):
        mdp = self.entry_test.get()
        if not mdp:
            self.lbl_resultat.configure(text="Force : -", text_color="gray")
            self.txt_feedback.delete("1.0", "end")
            return

        niveau, conseils = verifier_complexite(mdp)
        
        # Couleurs selon le niveau
        color = "red" if niveau == "FAIBLE" else "orange" if niveau == "MOYEN" else "green"
        self.lbl_resultat.configure(text=f"Force : {niveau}", text_color=color)

        self.txt_feedback.delete("1.0", "end")
        if conseils:
            self.txt_feedback.insert("end", "Conseils :\n" + "\n".join(conseils))
        else:
            self.txt_feedback.insert("end", "Mot de passe excellent !")

if __name__ == "__main__":
    app = PasswordApp()
    app.mainloop()
