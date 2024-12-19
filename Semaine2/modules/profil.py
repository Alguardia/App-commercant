import os
import pandas as pd
import hashlib
import pwnedpasswords
from modules.connexion import password_compromises

def modifier_password(username, password):
    global password_compromise
    print("1) Modifier votre mot de passe")
    nouveau_password = input("Entrez votre nouveau mot de passe : ")

    user_csv_path = 'data/user.csv'
    df = pd.read_csv(user_csv_path)


    filtered_df = df.loc[df['username'] == username]
    salt = bytes.fromhex(filtered_df['salt'].values[0])
    nouveau_password_combined = nouveau_password.encode("utf-8") + salt
    nouveau_password_hashed = hashlib.sha256(nouveau_password_combined).hexdigest()

    df.loc[df['username'] == username, 'password'] = nouveau_password_hashed

        
    df.to_csv(user_csv_path, index=False)

    password_compromise = password_compromises(nouveau_password)

    return password_compromise

def haveibeenpwnd_password():
    csv_path = 'password/password_verif.csv'
    df = pd.read_csv(csv_path)
    
    print("2) Vérifier votre mot de passe")
    password = input("Mettre votre mot de passe :")

    pwnded_password = pwnedpasswords.check(password)

    new_entry = pd.DataFrame({'password': [password], 'number': [pwnded_password]})

    
    df = pd.concat([df, new_entry], ignore_index=True)

   
    df.to_csv(csv_path, index=False)

    print(f"Votre mot de passe a été compromis : {pwnded_password}\n")
    input("Appuyez sur une touche pour continuer...")



