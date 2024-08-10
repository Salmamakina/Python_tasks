import tkinter as tk
import random

def lancer_de(n_faces):
    return random.randint(1, n_faces)

def afficher_resultats():
    try:
        n_faces = int(entry_faces.get())
        n_lancers = int(entry_lancers.get())
        
        if n_faces < 1 or n_lancers < 1:
            resultat_label.config(text="Les valeurs doivent être des entiers positifs.")
            return
        
        resultats = [lancer_de(n_faces) for _ in range(n_lancers)]
        resultats_str = "\n".join(f"Lancer {i + 1} : {resultat}" for i, resultat in enumerate(resultats))
        resultat_label.config(text=f"Résultats des lancers :\n{resultats_str}")
    
    except ValueError:
        resultat_label.config(text="Veuillez entrer des nombres valides.")
root = tk.Tk()
root.title("Simulateur de Lancer de Dés")

# Création des widgets
tk.Label(root, text="Nombre de faces du dé :").pack()
entry_faces = tk.Entry(root)
entry_faces.pack()

tk.Label(root, text="Nombre de lancers :").pack()
entry_lancers = tk.Entry(root)
entry_lancers.pack()

tk.Button(root, text="Lancer les dés", command=afficher_resultats).pack()

resultat_label = tk.Label(root, text="")
resultat_label.pack()

root.mainloop()
   
