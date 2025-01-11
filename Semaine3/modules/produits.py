import os
from tabulate import tabulate
import csv
import pandas as pd
import tkinter as tk

def lire_liste(chemin_fichier):

    df = pd.read_csv(chemin_fichier)

    produit = df.values.tolist()
    return produit



def ajouter_produit(chemin_fichier,entrée1, entrée2, entrée3, fenetre):
    
    inputusernom = entrée1.get()
    inputuserprix = entrée2.get()
    inputuserquantite = entrée3.get()

  
    if not inputusernom or not inputuserprix or not inputuserquantite:
        status = "[X] Erreur : Veuillez remplir tous les champs"
        label_produit = tk.Label(fenetre, text=status, fg="green")
        label_produit.place(x=150, y=110)
        return False

    produit_data = [[inputusernom.lower(), inputuserprix, inputuserquantite]]


    df_existing = pd.read_csv(chemin_fichier)

    df_new = pd.DataFrame(produit_data, columns=['NOM', 'PRIX', 'QUANTITE'])

    df_combined = pd.concat([df_existing, df_new], ignore_index=True)

    df_combined.to_csv(chemin_fichier, index=False)
 

    status = "[✓] Produit ajouté avec succès"
    label_produit = tk.Label(fenetre, text=status, fg="green")
    label_produit.place(x=150, y=110)

    return True



def supprimer_produit(chemin_fichier, entrée1_remove, fenetre):
    input_recherche = entrée1_remove.get()

    df = pd.read_csv(chemin_fichier)

    filtered_df = df[~df['NOM'].str.lower().eq(input_recherche.lower())]

    if len(filtered_df) < len(df):
        filtered_df.to_csv(chemin_fichier, index=False)
        status = "[✓] Produit supprimé avec succès"
        label_produit = tk.Label(fenetre, text=status, fg="green", wraplength=170 )
        label_produit.place(x=150, y=110)
        return True
    else:
        status = f"[X] Aucun élement trouvé pour {input_recherche}"
        label_produit = tk.Label(fenetre, text=status, fg="red", wraplength=160)
        label_produit.place(x=150, y=110)
        return False





def rechercher_produit(chemin_fichier, entrée1_remove, fenetre):


    input_recherche= entrée1_remove.get()

    df = pd.read_csv(chemin_fichier)

    filtered_df = df.loc[(df['NOM'] == input_recherche.lower())]
    
    if filtered_df.empty: 
        status = f"[X] Aucun élement trouvé pour {input_recherche}"
        label_produit = tk.Label(fenetre, text=status, fg="red")
        label_produit.place(x=150, y=110)
        return False
    
    else: 
        nom = filtered_df.iloc[0]['NOM']
        prix = filtered_df.iloc[0]['PRIX']
        quantite = filtered_df.iloc[0]['QUANTITE']
        
        status = f"Nom: {nom} | Prix: {prix} | Quantité: {quantite}"
        label_produit = tk.Label(fenetre, text=status, fg="green")
        label_produit.place(x=150, y=110)
        return True

        


def trier_produit_nom(chemin_fichier):

    df = pd.read_csv(chemin_fichier)
    df_sorted = df.sort_values(by="NOM")
    produit = df_sorted.values.tolist()
    return produit
	

def trier_produit_prix(chemin_fichier):
    df = pd.read_csv(chemin_fichier)
    df_sorted = df.sort_values(by="PRIX")
    produit = df_sorted.values.tolist()
    return produit

def trier_produit_quantite(chemin_fichier):

    df = pd.read_csv(chemin_fichier)
    df_sorted = df.sort_values(by="QUANTITE")
    produit = df_sorted.values.tolist()
    return produit