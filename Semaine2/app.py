import os
from modules.fonction import *
from modules.connexion import *
import pwnedpasswords

is_logged_in = False
chemin_fichier=""

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
        print("6) Revenir au menu précedent")
        answer = int(input("Choisir une option : "))
        os.system("cls")


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
            break


def menu_profil():
    while True :
        os.system("cls")
        print("|############################################################|")
        print("|                            Profil                          | ")
        print("|############################################################|")
        print("")
        print("1) Modifier votre mot de passe")
        print("2) Vérifier votre mot de passe")
        print("3) Quiter")
        answer = int(input("Choisir une option : "))
        os.system("cls")
        if answer == 1:
            os.system("cls")
            liste_commercants()
        elif answer == 2:
            os.system("cls")
            print("ok")
            input("")
        elif answer == 3:
            break






while True:
    os.system("cls") 

    if not is_logged_in:
        print("1) Se connecter")
        print("2) S'inscrire")
        print("3) Gestion du compte")
        answer = int(input("Choisir une option : "))

        if answer == 1:
            username = input("Entrez votre nom d'utilisateur : ")
            password = input("Entrez votre mot de passe : ")
            if login(username, password):
                nom_fichier = f"{username}.csv" 
                chemin_fichier = os.path.join('data', nom_fichier)
                os.system("cls")
                is_logged_in = True
            else:
                print("Échec de la connexion. Veuillez réessayer.")
                input("Appuyez sur une touche pour continuer...")

        elif answer == 2:
            os.system("cls")
            register()
           
        elif answer == 3:
            os.system("cls")
            print("1) Supprimer un compte")
            print("2) Liste des commercants")
            answer = int(input("Choisir une option : "))
            if answer == 1:
                os.system("cls")
                supprimer_user()

            elif answer == 2:
                os.system("cls")
                liste_commercants()

    else :
        print("1) Profil")
        print("2) Vos produits")
        answer = int(input("Choisir une option : "))

        if answer == 1:
            menu_profil()
     
        elif answer == 2 :
            menu_produit()
                

                