import os
import pandas as pd
import hashlib
from modules.connexion import password_compromises
import requests

def modifier_password(username, entrée1_change,entrée2_change,fenetre):
    global password_compromise
    
    old_password = entrée1_change
    nouveau_password = entrée2_change
    
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

        filtered_df = df.loc[df['username'] == username]
        salt = bytes.fromhex(filtered_df['salt'].values[0])
        nouveau_password_combined = nouveau_password.encode("utf-8") + salt
        nouveau_password_hashed = hashlib.sha256(nouveau_password_combined).hexdigest()

        df.loc[df['username'] == username, 'password'] = nouveau_password_hashed

            
        df.to_csv(user_csv_path, index=False)

        password_compromise = password_compromises(nouveau_password)

        return True ,password_compromise



def haveibeenpwnd_password():
    csv_path = 'password/password_verif.csv'
    df = pd.read_csv(csv_path)
    
    print("2) Vérifier votre mot de passe")
    password = input("Mettre votre mot de passe :").encode("utf-8")
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
            print(f"Votre mot de passe a été compromis {pwnded_password} fois.\n")
            input("Appuyez sur une touche pour continuer...")

        else:
            print("Votre mot de passe n'a pas été compromis.\n")
            input("Appuyez sur une touche pour continuer...")

    else:
        print("Erreur lors de la vérification du mot de passe.\n")
        input("Appuyez sur une touche pour continuer...")







