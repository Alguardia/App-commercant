import os
from tabulate import tabulate

def lire_liste():
    with open('produit.txt', 'r', encoding='utf-8') as fichier:
        f = fichier.readlines()

    produits = []
    for ligne in f:
        a = ligne.strip().split(",")  
        produits.append(a)

    headers = ["NOM", "PRIX", "QUANTITE"]
    print(tabulate(produits, headers=headers, tablefmt="grid"))


def ajouter_produit():
    print("Ajouter un produit :")
    inputusernom=input("Nom du produit :")
    inputuserprix=input("Prix du produit :")
    inputuserquantite=input("Quantité du produit :")

    with open('produit.txt', 'a',encoding='utf-8') as fichier:
        if not  inputusernom or not inputuserprix or not  inputuserquantite:
            print("Erreur, le champ est vide")
            inputusernom=input("Nom du produit :")
            inputuserprix=input("Prix du produit :")
            inputuserquantite=input("Quantité du produit :")
            
        else:
            fichier.write('\n')
            fichier.write(inputusernom +','+ inputuserprix + ',' +  inputuserquantite)


def supprimer_produit():
    input_recherche = input("Entrez le nom du produit à supprimer : ")
    with open('produit.txt', 'r', encoding='utf-8') as fichier:
        lignes = fichier.readlines()

    nouvelles_lignes = []
    produit_supprime = False

    for ligne in lignes:
        a = ligne.split(",")
        if input_recherche.lower() == a[0].lower():
            produit_supprime = True 
            print(f"Produit supprimé : {a[0]} , PRIX : {a[1]} , QUANTITE : {a[2]}")
        else:
            nouvelles_lignes.append(ligne.strip())

    if produit_supprime:
        with open('produit.txt', 'w', encoding='utf-8') as fichier:
            for i, ligne in enumerate(nouvelles_lignes):
                if i < len(nouvelles_lignes) - 1:
                    fichier.write(ligne + "\n")
                else:
                    fichier.write(ligne)
            
        print("Le produit a été supprimé avec succès.")
    else:
        print("Aucun produit trouvé avec ce nom.")





def rechercher_produit():
    i=0
    print("1) Recherche séquentielle")
    print("2) Recherhce dichotomique")
    answer = int(input("Choisir une option : "))



    if answer==1:
        verif=False
        os.system("cls")
        print("1) Recherche séquentielle : ")
        input_recherche=str(input("produit a rechercher : "))
        with open('produit.txt', 'r',encoding='utf-8') as fichier:
            f = fichier.readlines()
            for ligne in f:
                i=i+1
                a = ligne.split(",")
                if input_recherche.lower()==a[0].lower():
                    print('ID :',i,', NOM :',a[0],', PRIX :',a[1],', QUANTITE :',a[2])
                    verif=True
        if not verif:
            print(f"Le produit '{input_recherche}' n'a pas été trouvé.")




    elif answer == 2:
        os.system("cls")
        print("2) Recherhce dichotomique : ")
        liste = []
        input_recherche = str(input("Produit à rechercher : "))
        
        with open('produit.txt', 'r', encoding='utf-8') as fichier:
            f = fichier.readlines()
            
            for ligne in f:
                a = ligne.split(",")
                produit_nom = a[0].strip().lower()
                produit_prix = a[1].strip()
                produit_quantite = a[2].strip()
                liste.append((produit_nom, produit_prix, produit_quantite))
        liste.sort()
        indice = -1
        min = 0
        max = len(liste) - 1
        while min <= max and indice == -1:
            moy = (min + max) // 2
            if liste[moy][0] < input_recherche:
                min = moy + 1
            elif liste[moy][0] > input_recherche:
                max = moy - 1
            else:
                indice = moy


        if indice != -1:
            print('ID :',indice+1,', NOM :',input_recherche,', PRIX :',liste[indice][1],', QUANTITE :',liste[indice][2])
        else:
            print(f"Le produit '{input_recherche}' n'a pas été trouvé.")






def trier_produit():
    i=0
    print("1) Tri par sélection par nom")
    print("2) Tri à bulles par prix ")
    print("3) Tri rapide par quantité")
    answer = int(input("Choisir une option : "))

    if answer == 1:
        os.system("cls")
        print("1) Tri par sélection par nom : ")
        liste = []
        

        with open('produit.txt', 'r', encoding='utf-8') as fichier:
            f = fichier.readlines()
            
            for ligne in f:
                a = ligne.split(",")
                produit_nom = a[0].strip().lower()
                produit_prix = a[1].strip()
                produit_quantite = a[2].strip()
                liste.append((produit_nom, produit_prix, produit_quantite))


        n = len(liste)
        for i in range(0, n-1):
            min_indice = i
            min = liste[i]
            for j in range(i+1, n):
                if liste[j][0] < min[0]:
                    min_indice = j
                    min = liste[j]
            
            liste[i], liste[min_indice] = liste[min_indice], liste[i]


        headers = ["NOM", "PRIX", "QUANTITE"]
        print(tabulate(liste, headers=headers, tablefmt="grid"))

	

         


    if answer == 2:
        os.system("cls")
        print("2) Tri à bulles par prix : ")
        
        liste = []
        
        with open('produit.txt', 'r', encoding='utf-8') as fichier:
            f = fichier.readlines()

            for ligne in f:
                a = ligne.split(",")
                produit_nom = a[0].strip().lower()
                produit_prix = float(a[1].strip())
                produit_quantite = a[2].strip()
                liste.append((produit_nom, produit_prix, produit_quantite))

        n = len(liste)
        permut = True
        while permut:
            permut = False
            for i in range(0, n-1):
                if liste[i][1] > liste[i+1][1]:
                    liste[i], liste[i+1] = liste[i+1], liste[i]
                    permut = True
            n = n - 1

        headers = ["NOM", "PRIX", "QUANTITE"]
        print(tabulate(liste, headers=headers, tablefmt="grid"))





    if answer == 3:
        os.system("cls")
        print("3) Tri rapide par quantité :")
        liste = []
        
        with open('produit.txt', 'r', encoding='utf-8') as fichier:
            f = fichier.readlines()
            
            for ligne in f:
                a = ligne.split(",")
                produit_nom = a[0].strip().lower()
                produit_prix = a[1].strip()
                produit_quantite = a[2].strip()
                liste.append((produit_nom, float(produit_prix), int(produit_quantite)))

        n = len(liste)

        def tri_rapide(liste):
            if len(liste) <= 1:
                return liste
            else:
                pivot = liste[0][2]
                gauche = [x for x in liste[1:] if x[2] < pivot]
                droite = [x for x in liste[1:] if x[2] >= pivot]
                return tri_rapide(gauche) + [liste[0]] + tri_rapide(droite)

        liste_triee = tri_rapide(liste)

        headers = ["NOM", "PRIX", "QUANTITE"]
        print(tabulate(liste_triee, headers=headers, tablefmt="grid"))