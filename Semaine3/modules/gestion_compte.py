import os
import pandas as pd
import hashlib
import tkinter as tk
from modules.log import *

def supprimer_user(entrée1_remove,entrée2_remove, fenetre):
    type = 'delete_user'
    username=entrée1_remove.get().strip()
    password=entrée2_remove.get().strip().encode("utf-8")

    user_csv_path = 'data/user.csv'
    df = pd.read_csv(user_csv_path)


    filtered_df = df.loc[df['username'] == username]

    if filtered_df.empty:
        status = "[X] Les informations sont incorrectes."
        label_password = tk.Label(fenetre, text=status, fg="red")
        label_password.place(x=150, y=110)
        add_log(type,username,status)
        return


    salt = bytes.fromhex(filtered_df['salt'].values[0])

    password_combined = password + salt


    password_hashed = hashlib.sha256(password_combined).hexdigest()

    filtered_df = df.loc[~((df['username'] == username) & (df['password'] == password_hashed))]

    if len(filtered_df) < len(df):

        filtered_df.to_csv(user_csv_path, index=False)
        status = f"[✓] Utilisateur {username} supprimé avec succès."
        label_password = tk.Label(fenetre, text=status, fg="green")
        label_password.place(x=150, y=110)
        add_log(type,username,status)

        nom_fichier = f"{username}.csv"
        chemin_fichier = os.path.join('data', nom_fichier)
        if os.path.exists(chemin_fichier):
            os.remove(chemin_fichier)
        return True
    
    else:
        status = "[X] Les informations sont incorrectes."
        label_password = tk.Label(fenetre, text=status, fg="red")
        label_password.place(x=150, y=110)
        add_log(type,username,status)
        return False




def liste_commercants(fenetre):

    user_csv_path = 'data/user.csv'
    df = pd.read_csv(user_csv_path)

    commercants = df['username'].tolist()
    return commercants