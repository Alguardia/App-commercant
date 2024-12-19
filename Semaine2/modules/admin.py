import pandas as pd
import os
from tabulate import tabulate
import hashlib


def verifier_admin(username, password):

    df = pd.read_csv('data/user.csv')
    if username == "root":
        filtered_df = df.loc[df['username'] == username]

    
        salt = bytes.fromhex(filtered_df['salt'].values[0])
        password_combined = password.encode("utf-8") + salt
        password_hashed = hashlib.sha256(password_combined).hexdigest()

        if password_hashed == filtered_df['password'].values[0]:
            return True
        else:
            return False
    else :
        print("Aucun utilisateur trouvé avec ce nom et ce mot de passe.")
        input("Appuyez sur une touche pour continuer...")



def login_admin(username,password):

    if verifier_admin(username, password):
        print("Connexion réussie !")
        return True
    else:
        return False


def admin_panel():

    nom_fichier = "password_verif.csv"
    chemin_fichier = os.path.join('password', nom_fichier)
    df = pd.read_csv(chemin_fichier)

    produit = df.values.tolist()

    print(tabulate(produit, headers=df.columns, tablefmt="rounded_outline"))
    input("")

