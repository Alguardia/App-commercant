import os, time
from fonction import *
from tabulate import tabulate


def show_menu():
    global answer
    print("|############################################################|")
    print("|                          Produit                           | ")
    print("|############################################################|")
    print("")
    print("")
    print("1) Lire la liste")
    print("2) Ajouter un produit")
    print("3) Supprimer un produit")
    print("4) Rechercher")
    print("5) Trier")
    
    answer = int(input("Choisir une option : "))
    os.system("cls")
    return answer

while True:
    os.system("cls")    
    show_menu()

    if answer==1:
        lire_liste()
        input ("")
        os.system("cls")

                
    elif answer==2:
        ajouter_produit()
        input ("")
        os.system("cls")    

    elif answer==3:
        supprimer_produit()
        input ("")
        os.system("cls")       


    elif answer==4:
        rechercher_produit()
        input ("")
        os.system("cls")        


    elif answer==5:
        trier_produit()
        input ("")
        os.system("cls")

