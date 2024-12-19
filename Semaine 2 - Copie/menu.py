from consolemenu import *
from consolemenu.items import *
from modules.fonction import *
from modules.connexion import *
import pwnedpasswords


chemin_fichier = ""


def is_logged():
    while True:
        menu_connecte = ConsoleMenu("Menu Principal", "Options pour les utilisateurs connectés")
        menu_connecte.append_item(FunctionItem("Lire la liste", lire_liste))
        menu_connecte.append_item(FunctionItem("Ajouter un produit", ajouter_produit))
        menu_connecte.append_item(FunctionItem("Supprimer un produit", supprimer_produit))
        menu_connecte.append_item(FunctionItem("Rechercher un produit", rechercher_produit))
        menu_connecte.append_item(FunctionItem("Trier les produits", trier_produit))
        menu_connecte.append_item(FunctionItem("Quitter", exit_menu))

        exit_item = menu_connecte.exit_item
        menu_connecte.exit_item = None
        menu_connecte.append_item(exit_item)
        exit_item.show = False
        
        menu_connecte.show() 
        input('')

        if exit_menu(): 
            break

def exit_menu(): 
    return True

def main_menu():

    while True:
        
        
        menu_non_connecte = ConsoleMenu("Menu Principal", "Options pour les utilisateurs non connectés")
        

        menu_non_connecte.append_item(FunctionItem("Se connecter", login))
        menu_non_connecte.append_item(FunctionItem("Créer un compte", register))
        menu_non_connecte.append_item(FunctionItem("Supprimer un compte", supprimer_user))
        menu_non_connecte.append_item(FunctionItem("Voir la liste des commerçants", liste_commercants))

        menu_non_connecte.show() 


if __name__ == "__main__":
    main_menu()
