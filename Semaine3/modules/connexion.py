import os
import pandas as pd
import hashlib
import requests 
import tkinter as tk
from tkinter import *
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from modules.log import *
import random

def generate_salt():
    salt = os.urandom(16)
    return salt
 

def verif_email(entrée1_mail, code,fenetre):
    try:
        code_email = int(entrée1_mail.get())
        if code_email == code:
            save_user(fenetre)
            return True
        else:
            status = f"[X] Code reçu par mail invalide"
            label_password = tk.Label(fenetre, text=status, fg="red")
            label_password.pack(pady=(20, 0), anchor='center')
            add_log("register", username, status)
            return False
    except ValueError:
        status = "[X] Entrée invalide, veuillez entrer un code numérique."
        label_password = tk.Label(fenetre, text=status, fg="red")
        label_password.pack(pady=(20, 0), anchor='center') 
        add_log("register", username, status)
        return False


def save_user(fenetre):
    user_data = [[username, hashlib.sha256(password).hexdigest(), salt.hex(),email]]
    df_new = pd.DataFrame(user_data, columns=['username', 'password', 'salt','email'])
    df_combined = pd.concat([df, df_new], ignore_index=True)
    df_combined.to_csv(user_csv_path, index=False)

    status = f"[✓] Utilisateur {username} enregistré avec succès."
    label_password = tk.Label(fenetre, text=status, fg="green")
    label_password.pack(pady=(20, 0), anchor='center')
    add_log("register",username,status)

    df_produit = pd.DataFrame(columns=['NOM', 'PRIX', 'QUANTITE'])
    df_produit.to_csv(chemin_fichier, index=False)
    
    return True



def register(entrée1_register,entrée2_register, entrée3_register , fenetre):
    global username,password,salt,email,chemin_fichier,user_csv_path,df
    verif = False
    type = 'register'

    username=entrée1_register.get()
    
    salt = generate_salt()
    password=entrée2_register.get()
    email=entrée3_register.get()
    password_encode=password.encode("utf-8")

    if password_compromises(password):
        
        status = "[X] Changer de mot de passe."
        label_password = tk.Label(fenetre, text=status, fg="red")
        label_password.place(x=150, y=110)
        add_log(type,username,status)
        return False
        
    else :
        password = password_encode  + salt

        nom_fichier = f"{username}.csv"
        chemin_fichier = os.path.join('data', nom_fichier)

        user_csv_path = 'data/user.csv'
        if os.path.exists(user_csv_path):
            df = pd.read_csv(user_csv_path)

            if username in df['username'].values:
                status = "[X] Cette utilisateur existe déjà."
                label_username = tk.Label(fenetre, text=status, fg="red")
                label_username.place(x=150, y=110)
                add_log(type,username,status)
                return False
            
        else:
            df = pd.DataFrame(columns=['username', 'password', 'salt','email'])


        if email in df['email'].values:
                status = "[X] Cette email existe déjà."
                label_username = tk.Label(fenetre, text=status, fg="red")
                label_username.place(x=150, y=110)
                add_log(type,username,status)
                return False




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
    type = 'login'
    username=entrée1.get()
    password=entrée2.get()
    if verifier_utilisateur(username, password):
        
        status = "[✓] Connexion réusite."
        label_username = tk.Label(fenetre, text=status, fg="green")
        label_username.place(x=150, y=110)

        add_log(type,username,status)

        return True
    else:
        status = "[X] Connexion refusée."
        label_username = tk.Label(fenetre, text=status, fg="red")
        label_username.place(x=150, y=110)

        add_log(type,username,status)

        return False



def password_compromises(password):
    password_is_compromise = False

    nom_fichier = "hashed_passwords.csv"
    chemin_fichier = os.path.join('security', nom_fichier)
    df = pd.read_csv(chemin_fichier)
    df['Hashed'] = df['Hashed'].str.strip()
    password_hash = hashlib.sha256(password.encode('utf-8')).hexdigest()


    if password_hash in df['Hashed'].values:
        password_is_compromise = True


    
    return password_is_compromise




def haveibeenpwnd_password(password):
    password_is_compromise = False
    password_encode=password.encode("utf-8")
    
    
    password_hashed = hashlib.sha1(password_encode).hexdigest()
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
            password_is_compromise = True
            return password_is_compromise
        else:
            return False
    else:
        print("Erreur lors de la vérification du mot de passe.\n")
        input("Appuyez sur une touche pour continuer...")

        return False
    
def envoyer_email(email,type,code):

    serveur = 'smtp.gmail.com'
    port = 465
    email_expediteur = 't84089972@gmail.com'
    mdp_expediteur = 'wkibkccwhvllbzsy'
    msg = MIMEMultipart()
    msg['From'] = 'Support App'
    msg['To'] = email
    texte_message = ""

    if type=='check_register' :
        msg['Subject'] = "Confirmation d'email"
        texte_message = f'''
        Bonjour,

        Merci de vous être inscrit sur notre application. Pour compléter la création de votre compte, veuillez utiliser le code de vérification ci-dessous :

        Code de vérification : {code}

        Si vous n'avez pas demandé cette vérification, veuillez ignorer cet email.

        Cordialement,
        L'équipe Support App
        '''

    if type=='login' :
        msg['Subject'] = "Alerte : Mot de passe compromis"
        texte_message = f'''
        Bonjour,

        Nous avons détecté que votre mot de passe pour notre application a été compromis. Par mesure de sécurité, nous vous recommandons de le changer immédiatement.

        Pour votre sécurité, nous vous conseillons de choisir un mot de passe unique et robuste.

        Si vous n'avez pas effectué cette modification ou si vous avez des questions, veuillez nous contacter immédiatement.

        Cordialement,
        L'équipe Support App
        '''
    if type == 'password_changed' :
        msg['Subject'] = "Notification de changement de mot de passe"
        texte_message = f'''
        Bonjour,

        Nous vous informons que votre mot de passe a été modifié avec succès. Si vous avez effectué cette modification, vous pouvez ignorer cet email.

        Si vous n'êtes pas à l'origine de ce changement ou si vous souhaitez réinitialiser votre mot de passe, veuillez vous rendre dans la section "Gestion de compte", puis cliquez sur "Récupération de compte" pour récupérer l'accès à votre compte.

        Si vous avez des questions ou si vous avez besoin d'assistance supplémentaire, n'hésitez pas à nous contacter.

        Cordialement,
        L'équipe Support App
        '''

    if type == 'password_recovery' :
        msg['Subject'] = "Récupération de mot de passe"
        texte_message = f'''
        Bonjour,

        Nous avons reçu une demande de récupération de votre mot de passe pour votre compte. Pour procéder à la récupération, veuillez utiliser le code de vérification ci-dessous :

        Code de vérification : {code}

        Si vous n'êtes pas à l'origine de cette demande, veuillez ignorer cet email. Si vous avez des questions ou si vous avez besoin d'assistance supplémentaire, n'hésitez pas à nous contacter.

        Cordialement,
        L'équipe Support App
        '''






    msg.attach(MIMEText(texte_message, 'plain'))
 
    try:
        serveur_smtp = smtplib.SMTP_SSL(serveur, port)
        serveur_smtp.login(email_expediteur, mdp_expediteur)
        texte = msg.as_string()
        serveur_smtp.sendmail(email_expediteur, email, texte)
        serveur_smtp.quit()

    except Exception as e:
        print("Erreur lors de l'envoi du courriel: " + str(e))
        return False





    
def clear_window(fenetre):
    for widget in fenetre.winfo_children():
        if widget.winfo_ismapped():
            if widget.winfo_manager() == 'pack':
                widget.pack_forget()
            elif widget.winfo_manager() == 'grid':
                widget.grid_forget()
            elif widget.winfo_manager() == 'place':
                widget.place_forget() 













