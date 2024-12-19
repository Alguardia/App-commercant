import os
import pandas as pd
import hashlib

def password_hash():
    chemin_fichier = os.path.join('password', 'rockyou.txt')
    output_csv = os.path.join('password', 'hashed_passwords.csv')


    with open(chemin_fichier, 'r', encoding='latin-1') as fichier:
        lignes = fichier.readlines()

    hashed_passwords = []
    for ligne in lignes:
        ligne = ligne.strip()
        hashed_password = hashlib.sha256(ligne.encode('utf-8')).hexdigest()
        hashed_passwords.append([hashed_password])


    df = pd.DataFrame(hashed_passwords, columns=['Hashed'])

    df.to_csv(output_csv, index=False)

    print(f"Les mots de passe hachés ont été enregistrés dans {output_csv}")


password_hash()
