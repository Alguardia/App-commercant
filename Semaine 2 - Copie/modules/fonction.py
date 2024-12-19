import os
from tabulate import tabulate
import csv
import pandas as pd


def lire_liste(chemin_fichier):

    df = pd.read_csv(chemin_fichier)

    produit = df.values.tolist()

    print(tabulate(produit, headers=df.columns, tablefmt="grid"))



def ajouter_produit(chemin_fichier):
    print("Ajouter un produit :")
    inputusernom = input("Nom du produit : ")
    inputuserprix = input("Prix du produit : ")
    inputuserquantite = input("Quantité du produit : ")

  
    if not inputusernom or not inputuserprix or not inputuserquantite:
        print("Erreur, le champ est vide")
        return

    produit_data = [[inputusernom.lower(), inputuserprix, inputuserquantite]]



    df_existing = pd.read_csv(chemin_fichier)

    df_new = pd.DataFrame(produit_data, columns=['NOM', 'PRIX', 'QUANTITE'])

    df_combined = pd.concat([df_existing, df_new], ignore_index=True)

    df_combined.to_csv(chemin_fichier, index=False)
 

    print(f"Produit {inputusernom} ajouté avec succès !")



def supprimer_produit(chemin_fichier):
    input_recherche = input("Entrez le nom du produit à supprimer : ")

    df = pd.read_csv(chemin_fichier)

    filtered_df = df.loc[df['NOM'].str.lower().str.contains(input_recherche.lower())]

    if len(filtered_df) < len(df):
        filtered_df.to_csv(chemin_fichier, index=False)
        print(f"Produit '{input_recherche}' supprimé avec succès.")
    else:
        print(f"Aucun produit trouvé avec le nom '{input_recherche}'.")



def rechercher_produit(chemin_fichier):

    os.system("cls")
    print("1) Recherche séquentielle : ")
    input_recherche=str(input("produit a rechercher : "))
    df = pd.read_csv(chemin_fichier)

    filtered_df = df.loc[(df['NOM'] == input_recherche.lower())]

    if filtered_df.empty: 
        print(f"Le produit '{input_recherche}' n'a pas été trouvé.")
        return False
    
    else: 
        print("Éléments trouvés :") 
        print(filtered_df)
        return True

        


def trier_produit(chemin_fichier):
    i=0
    print("1) Tri par sélection par nom")
    print("2) Tri à bulles par prix ")
    print("3) Tri rapide par quantité")
    answer = int(input("Choisir une option : "))

    if answer == 1:
        os.system("cls")
        print("1) Tri par nom : ")
    
        df = pd.read_csv(chemin_fichier)
        df_sorted = df.sort_values(by="NOM")
        print(df_sorted)
	


    if answer == 2:
        os.system("cls")
        print("2) Tri par prix : ")
    

        df = pd.read_csv(chemin_fichier)
        df_sorted = df.sort_values(by="PRIX")
        print(df_sorted)
	

    if answer == 3:
        os.system("cls")
        print("3) Tri par quantité :")
        liste = []

        df = pd.read_csv(chemin_fichier)
        df_sorted = df.sort_values(by="QUANTITE")
        print(df_sorted)