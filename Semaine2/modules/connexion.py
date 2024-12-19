import os
import pandas as pd
import hashlib


def generate_salt():
    salt = os.urandom(16)
    return salt
    

def register():
    username = input("Mettre votre nom : ")
    salt = generate_salt()
    password = input("Mettre votre mot de passe : ").encode("utf-8") + salt

    nom_fichier = f"{username}.csv"
    chemin_fichier = os.path.join('data', nom_fichier)

    user_csv_path = 'data/user.csv'
    if os.path.exists(user_csv_path):
        df = pd.read_csv(user_csv_path)

        if username in df['username'].values:
            print("Erreur : Le nom d'utilisateur existe déjà.")
            input("")
            return
    else:
        df = pd.DataFrame(columns=['username', 'password', 'salt'])

    user_data = [[username, hashlib.sha256(password).hexdigest(), salt.hex()]]
    df_new = pd.DataFrame(user_data, columns=['username', 'password', 'salt'])
    df_combined = pd.concat([df, df_new], ignore_index=True)
    df_combined.to_csv(user_csv_path, index=False)

    print(f"Utilisateur {username} enregistré avec succès !")

    df_produit = pd.DataFrame(columns=['NOM', 'PRIX', 'QUANTITE'])
    df_produit.to_csv(chemin_fichier, index=False)

    input("Appuyez sur une touche pour continuer...")




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



def login(username,password):

    if verifier_utilisateur(username, password):
        print("Connexion réussie !")
        return True
    else:
        return False



def password_compromises(password):
    password_is_compromise = False

    nom_fichier = "hashed_passwords.csv"
    chemin_fichier = os.path.join('password', nom_fichier)
    df = pd.read_csv(chemin_fichier)
    df['Hashed'] = df['Hashed'].str.strip()
    password_hash = hashlib.sha256(password.encode('utf-8')).hexdigest()


    if password_hash in df['Hashed'].values:
        print(f"Le mot de passe est compromis. Hash trouvé: {password_hash}")
        password_is_compromise = True
    else:
        print(f"Le mot de passe n'est pas compromis. Hash non trouvé.")
    
    return password_is_compromise