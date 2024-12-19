import os
import csv
from tabulate import tabulate
import pandas as pd
import hashlib
from menu import *


def generate_salt():
    salt = os.urandom(16)
    return salt
    

def register():
    username = input("Mettre votre nom : ")
    salt = generate_salt()
    password = input("Mettre votre mot de passe : ").encode("utf-8") + salt

    nom_fichier = f"{username}.csv"
    chemin_fichier = os.path.join('data', nom_fichier)

    user_csv_path = 'data/user.csv'
    if os.path.exists(user_csv_path):
        df = pd.read_csv(user_csv_path)

        if username in df['username'].values:
            print("Erreur : Le nom d'utilisateur existe déjà.")
            input("")
            return
    else:
        df = pd.DataFrame(columns=['username', 'password', 'salt'])

    user_data = [[username, hashlib.sha256(password).hexdigest(), salt.hex()]]
    df_new = pd.DataFrame(user_data, columns=['username', 'password', 'salt'])
    df_combined = pd.concat([df, df_new], ignore_index=True)
    df_combined.to_csv(user_csv_path, index=False)

    print(f"Utilisateur {username} enregistré avec succès !")

    df_produit = pd.DataFrame(columns=['NOM', 'PRIX', 'QUANTITE'])
    df_produit.to_csv(chemin_fichier, index=False)

    input("Appuyez sur une touche pour continuer...")




def verifier_utilisateur(username, password):

    df = pd.read_csv('data/user.csv')

    filtered_df = df.loc[df['username'] == username]

    if filtered_df.empty:
        return False

    salt = bytes.fromhex(filtered_df['salt'].values[0])
    password_combined = password.encode("utf-8") + salt
    password_hashed = hashlib.sha256(password_combined).hexdigest()

    if password_hashed == filtered_df['password'].values[0]:
        return True
    else:
        return False




def login():
    global is_logged_in 
    username = input("Mettre votre nom : ")
    password = input("Mettre votre mot de passe : ")

    if verifier_utilisateur(username, password):
        
        print("Connexion réussie !")
        
        is_logged()
    else:
        print("Échec de la connexion.")
        return False



def supprimer_user():
    username = input("Entrez votre nom d'utilisateur : ").strip()
    password = input("Entrez votre mot de passe : ").strip().encode("utf-8")

    user_csv_path = 'data/user.csv'
    df = pd.read_csv(user_csv_path)


    filtered_df = df.loc[df['username'] == username]

    if filtered_df.empty:
        print("Aucun utilisateur trouvé avec ce nom.")
        input("Appuyez sur une touche pour continuer...")
        return


    salt = bytes.fromhex(filtered_df['salt'].values[0])

    password_combined = password + salt


    password_hashed = hashlib.sha256(password_combined).hexdigest()

    filtered_df = df.loc[~((df['username'] == username) & (df['password'] == password_hashed))]

    if len(filtered_df) < len(df):

        filtered_df.to_csv(user_csv_path, index=False)
        print(f"Utilisateur {username} supprimé avec succès.")


        nom_fichier = f"{username}.csv"
        chemin_fichier = os.path.join('data', nom_fichier)
        if os.path.exists(chemin_fichier):
            os.remove(chemin_fichier)
            print(f"Le fichier CSV '{nom_fichier}' a été supprimé.")
    else:
        print("Aucun utilisateur trouvé avec ce nom et ce mot de passe.")

    input("Appuyez sur une touche pour continuer...")


def liste_commercants():

    user_csv_path = 'data/user.csv'
    df = pd.read_csv(user_csv_path)


    commercants = df['username'].tolist()
    print("Liste des commerçants :")
    for commercant in commercants:
        print(f"- {commercant}")

    input("Appuyez sur une touche pour continuer...")

