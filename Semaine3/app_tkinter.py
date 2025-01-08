from tkinter import *
import tkinter as tk
from webbrowser import *
from modules.produits import *
from modules.connexion import *
from modules.gestion_compte import *
from modules.profil import *
from modules.admin import *

is_logged_in = False
chemin_fichier=""
password_compromise= False


fenetre = Tk()
fenetre.geometry("400x150")
v = StringVar() 
fenetre.title('Menu Connexion')

#####################################################   Menu connexion   #################################################################

def menu_connexion():
    fenetre.geometry("400x150")
    clear_window()
    header_frame = tk.Frame(fenetre)
    header_frame.pack(fill=tk.X)


    label_header = tk.Label(header_frame, text="Menu de connexion :", font=("Arial", 16))
    label_header.pack(side=tk.LEFT, pady=10, padx=10)

    retour_button = tk.Button(header_frame, text="← Retour", command=menu_connexion)
    retour_button.pack(side=tk.RIGHT, pady=10, padx=10)


    button_frame = tk.Frame(fenetre)
    button_frame.pack(expand=True)

    bouton1 = Button(button_frame,text = "Se connecter",width=15, command=menu_login)
    bouton1.pack(side=tk.LEFT, padx=10)
    bouton2 = Button(button_frame,text = "Crée un compte",width=15, command=menu_register)
    bouton2.pack(side=tk.LEFT, padx=10) 
    bouton3 = Button(button_frame,text = "Gestion du compte",width=15, command=menu_gestion_compte)
    bouton3.pack(side=tk.LEFT, padx=10)
    
    




#####################################################   Menu login   #################################################################





def login_inter():
    global password_compromise ,username
    username=entrée1
    if login(entrée1, entrée2,fenetre):
                password=entrée2.get()
                password_compromise = password_compromises(password)
                menu_principal()
    

def menu_login():

    global entrée1, entrée2
    
    clear_window()
    fenetre.geometry("400x150")
    fenetre.title('Se connecter')
    header_frame = tk.Frame(fenetre)
    header_frame.pack(fill=tk.X)


    label_header = tk.Label(header_frame, text="Se connecter :", font=("Arial", 16))
    label_header.pack(side=tk.LEFT, pady=10, padx=10)

    retour_button = tk.Button(header_frame, text="← Retour", command=menu_connexion)
    retour_button.pack(side=tk.RIGHT, pady=10, padx=10)

    texte1 = Label(fenetre, text = "Nom d'utilisateur : ")
    texte1.place(x = 20, y = 50)
    entrée1 = Entry(fenetre)
    entrée1.place(x = 150, y = 50)
    texte2 = Label(fenetre,text = "Mot de passe : ")
    texte2.place(x = 20, y = 80)
    entrée2 = Entry(fenetre, show="*")
    entrée2.place(x = 150, y = 80)

    bouton1 = Button(fenetre,text = "Connexion",width=15, command=login_inter)
    bouton1.place(x = 20, y = 110)



#####################################################   Menu register   #################################################################


def register_inter():
    global fenetre, entrée1_register , entrée2_register 
    
    verif = register(entrée1_register,entrée2_register, fenetre)
    if verif :
        fenetre.after(2000,menu_connexion)

        
def menu_register():

    global entrée1_register, entrée2_register
    clear_window()
    fenetre.geometry("400x150")
    fenetre.title('Crée un compte')
    header_frame = tk.Frame(fenetre)
    header_frame.pack(fill=tk.X)


    label_header = tk.Label(header_frame, text="Crée un Compte :", font=("Arial", 16))
    label_header.pack(side=tk.LEFT, pady=10, padx=10)

    retour_button = tk.Button(header_frame, text="← Retour", command=menu_connexion)
    retour_button.pack(side=tk.RIGHT, pady=10, padx=10)

    texte1 = Label(fenetre, text = "Nom d'utilisateur : ")
    texte1.place(x = 20, y = 50)
    entrée1_register = Entry(fenetre)
    entrée1_register.place(x = 150, y = 50)
    texte2 = Label(fenetre,text = "Mot de passe : ")
    texte2.place(x = 20, y = 80)
    entrée2_register = Entry(fenetre, show="*")
    entrée2_register.place(x = 150, y = 80)

    bouton1 = Button(fenetre,text = "Crée un compte",width=15, command=register_inter)
    bouton1.place(x = 20, y = 110)



#####################################################   Menu Gestion du compte   #################################################################


def menu_gestion_compte():

    clear_window()
    fenetre.geometry("400x150")
    fenetre.title('Gestion du compte')
    header_frame = tk.Frame(fenetre)
    header_frame.pack(fill=tk.X)


    label_header = tk.Label(header_frame, text="Gestion du compte :", font=("Arial", 16))
    label_header.pack(side=tk.LEFT, pady=10, padx=10)

    retour_button = tk.Button(header_frame, text="← Retour", command=menu_connexion)
    retour_button.pack(side=tk.RIGHT, pady=10, padx=10)


    button_frame = tk.Frame(fenetre)
    button_frame.pack(expand=True)

    bouton1 = Button(button_frame,text = "Supprimer compte", width=15, command=menu_supprimer_utilisateur)
    bouton1.pack(side=tk.LEFT, padx=10)
    bouton2 = Button(button_frame,text = "Liste commercants", width=15, command=menu_liste_commercant)
    bouton2.pack(side=tk.LEFT, padx=10) 

    



#####################################################   Menu supprimer utilisateur   #################################################################

def supprimer_user_inter():
    global fenetre, entrée1_remove , entrée2_remove 
    verif = supprimer_user(entrée1_remove,entrée2_remove, fenetre)
    if verif :
        fenetre.after(2000,menu_connexion)


def menu_supprimer_utilisateur():
    global entrée1_remove, entrée2_remove
    clear_window()
    fenetre.geometry("400x150")
    fenetre.title('Supprimer un compte')
    header_frame = tk.Frame(fenetre)
    header_frame.pack(fill=tk.X)


    label_header = tk.Label(header_frame, text="Supprimer un compte :", font=("Arial", 16))
    label_header.pack(side=tk.LEFT, pady=10, padx=10)

    retour_button = tk.Button(header_frame, text="← Retour", command=menu_gestion_compte)
    retour_button.pack(side=tk.RIGHT, pady=10, padx=10)

    texte1 = Label(fenetre, text = "Nom d'utilisateur : ")
    texte1.place(x = 20, y = 50)
    entrée1_remove = Entry(fenetre)
    entrée1_remove.place(x = 150, y = 50)
    texte2 = Label(fenetre,text = "Mot de passe : ")
    texte2.place(x = 20, y = 80)
    entrée2_remove = Entry(fenetre, show="*")
    entrée2_remove.place(x = 150, y = 80)

    bouton1 = Button(fenetre,text = "Supprimer",width=15, command=supprimer_user_inter)
    bouton1.place(x = 20, y = 110)




#####################################################   Menu liste des commercants   #################################################################

def menu_liste_commercant():
    clear_window()
    fenetre.title('Liste des commerçants')

    header_frame = tk.Frame(fenetre)
    header_frame.pack(fill=tk.X)

    label_header = tk.Label(header_frame, text="Liste des commerçants :", font=("Arial", 16))
    label_header.pack(side=tk.LEFT, pady=10, padx=10)

    retour_button = tk.Button(header_frame, text="← Retour", command=menu_gestion_compte)
    retour_button.pack(side=tk.RIGHT, pady=10, padx=10)

    commercants = liste_commercants(fenetre)

    hauteur_fenetre = 100 + len(commercants) * 30 
    fenetre.geometry(f"400x{hauteur_fenetre}")

    frame_commercants = tk.Frame(fenetre)
    frame_commercants.pack(fill=tk.BOTH, expand=True)

    for commercant in commercants:
        label_commercant = tk.Label(frame_commercants, text=f"- {commercant}", font=("Arial", 12), anchor="w")
        label_commercant.pack(pady=5, padx=10, anchor="w")




#####################################################   Menu principal   #################################################################


def menu_principal_inter():
    test=1

def menu_principal():
    fenetre.geometry("400x150")
    fenetre.title('Menu principal')
    clear_window()


    header_frame = tk.Frame(fenetre)
    header_frame.pack(fill=tk.X)

    label_header = tk.Label(header_frame, text="Menu principal :", font=("Arial", 16))
    label_header.pack(side=tk.LEFT, pady=10, padx=10)

    retour_button = tk.Button(header_frame, text="← Déconnexion", command=menu_connexion)
    retour_button.pack(side=tk.RIGHT, pady=10, padx=10)

    password_frame = tk.Frame(fenetre)
    password_frame.pack(pady=10)

    if password_compromise:
        password_status = "[X] Votre mot de passe est compromis.\n[!] Aller dans la rubrique Profil pour changer votre mot de passe."
        label_password = tk.Label(password_frame, text=password_status, fg="red")
    else:
        password_status = "[✓] Votre mot de passe est sécurisé."
        label_password = tk.Label(password_frame, text=password_status, fg="green")

    label_password.pack()

    button_frame = tk.Frame(fenetre)
    button_frame.pack(expand=True)

    bouton1 = Button(button_frame, text="Profil", width=15, command=menu_profil)
    bouton1.pack(side=tk.LEFT, padx=10)
    bouton2 = Button(button_frame, text="Vos produits", width=15, command=menu_produit)
    bouton2.pack(side=tk.LEFT, padx=10)




#####################################################   Menu profil   #################################################################



def menu_profil():
    fenetre.geometry("400x150")
    fenetre.title('Profil')
    clear_window()

    header_frame = tk.Frame(fenetre)
    header_frame.pack(fill=tk.X)

    label_header = tk.Label(header_frame, text="Votre Profil :", font=("Arial", 16))
    label_header.pack(side=tk.LEFT, pady=10, padx=10)

    retour_button = tk.Button(header_frame, text="← Retour", command=menu_principal)
    retour_button.pack(side=tk.RIGHT, pady=10, padx=10)

    button_frame = tk.Frame(fenetre)
    button_frame.pack(expand=True)

    bouton1 = Button(button_frame, text="Modifier votre mot de passe", width=25, command=menu_change_password)
    bouton1.pack(side=tk.LEFT, padx=10)
    bouton2 = Button(button_frame, text="Vérifier votre mot de passe", width=25, command=menu_check_password)
    bouton2.pack(side=tk.LEFT, padx=10)





#####################################################   Menu modifier mot de passe   #################################################################

def change_password_inter():
    global fenetre, entrée1_change , entrée2_change
    
    verif = modifier_password(username,entrée1_change,entrée2_change, fenetre)
    if verif :
        fenetre.after(2000,menu_connexion)

def menu_change_password():
    global entrée1_change, entrée2_change
    clear_window()
    fenetre.geometry("400x150")
    fenetre.title('Modifier votre mot de passe')
    header_frame = tk.Frame(fenetre)
    header_frame.pack(fill=tk.X)


    label_header = tk.Label(header_frame, text="Modifier votre mot de passe :", font=("Arial", 16))
    label_header.pack(side=tk.LEFT, pady=10, padx=10)

    retour_button = tk.Button(header_frame, text="← Retour", command=menu_principal)
    retour_button.pack(side=tk.RIGHT, pady=10, padx=10)


    texte1 = Label(fenetre,text = "Mot de passe : ")
    texte1.place(x = 20, y = 50)
    entrée1_change = Entry(fenetre, show="*")
    entrée1_change.place(x = 150, y = 50)
    texte2 = Label(fenetre,text = "Nouveau mot de passe : ")
    texte2.place(x = 20, y = 80)
    entrée2_change = Entry(fenetre, show="*")
    entrée2_change.place(x = 150, y = 80)

    bouton1 = Button(fenetre,text = "Modifier",width=15, command=change_password_inter)
    bouton1.place(x = 20, y = 110)


#####################################################   Menu verifier votre mot de passe   #################################################################

def check_password_inter():
    test=1


def menu_check_password():
    global entrée1_change, entrée2_change
    clear_window()
    fenetre.geometry("400x150")
    fenetre.title('Vérifier votre mod de passe')
    header_frame = tk.Frame(fenetre)
    header_frame.pack(fill=tk.X)


    label_header = tk.Label(header_frame, text="Vérifier votre mot de passe :", font=("Arial", 16))
    label_header.pack(side=tk.LEFT, pady=10, padx=10)

    retour_button = tk.Button(header_frame, text="← Retour", command=menu_principal)
    retour_button.pack(side=tk.RIGHT, pady=10, padx=10)

    texte1 = Label(fenetre, text = "Mot de passe : ")
    texte1.place(x = 20, y = 50)
    entrée1_check = Entry(fenetre)
    entrée1_check.place(x = 150, y = 50)

    bouton1 = Button(fenetre,text = "Vérifier",width=15, command=check_password_inter)
    bouton1.place(x = 20, y = 90)





#####################################################   Menu produit   #################################################################


def menu_produit():
     test="test"








#####################################################   clear fenetre   #################################################################



def clear_window():
    for widget in fenetre.winfo_children():
        if widget.winfo_ismapped():
            if widget.winfo_manager() == 'pack':
                widget.pack_forget()
            elif widget.winfo_manager() == 'grid':
                widget.grid_forget()
            elif widget.winfo_manager() == 'place':
                widget.place_forget()











menu_connexion()

fenetre.mainloop()



