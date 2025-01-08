import os
import pandas as pd
import hashlib
import tkinter as tk


def supprimer_user(entrée1_remove,entrée2_remove, fenetre):
    informations_good = False
    username=entrée1_remove.get().strip()
    password=entrée2_remove.get().strip().encode("utf-8")

    user_csv_path = 'data/user.csv'
    df = pd.read_csv(user_csv_path)


    filtered_df = df.loc[df['username'] == username]

    if filtered_df.empty:
        password_status = "[X] Les informations sont incorrectes."
        label_password = tk.Label(fenetre, text=password_status, fg="red")
        label_password.place(x=150, y=110)
        return


    salt = bytes.fromhex(filtered_df['salt'].values[0])

    password_combined = password + salt


    password_hashed = hashlib.sha256(password_combined).hexdigest()

    filtered_df = df.loc[~((df['username'] == username) & (df['password'] == password_hashed))]

    if len(filtered_df) < len(df):

        filtered_df.to_csv(user_csv_path, index=False)
        password_status = f"[✓] Utilisateur {username} supprimé avec succès."
        label_password = tk.Label(fenetre, text=password_status, fg="green")
        label_password.place(x=150, y=110)

        nom_fichier = f"{username}.csv"
        chemin_fichier = os.path.join('data', nom_fichier)
        if os.path.exists(chemin_fichier):
            os.remove(chemin_fichier)
            
    
    else:
        password_status = "[X] Les informations sont incorrectes."
        label_password = tk.Label(fenetre, text=password_status, fg="red")
        label_password.place(x=150, y=110)





def liste_commercants(fenetre):

    user_csv_path = 'data/user.csv'
    df = pd.read_csv(user_csv_path)

    commercants = df['username'].tolist()
    return commercants