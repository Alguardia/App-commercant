from tkinter import *
import tkinter as tk
from webbrowser import *
from modules.produits import *
from modules.connexion import *
from modules.gestion_compte import *
from modules.profil import *
from modules.admin import *
from tkinter import ttk
import tkinter.messagebox
import os 
from tkinter import ttk

is_logged_in = False
chemin_fichier=""
password_compromise= False
username = ''

fenetre = tk.Tk()
fenetre.geometry("400x150")
fenetre.title('Menu Connexion')

chemin_image = os.path.abspath('img/image2.png')

image = PhotoImage(file=chemin_image)

fenetre.iconphoto(False, image)


fenetre.resizable(False, False)

#####################################################   Menu connexion   #################################################################

def menu_connexion():
    fenetre.geometry("400x150")
    clear_window()
    header_frame = tk.Frame(fenetre)
    header_frame.pack(fill=tk.X)


    label_header = tk.Label(header_frame, text="Menu de connexion :", font=("Arial", 16, 'underline'),)
    label_header.pack(side=tk.LEFT, pady=10, padx=10)

    retour_button = tk.Button(header_frame, text="← Quiter", command=fenetre.destroy)
    retour_button.pack(side=tk.RIGHT, pady=10, padx=10)


    button_frame = tk.Frame(fenetre)
    button_frame.place(relx=0.5, rely=0.5, anchor='center')

    bouton1 = Button(button_frame,text = "Se connecter",width=15, command=menu_login)
    bouton1.pack(side=tk.LEFT, padx=10)
    bouton2 = Button(button_frame,text = "Crée un compte",width=15, command=menu_register)
    bouton2.pack(side=tk.LEFT, padx=10) 
    bouton3 = Button(button_frame,text = "Gestion du compte",width=15, command=menu_gestion_compte)
    bouton3.pack(side=tk.LEFT, padx=10)
    
    




#####################################################   Menu login   #################################################################





def login_inter():
    global password_compromise ,username , password
    username=entrée1.get()
    password=entrée2.get()
    if login(entrée1, entrée2,fenetre):
                password_compromise = haveibeenpwnd_password(password)
                
                if password_compromise:
                    df = pd.read_csv('data/user.csv')
                    user_row = df[df['username'] == username]
            
                    if not user_row.empty:
                        email = user_row['email'].iloc[0]
                        envoyer_email(email)
                
                fenetre.after(2000,menu_principal)
    

def menu_login():

    global entrée1, entrée2
    
    clear_window()
    fenetre.geometry("400x150")
    fenetre.title('Se connecter')
    header_frame = tk.Frame(fenetre)
    header_frame.pack(fill=tk.X)


    label_header = tk.Label(header_frame, text="Se connecter :", font=("Arial", 16, 'underline'))
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
    global fenetre, entrée1_register , entrée2_register , entrée3_register
    
    verif = register(entrée1_register,entrée2_register, entrée3_register, fenetre)
    if verif :
        fenetre.after(2000,menu_connexion)

        
def menu_register():

    global entrée1_register, entrée2_register , entrée3_register
    clear_window()
    fenetre.geometry("400x150")
    fenetre.title('Crée un compte')
    header_frame = tk.Frame(fenetre)
    header_frame.pack(fill=tk.X)


    label_header = tk.Label(header_frame, text="Crée un Compte :", font=("Arial", 16, 'underline'))
    label_header.pack(side=tk.LEFT, pady=10, padx=10)

    retour_button = tk.Button(header_frame, text="← Retour", command=menu_connexion)
    retour_button.pack(side=tk.RIGHT, pady=10, padx=10)

    texte1 = Label(fenetre, text = "Nom d'utilisateur : ")
    texte1.place(x = 20, y = 40)
    entrée1_register = Entry(fenetre)
    entrée1_register.place(x = 150, y = 40)
    
    texte3 = Label(fenetre,text = "Email : ")
    texte3.place(x = 20, y = 65)
    entrée3_register = Entry(fenetre)
    entrée3_register.place(x = 150, y = 65)


    texte2 = Label(fenetre,text = "Mot de passe : ")
    texte2.place(x = 20, y = 90)
    entrée2_register = Entry(fenetre, show="*")
    entrée2_register.place(x = 150, y = 90)


    bouton1 = Button(fenetre,text = "Crée un compte",width=15, command=register_inter)
    bouton1.place(x = 20, y = 110)



#####################################################   Menu Gestion du compte   #################################################################


def menu_gestion_compte():

    clear_window()
    fenetre.geometry("400x150")
    fenetre.title('Gestion du compte')
    header_frame = tk.Frame(fenetre)
    header_frame.pack(fill=tk.X)


    label_header = tk.Label(header_frame, text="Gestion du compte :", font=("Arial", 16, 'underline'))
    label_header.pack(side=tk.LEFT, pady=10, padx=10)

    retour_button = tk.Button(header_frame, text="← Retour", command=menu_connexion)
    retour_button.pack(side=tk.RIGHT, pady=10, padx=10)


    button_frame = tk.Frame(fenetre)
    button_frame.place(relx=0.5, rely=0.5, anchor='center')

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


    label_header = tk.Label(header_frame, text="Supprimer un compte :", font=("Arial", 16, 'underline'))
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

    label_header = tk.Label(header_frame, text="Liste des commerçants :", font=("Arial", 16, 'underline'))
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



def menu_principal():
    global password_compromise
    clear_window()
    fenetre.geometry("400x150")
    fenetre.title('Menu principal')
    

    header_frame = tk.Frame(fenetre)
    header_frame.pack(fill=tk.X)

    label_header = tk.Label(header_frame, text=f"Menu principal :", font=("Arial", 16, 'underline'))
    label_header.pack(side=tk.LEFT, pady=10, padx=10)

    retour_button = tk.Button(header_frame, text="← Déconnexion", command=menu_connexion)
    retour_button.pack(side=tk.RIGHT, pady=10, padx=10)

    password_frame = tk.Frame(fenetre)
    password_frame.pack(pady=10)

    if password_compromise:
        password_status = "[X] Votre mot de passe est compromis."
        password_status2 = "[!] Aller dans la rubrique Profil pour changer votre mot de passe."
        label_password = tk.Label(password_frame, text=password_status, fg="red")
        label_password2 = tk.Label(password_frame, text=password_status2, fg="orange")
        label_password.pack()
        label_password2.pack()
    else:
        password_status = "[✓] Votre mot de passe est sécurisé."
        label_password = tk.Label(password_frame, text=password_status, fg="green")
        label_password.pack()
    
    

    button_frame = tk.Frame(fenetre)
    button_frame.pack(expand=True)

    bouton1 = Button(button_frame, text="Profil", width=15, command=menu_profil)
    bouton1.pack(side=tk.LEFT, padx=10)


    if username=='root':
        bouton3 = Button(button_frame, text="Panel Admin", width=15, command=menu_admin)
        bouton3.pack(side=tk.LEFT, padx=10 )




    bouton2 = Button(button_frame, text="Vos produits", width=15, command=menu_produit)
    bouton2.pack(side=tk.LEFT, padx=10)



#####################################################   panel admin   #################################################################



def menu_admin():
        
    fenetre.title('Panel Admin')
    fenetre.geometry("800x150")
    clear_window()


    chemin_fichier = 'password/log.csv'

    df = pd.read_csv(chemin_fichier)
    df_sorted = df.sort_values(ascending=False,by="id")
    liste = df_sorted.values.tolist()
   
    header_frame = tk.Frame(fenetre)
    header_frame.pack(fill=tk.X)


    label_header = tk.Label(header_frame, text="Panel Admin :", font=("Arial", 16, 'underline'))
    label_header.pack(side=tk.LEFT, pady=10, padx=10)

    retour_button = tk.Button(header_frame, text="← Retour", command=menu_principal)
    retour_button.pack(side=tk.RIGHT, pady=10, padx=10)

    hauteur_fenetre = len(liste)*20
    hauteur_fenetre = min(hauteur_fenetre, 600)
    fenetre.geometry(f"800x{hauteur_fenetre}")
    

    frame_commercants = tk.Frame(fenetre)
    frame_commercants.pack(fill=tk.BOTH, expand=True)
    style = ttk.Style()
    style.configure("Treeview.Heading", font=("Arial", 10, "bold"))
    tree = ttk.Treeview(frame_commercants, columns=("id", "date", "time", "user", "processus", "details"), show='headings')
    

    tree.heading("id", text="ID")
    tree.heading("date", text="Date")
    tree.heading("time", text="Time")
    tree.heading("user", text="User")
    tree.heading("processus", text="Processus")
    tree.heading("details", text="Details")


    tree.column("id", width=10)
    tree.column("date", width=10)
    tree.column("time", width=10)
    tree.column("user", width=10)
    tree.column("processus", width=10)
    tree.column("details", width=200)

    
    for i, produit in enumerate(liste, start=1):
        tree.insert("", "end", values=(produit))

    tree.pack(fill=tk.BOTH, expand=True)





#####################################################   Menu profil   #################################################################



def menu_profil():
    fenetre.geometry("400x150")
    fenetre.title('Profil')
    clear_window()
    
    header_frame = tk.Frame(fenetre)
    header_frame.pack(fill=tk.X)

    label_header = tk.Label(header_frame, text="Votre Profil :", font=("Arial", 16, 'underline'))
    label_header.pack(side=tk.LEFT, pady=10, padx=10)

    retour_button = tk.Button(header_frame, text="← Retour", command=menu_principal)
    retour_button.pack(side=tk.RIGHT, pady=10, padx=10)

    button_frame = tk.Frame(fenetre)
    button_frame.place(relx=0.5, rely=0.5, anchor='center')




    bouton1 = Button(button_frame, text="Modifier votre mot de passe", width=25, command=menu_change_password)
    bouton1.pack(side=tk.LEFT, padx=10)
    bouton2 = Button(button_frame, text="Vérifier votre mot de passe", width=25, command=menu_check_password)
    bouton2.pack(side=tk.LEFT, padx=10)
    




#####################################################   Menu modifier mot de passe   #################################################################

def change_password_inter():
    global fenetre, entrée1_change , entrée2_change , password_compromise
    
    verif = modifier_password(username,entrée1_change,entrée2_change, fenetre)
    password_compromise = haveibeenpwnd_password(entrée2_change.get())
    if verif :
        fenetre.after(2000,menu_principal)

def menu_change_password():
    global entrée1_change, entrée2_change
    clear_window()
    fenetre.geometry("400x150")
    fenetre.title('Modifier votre mot de passe')
    header_frame = tk.Frame(fenetre)
    header_frame.pack(fill=tk.X)


    label_header = tk.Label(header_frame, text="Modifier votre mot de passe :", font=("Arial", 16, 'underline'))
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
    global fenetre, entrée1_check

    verif = haveibeenpwnd_password_check(entrée1_check, fenetre,username)
    if verif :
        fenetre.after(2000,menu_principal)


def menu_check_password():
    global entrée1_check
    clear_window()
    fenetre.geometry("400x150")
    fenetre.title('Vérifier votre mod de passe')
    header_frame = tk.Frame(fenetre)
    header_frame.pack(fill=tk.X)


    label_header = tk.Label(header_frame, text="Vérifier votre mot de passe :", font=("Arial", 16, 'underline'))
    label_header.pack(side=tk.LEFT, pady=10, padx=10)

    retour_button = tk.Button(header_frame, text="← Retour", command=menu_principal)
    retour_button.pack(side=tk.RIGHT, pady=10, padx=10)

    texte1 = Label(fenetre, text = "Mot de passe : ")
    texte1.place(x = 20, y = 50)
    entrée1_check = Entry(fenetre,  show='*')
    entrée1_check.place(x = 150, y = 50)

    bouton1 = Button(fenetre,text = "Vérifier",width=15, command=check_password_inter)
    bouton1.place(x = 20, y = 90)





#####################################################   Menu produit   #################################################################


def menu_produit():
    global username
    fenetre.title('Gestion des produits')
    fenetre.geometry("400x150")
    clear_window()
    header_frame = tk.Frame(fenetre)
    header_frame.pack(fill=tk.X)


    label_header = tk.Label(header_frame, text="Gestion des produits :", font=("Arial", 16, 'underline'))
    label_header.pack(side=tk.LEFT, pady=10, padx=10)

    retour_button = tk.Button(header_frame, text="← Retour", command=menu_principal)
    retour_button.pack(side=tk.RIGHT, pady=10, padx=10)


    button_frame = tk.Frame(fenetre)
    button_frame.pack(expand=True)

    button_frame2 = tk.Frame(fenetre)
    button_frame2.pack(expand=True)

    bouton1 = Button(button_frame,text = "Lire la liste",width=15, command=menu_lire_liste)
    bouton1.pack(side=tk.LEFT, padx=10)
    bouton2 = Button(button_frame,text = "Ajouter produit",width=15, command=menu_ajouter_produit)
    bouton2.pack(side=tk.LEFT, padx=10) 
    bouton3 = Button(button_frame,text = "Supprimer produit",width=15, command=menu_supprimer_produit)
    bouton3.pack(side=tk.LEFT, padx=10)
    bouton4 = Button(button_frame2,text = "Rechercher",width=15, command=menu_recherche_produit)
    bouton4.pack(side=tk.LEFT, padx=10)
    bouton5 = Button(button_frame2,text = "Trier",width=15, command=menu_trier_produit)
    bouton5.pack(side=tk.LEFT, padx=10)



#####################################################   lire liste   #################################################################

def menu_lire_liste():
    global produit
    
    fenetre.title('Lire la liste des produits')
    fenetre.geometry("400x150")
    clear_window()


    chemin_fichier = recup_user()


    liste=lire_liste(chemin_fichier)

    header_frame = tk.Frame(fenetre)
    header_frame.pack(fill=tk.X)


    label_header = tk.Label(header_frame, text="Lire la liste des produits :", font=("Arial", 16, 'underline'))
    label_header.pack(side=tk.LEFT, pady=10, padx=10)

    retour_button = tk.Button(header_frame, text="← Retour", command=menu_produit)
    retour_button.pack(side=tk.RIGHT, pady=10, padx=10)

    hauteur_fenetre = 100 + len(liste) * 20
    fenetre.geometry(f"400x{hauteur_fenetre}")

    frame_commercants = tk.Frame(fenetre)
    frame_commercants.pack(fill=tk.BOTH, expand=True)

    style = ttk.Style()
    style.configure("Treeview.Heading", font=("Arial", 10, "bold"))
    tree = ttk.Treeview(frame_commercants, columns=("NOM", "PRIX", "QUANTITE"))


    tree.heading("NOM", text="Nom")
    tree.heading("PRIX", text="Prix")
    tree.heading("QUANTITE", text="Quantité")


    tree.column("NOM", width=150)
    tree.column("PRIX", width=100)
    tree.column("QUANTITE", width=100, anchor="center")

    tree["show"] = "headings"

    for i, produit in enumerate(liste, start=1):
        tree.insert("", "end", values=(produit))

    tree.pack(fill=tk.BOTH, expand=True)



#####################################################   Ajouter produit   #################################################################

def ajouter_produit_inter():
    global entrée1, entrée2, entrée3
    chemin_fichier=recup_user()
    verif = ajouter_produit(chemin_fichier,entrée1, entrée2, entrée3,fenetre)
    if verif :
        fenetre.after(2000,menu_produit)


def menu_ajouter_produit():

    global entrée1, entrée2 , entrée3
    clear_window()

    

    fenetre.geometry("400x150")
    fenetre.title('Ajouter produit')
    header_frame = tk.Frame(fenetre)
    header_frame.pack(fill=tk.X)


    label_header = tk.Label(header_frame, text="Ajouter un produit :", font=("Arial", 16, 'underline'))
    label_header.pack(side=tk.LEFT, pady=10, padx=10)

    retour_button = tk.Button(header_frame, text="← Retour", command=menu_produit)
    retour_button.pack(side=tk.RIGHT, pady=10, padx=10)


    texte1 = Label(fenetre,text = "Nom : ")
    texte1.place(x = 20, y = 40)
    entrée1 = Entry(fenetre)
    entrée1.place(x = 100, y = 40)
    texte2 = Label(fenetre,text = "Prix : ")
    texte2.place(x = 20, y = 62)
    entrée2 = Entry(fenetre)
    entrée2.place(x = 100, y = 62)
    texte3 = Label(fenetre,text = "Quantité : ")
    texte3.place(x = 20, y = 84)
    entrée3 = Entry(fenetre)
    entrée3.place(x = 100, y = 84)

    bouton1 = Button(fenetre,text = "Ajouter",width=15, command=ajouter_produit_inter)
    bouton1.place(x = 20, y = 110)



#####################################################   Menu supprimer produit   #################################################################

def supprimer_produit_inter():
    global fenetre, entrée1_remove 
    chemin_fichier= recup_user()
    verif = supprimer_produit(chemin_fichier, entrée1_remove, fenetre)
    if verif :
        fenetre.after(2000,menu_produit)


def menu_supprimer_produit():
    global entrée1_remove
    clear_window()
    fenetre.geometry("400x150")
    fenetre.title('Supprimer un produit')
    header_frame = tk.Frame(fenetre)
    header_frame.pack(fill=tk.X)


    label_header = tk.Label(header_frame, text="Supprimer un produit :", font=("Arial", 16, 'underline'))
    label_header.pack(side=tk.LEFT, pady=10, padx=10)

    retour_button = tk.Button(header_frame, text="← Retour", command=menu_produit)
    retour_button.pack(side=tk.RIGHT, pady=10, padx=10)

    texte1 = Label(fenetre, text = "Nom du produit : ")
    texte1.place(x = 20, y = 50)
    entrée1_remove = Entry(fenetre)
    entrée1_remove.place(x = 150, y = 50)


    bouton1 = Button(fenetre,text = "Supprimer",width=15, command=supprimer_produit_inter)
    bouton1.place(x = 20, y = 110)





#####################################################   Menu recherche produit  #################################################################

def recherche_produit_inter():
    global fenetre, entrée1
    chemin_fichier= recup_user()
    verif = rechercher_produit(chemin_fichier, entrée1, fenetre)
    if verif :
        fenetre.after(5000,menu_produit)


def menu_recherche_produit():
    global entrée1
    clear_window()
    fenetre.geometry("400x150")
    fenetre.title('Rechercher un produit')
    header_frame = tk.Frame(fenetre)
    header_frame.pack(fill=tk.X)


    label_header = tk.Label(header_frame, text="Rechercher un produit :", font=("Arial", 16, 'underline'))
    label_header.pack(side=tk.LEFT, pady=10, padx=10)

    retour_button = tk.Button(header_frame, text="← Retour", command=menu_produit)
    retour_button.pack(side=tk.RIGHT, pady=10, padx=10)

    texte1 = Label(fenetre, text = "Nom du produit : ")
    texte1.place(x = 20, y = 50)
    entrée1 = Entry(fenetre)
    entrée1.place(x = 150, y = 50)


    bouton1 = Button(fenetre,text = "Rechercher",width=15, command=recherche_produit_inter)
    bouton1.place(x = 20, y = 110)


#####################################################   Menu trier produit  #################################################################

def menu_trier_produit():
    global username
    fenetre.title('Trier les produits')
    fenetre.geometry("400x150")
    clear_window()
    header_frame = tk.Frame(fenetre)
    header_frame.pack(fill=tk.X)


    label_header = tk.Label(header_frame, text="Trier les produits :", font=("Arial", 16, 'underline'))
    label_header.pack(side=tk.LEFT, pady=10, padx=10)

    retour_button = tk.Button(header_frame, text="← Retour", command=menu_principal)
    retour_button.pack(side=tk.RIGHT, pady=10, padx=10)


    button_frame = tk.Frame(fenetre)
    button_frame.place(relx=0.5, rely=0.5, anchor='center')


    bouton1 = Button(button_frame,text = "Trier par nom",width=15, command=trier_nom)
    bouton1.pack(side=tk.LEFT, padx=10)
    bouton2 = Button(button_frame,text = "Trier par prix",width=15, command=trier_prix)
    bouton2.pack(side=tk.LEFT, padx=10) 
    bouton3 = Button(button_frame,text = "Trier par quantité",width=15, command=trier_quantite)
    bouton3.pack(side=tk.LEFT, padx=10)


def trier_nom():
    global produit
    
    fenetre.title('Trier par nom')
    fenetre.geometry("400x150")
    clear_window()



    chemin_fichier = recup_user()


    liste=trier_produit_nom(chemin_fichier)

    header_frame = tk.Frame(fenetre)
    header_frame.pack(fill=tk.X)


    label_header = tk.Label(header_frame, text="Trier par nom :", font=("Arial", 16, 'underline'))
    label_header.pack(side=tk.LEFT, pady=10, padx=10)

    retour_button = tk.Button(header_frame, text="← Retour", command=menu_produit)
    retour_button.pack(side=tk.RIGHT, pady=10, padx=10)

    hauteur_fenetre = 100 + len(liste) * 20
    fenetre.geometry(f"400x{hauteur_fenetre}")

    frame_commercants = tk.Frame(fenetre)
    frame_commercants.pack(fill=tk.BOTH, expand=True)

    style = ttk.Style()
    style.configure("Treeview.Heading", font=("Arial", 10, "bold"))
    tree = ttk.Treeview(frame_commercants, columns=("NOM", "PRIX", "QUANTITE"))


    tree.heading("NOM", text="Nom")
    tree.heading("PRIX", text="Prix")
    tree.heading("QUANTITE", text="Quantité")


    tree.column("NOM", width=150)
    tree.column("PRIX", width=100)
    tree.column("QUANTITE", width=100, anchor="center")

    tree["show"] = "headings"

    for i, produit in enumerate(liste, start=1):
        tree.insert("", "end", values=(produit))

    tree.pack(fill=tk.BOTH, expand=True)

def trier_prix():
    global produit
    
    fenetre.title('Trier par nom')
    fenetre.geometry("400x150")
    clear_window()



    chemin_fichier = recup_user()


    liste=trier_produit_prix(chemin_fichier)

    header_frame = tk.Frame(fenetre)
    header_frame.pack(fill=tk.X)


    label_header = tk.Label(header_frame, text="Trier par nom :", font=("Arial", 16, 'underline'))
    label_header.pack(side=tk.LEFT, pady=10, padx=10)

    retour_button = tk.Button(header_frame, text="← Retour", command=menu_produit)
    retour_button.pack(side=tk.RIGHT, pady=10, padx=10)

    hauteur_fenetre = 100 + len(liste) * 20
    fenetre.geometry(f"400x{hauteur_fenetre}")

    frame_commercants = tk.Frame(fenetre)
    frame_commercants.pack(fill=tk.BOTH, expand=True)

    style = ttk.Style()
    style.configure("Treeview.Heading", font=("Arial", 10, "bold"))
    tree = ttk.Treeview(frame_commercants, columns=("NOM", "PRIX", "QUANTITE"))


    tree.heading("NOM", text="Nom")
    tree.heading("PRIX", text="Prix")
    tree.heading("QUANTITE", text="Quantité")


    tree.column("NOM", width=150)
    tree.column("PRIX", width=100)
    tree.column("QUANTITE", width=100, anchor="center")

    tree["show"] = "headings"

    for i, produit in enumerate(liste, start=1):
        tree.insert("", "end", values=(produit))

    tree.pack(fill=tk.BOTH, expand=True)



def trier_quantite():
    global produit
    
    fenetre.title('Trier par nom')
    fenetre.geometry("400x150")
    clear_window()



    chemin_fichier = recup_user()


    liste=trier_produit_quantite(chemin_fichier)

    header_frame = tk.Frame(fenetre)
    header_frame.pack(fill=tk.X)


    label_header = tk.Label(header_frame, text="Trier par nom :", font=("Arial", 16, 'underline'))
    label_header.pack(side=tk.LEFT, pady=10, padx=10)

    retour_button = tk.Button(header_frame, text="← Retour", command=menu_produit)
    retour_button.pack(side=tk.RIGHT, pady=10, padx=10)

    hauteur_fenetre = 100 + len(liste) * 20
    fenetre.geometry(f"400x{hauteur_fenetre}")

    frame_commercants = tk.Frame(fenetre)
    frame_commercants.pack(fill=tk.BOTH, expand=True)

    style = ttk.Style()
    style.configure("Treeview.Heading", font=("Arial", 10, "bold"))
    tree = ttk.Treeview(frame_commercants, columns=("NOM", "PRIX", "QUANTITE"))


    tree.heading("NOM", text="Nom")
    tree.heading("PRIX", text="Prix")
    tree.heading("QUANTITE", text="Quantité")


    tree.column("NOM", width=150)
    tree.column("PRIX", width=100)
    tree.column("QUANTITE", width=100, anchor="center")

    tree["show"] = "headings"

    for i, produit in enumerate(liste, start=1):
        tree.insert("", "end", values=(produit))

    tree.pack(fill=tk.BOTH, expand=True)





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


def recup_user():
    
    nom_fichier = f"{username}.csv"
    chemin_fichier = os.path.join('data', nom_fichier)

    return chemin_fichier


def callback():
    type = 'exit'
    if username !='': 
        status = f"[X] {username} a quitter l'application"
    else :
         status = f"[X] L'utilisateur a quitter l'application"
    add_log(type,username,status)
    fenetre.destroy()









fenetre.protocol("WM_DELETE_WINDOW", callback)
menu_connexion()

fenetre.mainloop()



