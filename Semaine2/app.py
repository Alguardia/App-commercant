import os
from modules.produits import *
from modules.connexion import *
from modules.gestion_compte import *
from modules.profil import *
from modules.admin import *

OKGREEN = '\033[92m'
WARNING = '\033[0;31m'
ENDC = '\033[0m'
is_logged_in = False
chemin_fichier=""
password_compromise= False
answer= 0

def menu_produit():
    while True :
        os.system("cls")
        print("|############################################################|")
        print("|                          Produit                           | ")
        print("|############################################################|")
        print("")
        print("1) Lire la liste")
        print("2) Ajouter un produit")
        print("3) Supprimer un produit")
        print("4) Rechercher")
        print("5) Trier")
        print("6) Quitter")
        answer = int(input(">> "))
        os.system("cls")
        nom_fichier = f"{username}.csv"
        chemin_fichier = os.path.join('data', nom_fichier)


        if answer == 1:
            lire_liste(chemin_fichier)
            input("Appuyez sur une touche pour continuer...")
            os.system("cls")

        elif answer == 2:
            ajouter_produit(chemin_fichier)
            input("Appuyez sur une touche pour continuer...")
            os.system("cls")    

        elif answer == 3:
            supprimer_produit(chemin_fichier)
            input("Appuyez sur une touche pour continuer...")
            os.system("cls")       

        elif answer == 4:
            rechercher_produit(chemin_fichier)
            input("Appuyez sur une touche pour continuer...")
            os.system("cls")        

        elif answer == 5:
            trier_produit(chemin_fichier)
            input("Appuyez sur une touche pour continuer...")
            os.system("cls")

        else : 
            menu_principal(password_compromise)


def menu_profil():
    global password_compromise
    while True :
        os.system("cls")
        print("|############################################################|")
        print("|                            Profil                          | ")
        print("|############################################################|")
        print("")
        print("1) Modifier votre mot de passe")
        print("2) Vérifier votre mot de passe")
        print("3) Quitter")
        answer = int(input(">> "))
        os.system("cls")
        if answer == 1:
            os.system("cls")
            password_compromise=modifier_password(username,password)
            return menu_principal(password_compromise)
        elif answer == 2:
            os.system("cls")
            haveibeenpwnd_password()
            return menu_principal(password_compromise)
        elif answer == 3:
            return menu_principal(password_compromise)



def menu_principal(password_compromise):
    global is_logged_in
    while True:
        os.system("cls")
        print("|############################################################|")
        print("|                         Menu principal                     |")
        print("|############################################################|")
        print("")

        if password_compromise:
            print(WARNING + "[X] Votre mot de passe actuel est compromis.\n[!] Aller dans la rubrique Profil pour changer votre mot de passe. " + ENDC)
            print("")
        elif password_compromise == False:
            print(OKGREEN + "[✓] Votre mot de passe est sécurisé." + ENDC)
            print("")
        
        print("1) Profil")
        print("2) Vos produits")
        print("3) Quitter")

        answer = int(input(">> "))

        if answer == 1:
            menu_profil()

        elif answer == 2:
            menu_produit()

        elif answer == 3:
            password_compromise = False  
            is_logged_in = False
            return menu_connexion()








def menu_connexion():
    
    while True :
        global is_logged_in ,password_compromise,username ,password
        is_logged_in = False

        os.system("cls")
        print(ENDC +"|############################################################|")
        print("|                          Connexion                         | ")
        print("|############################################################|")
        print("")
        print("1) Se connecter")
        print("2) S'inscrire")
        print("3) Gestion du compte")
        answer = int(input(">> "))

        if answer == 1:
            username = input("Entrez votre nom d'utilisateur : ")
            password = input("Entrez votre mot de passe : ")
            if login(username, password):
                
                
                password_compromise = password_compromises(password)
                
                os.system("cls")
                is_logged_in = True
                return is_logged_in, password
            else:
                print("Échec de la connexion. Veuillez réessayer.")
                input("Appuyez sur une touche pour continuer...")

        elif answer == 2:
            os.system("cls")
            register()
            

        elif answer == 3:
            menu_gestion_compte()

        elif answer == 0:
            username = input("Entrez votre nom d'utilisateur : ")
            password = input("Entrez votre mot de passe : ")
            if login_admin(username, password):
                os.system("cls")
                admin_panel()
                
            








def menu_gestion_compte():
    while True:
        os.system("cls")
        print("|############################################################|")
        print("|                       Gestion du compte                    |")
        print("|############################################################|")
        print("")
        print("1) Supprimer un compte")
        print("2) Liste des commercants")
        print("3) Quitter")
        answer = int(input(">> "))
        if answer == 1:
            os.system("cls")
            supprimer_user()
            

        elif answer == 2:
            os.system("cls")
            liste_commercants()
            
        elif answer == 3:
            menu_connexion()



while True:
    os.system("cls")

    if not is_logged_in:
        is_logged_in = menu_connexion()
    else:
        
        is_logged_in = menu_principal(password_compromise)