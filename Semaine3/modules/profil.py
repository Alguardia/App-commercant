import os
import pandas as pd
import hashlib
from modules.connexion import haveibeenpwnd_password
import requests
import tkinter as tk
from modules.log import *


def modifier_password(username, entrée1_change,entrée2_change,fenetre):
    type = 'change_password'
    
    old_password = entrée1_change.get()
    password = entrée2_change.get()
    

    user_csv_path = 'data/user.csv'
    df = pd.read_csv(user_csv_path)


    filtered_df = df.loc[df['username'] == username]

    if filtered_df.empty:
        return False

    salt = bytes.fromhex(filtered_df['salt'].values[0])
    password_combined = old_password.encode("utf-8") + salt
    password_hashed = hashlib.sha256(password_combined).hexdigest()

    if password_hashed == filtered_df['password'].values[0]:
        verif=True
    else:
        verif=False

    if verif:

        status = f"[✓] Mot de passe changé."
        label_password = tk.Label(fenetre, text=status, fg="green")
        label_password.place(x=150, y=110)
        add_log(type,username,status)
        filtered_df = df.loc[df['username'] == username]
        salt = bytes.fromhex(filtered_df['salt'].values[0])
        nouveau_password_combined = password.encode("utf-8") + salt
        nouveau_password_hashed = hashlib.sha256(nouveau_password_combined).hexdigest()

        df.loc[df['username'] == username, 'password'] = nouveau_password_hashed

            
        df.to_csv(user_csv_path, index=False)

        

        return True
    else :
        status = "[X] Mauvais mot de passe."
        label_password = tk.Label(fenetre, text=status, fg="red")
        label_password.place(x=150, y=110)
        add_log(type,username,status)



def haveibeenpwnd_password_check(entrée_check,fenetre,username):
    
   
    csv_path = 'password/log.csv'
    df = pd.read_csv(csv_path)
    type = 'check_password'
    
    password = entrée_check.get()
    password = password.encode("utf-8")
    password_hashed = hashlib.sha1(password).hexdigest()
    char = password_hashed[:5]

    response = requests.get(f"https://api.pwnedpasswords.com/range/{char}")
    

    if response.status_code == 200:

        lines = response.text.splitlines()
        

        suffix = password_hashed[5:].upper()

        for line in lines:
            hash_suffix, count = line.split(':')
            if hash_suffix == suffix:
                pwnded_password = int(count)
                break
        else:
            pwnded_password = 0


        if pwnded_password > 0:
            status = f"[X] Le mot de passe est compromis {pwnded_password} fois."
            label_password = tk.Label(fenetre, text=status, fg="red", wraplength=210)
            label_password.place(x=150, y=90)
            add_log(type,username,status)
            return

        else:
            status = f"[✓] Votre mot de passe n'a pas été compromis."
            label_password = tk.Label(fenetre, text=status, fg="green" ,wraplength=230)
            label_password.place(x=150, y=90)
            add_log(type,username,status)
            return
    else:
        status = f"[!] Erreur lors de la vérification du mot de passe."
        label_password = tk.Label(fenetre, text=status, fg="yellow" ,wraplength=230)
        label_password.place(x=150, y=90)
        add_log(type,username,status)
        return 
