import os
import pandas as pd
import hashlib
import requests 
import tkinter as tk


def generate_salt():
    salt = os.urandom(16)
    return salt
    

def register(entrée1_register,entrée2_register, fenetre):
    password_check=False
    username_check=False

    username=entrée1_register.get()
    
    salt = generate_salt()
    password=entrée2_register.get()

    password_encode=password.encode("utf-8")

    if haveibeenpwnd_password(password_encode):
        
        password_status = "[X] Changer de mot de passe."
        label_password = tk.Label(fenetre, text=password_status, fg="red")
        label_password.place(x=150, y=110)
        return False
        
    else :
        password = password_encode  + salt

        nom_fichier = f"{username}.csv"
        chemin_fichier = os.path.join('data', nom_fichier)

        user_csv_path = 'data/user.csv'
        if os.path.exists(user_csv_path):
            df = pd.read_csv(user_csv_path)

            if username in df['username'].values:
                username_status = "[X] Cette utilisateur existe déjà."
                label_username = tk.Label(fenetre, text=username_status, fg="red")
                label_username.place(x=150, y=110)
                return False
        else:
            df = pd.DataFrame(columns=['username', 'password', 'salt'])

        user_data = [[username, hashlib.sha256(password).hexdigest(), salt.hex()]]
        df_new = pd.DataFrame(user_data, columns=['username', 'password', 'salt'])
        df_combined = pd.concat([df, df_new], ignore_index=True)
        df_combined.to_csv(user_csv_path, index=False)

        password_status = f"[✓] Utilisateur {username} enregistré avec succès."
        label_password = tk.Label(fenetre, text=password_status, fg="green")
        label_password.place(x=150, y=110)

        df_produit = pd.DataFrame(columns=['NOM', 'PRIX', 'QUANTITE'])
        df_produit.to_csv(chemin_fichier, index=False)

        return True




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


def login(entrée1,entrée2,fenetre):
    username=entrée1.get()
    password=entrée2.get()
    if verifier_utilisateur(username, password):
        status = "[✓] Connexion réusite."
        label_username = tk.Label(fenetre, text=status, fg="green")
        label_username.place(x=150, y=110)
        return True
    else:
        status = "[X] Connexion refusée."
        label_username = tk.Label(fenetre, text=status, fg="red")
        label_username.place(x=150, y=110)
        return False



def password_compromises(password):
    password_is_compromise = False

    nom_fichier = "hashed_passwords.csv"
    chemin_fichier = os.path.join('password', nom_fichier)
    df = pd.read_csv(chemin_fichier)
    df['Hashed'] = df['Hashed'].str.strip()
    password_hash = hashlib.sha256(password.encode('utf-8')).hexdigest()


    if password_hash in df['Hashed'].values:
        print(f". Hash trouvé: {password_hash}")
        password_is_compromise = True
    else:
        print(f"Le mot de passe n'est pas compromis. Hash non trouvé.")
    
    return password_is_compromise




def haveibeenpwnd_password(password):
    csv_path = 'password/password_verif.csv'
    df = pd.read_csv(csv_path)
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
            return True
        else:
            return False
    else:
        print("Erreur lors de la vérification du mot de passe.\n")
        input("Appuyez sur une touche pour continuer...")

        return False