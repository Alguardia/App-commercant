import os
import pandas as pd
import hashlib
from modules.connexion import password_compromises
import requests
import tkinter as tk

def modifier_password(username, entrée1_change,entrée2_change,fenetre):
    global password_compromise
    
    username = username.get()
    old_password = entrée1_change.get()
    nouveau_password = entrée2_change.get()
    

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

        password_status = f"[✓] Mot de passe changé."
        label_password = tk.Label(fenetre, text=password_status, fg="green")
        label_password.place(x=150, y=110)

        filtered_df = df.loc[df['username'] == username]
        salt = bytes.fromhex(filtered_df['salt'].values[0])
        nouveau_password_combined = nouveau_password.encode("utf-8") + salt
        nouveau_password_hashed = hashlib.sha256(nouveau_password_combined).hexdigest()

        df.loc[df['username'] == username, 'password'] = nouveau_password_hashed

            
        df.to_csv(user_csv_path, index=False)

        password_compromise = password_compromises(nouveau_password)

        return True ,password_compromise
    else :
        password_status = "[X] Mauvais mot de passe."
        label_password = tk.Label(fenetre, text=password_status, fg="red")
        label_password.place(x=150, y=110)



def haveibeenpwnd_password(entrée_check,fenetre):
    csv_path = 'password/password_verif.csv'
    df = pd.read_csv(csv_path)
    
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

        new_entry = pd.DataFrame({'password': [password.decode('utf-8')], 'number': [pwnded_password]})
        df = pd.concat([df, new_entry], ignore_index=True)
        df.to_csv(csv_path, index=False)

        if pwnded_password > 0:
            password_status = f"[X] Votre mot de passe est compromis {pwnded_password} fois."
            label_password = tk.Label(fenetre, text=password_status, fg="red", wraplength=230)
            label_password.place(x=150, y=90)

        else:
            password_status = f"[✓] Votre mot de passe n'a pas été compromis."
            label_password = tk.Label(fenetre, text=password_status, fg="green")
            label_password.place(x=150, y=90)

    else:
        password_status = f"[!] Erreur lors de la vérification du mot de passe."
        label_password = tk.Label(fenetre, text=password_status, fg="yellow")
        label_password.place(x=150, y=90)
