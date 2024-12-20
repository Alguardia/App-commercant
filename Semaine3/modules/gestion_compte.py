import os
import pandas as pd
import hashlib


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

