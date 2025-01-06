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
fenetre.title('Authentification')


def login_inter():
    if login(entrée1, entrée2):
                password=entrée2.get()
                password_compromise = password_compromises(password)
                print(password_compromise)
                menu_principal(password_compromise)
    

def menu_connexion():

    global entrée1, entrée2
    clear_window()
    fenetre.title('Authentification')
    texte1 = Label(fenetre, text = "Nom d'utilisateur : ")
    texte1.place(x = 20, y = 20)
    entrée1 = Entry(fenetre)
    entrée1.place(x = 150, y = 20)
    texte2 = Label(fenetre,text = "Mot de passe : ")
    texte2.place(x = 20, y = 60)
    entrée2 = Entry(fenetre, show="*")
    entrée2.place(x = 150, y = 60)

    bouton1 = Button(fenetre,text = "Gestion du compte", command=menu_gestion_compte)
    bouton1.place(x = 280, y = 100)
    bouton2 = Button(fenetre,text = "Crée un compte", command=menu_register)
    bouton2.place(x = 180, y = 100)
    bouton3 = Button(fenetre,text = "Se connecter", command=login_inter)
    bouton3.place(x = 90, y = 100)
    bouton4=Button(fenetre,text="Quitter",command = fenetre.destroy )
    bouton4.place(x = 30, y = 100 )




def register_inter():
    global fenetre, entrée1_register , entrée2_register 
    
    register(entrée1_register,entrée2_register, fenetre)
    

        
def menu_register():
    global fenetre, entrée1_register , entrée2_register 
    clear_window()
    fenetre.title('Crée un compte')

    texte1 = Label(fenetre, text = "Nom d'utilisateur : ")
    texte1.place(x = 20, y = 20)
    entrée1_register = Entry(fenetre)
    entrée1_register.place(x = 150, y = 20)
    texte2 = Label(fenetre,text = "Mot de passe : ")
    texte2.place(x = 20, y = 60)
    entrée2_register = Entry(fenetre, show="*")
    entrée2_register.place(x = 150, y = 60)

    bouton1 = Button(fenetre,text = "Crée un compte", command=register_inter)
    bouton1.place(x = 90, y = 100)
    bouton2=Button(fenetre,text="Quitter",command = menu_connexion)
    bouton2.place(x = 30, y = 100 )



def menu_principal(password_compromise):
    global fenetre
    clear_window()
    fenetre.title('Menu principal')

    if password_compromise:
        password_status = "[X] Votre mot de passe est compromis.\n[!] Aller dans la rubrique Profil pour changer votre mot de passe."
        label_password = tk.Label(fenetre, text=password_status, fg="red")
    else:
        password_status = "[✓] Votre mot de passe est sécurisé."
        label_password = tk.Label(fenetre, text=password_status, fg="green")

    label_password.place(x=20, y=10)  


    bouton_profil = tk.Button(fenetre, text="Profil", width=15, command=menu_profil)
    bouton_profil.place(x=20, y=60)

    bouton_produit = tk.Button(fenetre, text="Vos produits", width=15, command=menu_produit)
    bouton_produit.place(x=150, y=60)

    bouton_quitter = tk.Button(fenetre, text="Quitter", width=15, command=menu_connexion)
    bouton_quitter.place(x=280, y=60)

    
    fenetre.mainloop()

def menu_profil():
     test="test"

def menu_produit():
     test="test"

def menu_gestion_compte():

    global fenetre
    clear_window()
    fenetre.title('Gestion du compte')
     
    bouton_supprimer = tk.Button(fenetre, text="Supprimer compte", width=15, command=menu_supprimer_utilisateur)
    bouton_supprimer.place(x=20, y=60)

    bouton_liste_commercant = tk.Button(fenetre, text="Liste commercants", width=15, command=menu_liste_commercant)
    bouton_liste_commercant.place(x=150, y=60)

    bouton_quitter = tk.Button(fenetre, text="Quitter", width=15, command=menu_connexion)
    bouton_quitter.place(x=280, y=60)

def menu_supprimer_utilisateur():
    global fenetre, entrée1_remove , entrée2_remove
    clear_window()
    fenetre.title('Supprimer un compte')

    texte1 = Label(fenetre, text = "Nom d'utilisateur : ")
    texte1.place(x = 20, y = 20)
    entrée1_remove = Entry(fenetre)
    entrée1_remove.place(x = 150, y = 20)
    texte2 = Label(fenetre,text = "Mot de passe : ")
    texte2.place(x = 20, y = 60)
    entrée2_remove = Entry(fenetre, show="*")
    entrée2_remove.place(x = 150, y = 60)

    bouton1 = Button(fenetre,text = "Supprimer un compte", command=supprimer_user_inter)
    bouton1.place(x = 90, y = 100)
    bouton2=Button(fenetre,text="Quitter",command = menu_connexion)
    bouton2.place(x = 30, y = 100 )

def supprimer_user_inter():
    global fenetre, entrée1_remove , entrée2_remove 
    supprimer_user(entrée1_remove,entrée2_remove, fenetre)


def menu_liste_commercant():
    clear_window()
    fenetre.title('Liste des commerçants')

    commercants = liste_commercants(fenetre)

    frame_canvas = tk.Frame(fenetre)
    frame_canvas.pack(fill=tk.BOTH, expand=True)

    canvas = tk.Canvas(frame_canvas)
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    scrollbar = tk.Scrollbar(frame_canvas, orient=tk.VERTICAL, command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    canvas.configure(yscrollcommand=scrollbar.set)

    frame_labels = tk.Frame(canvas)
    canvas.create_window((0, 0), window=frame_labels, anchor="nw")

    label_header = tk.Label(frame_labels, text="Liste des commerçants", font=("Arial", 16))
    label_header.grid(row=0, column=0, pady=10)

    for commercant in commercants:
        label_commercant = tk.Label(frame_labels, text=f"- {commercant}", font=("Arial", 12), anchor="w")
        label_commercant.place(x=12, column=0, sticky="w", padx=10, pady=5)
        y_position += 1

    frame_labels.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))
    canvas.bind_all("<MouseWheel>", lambda event: on_mouse_wheel(event, canvas))
    bouton_quitter = tk.Button(fenetre, text="Quitter", width=15, command=menu_connexion)
    bouton_quitter.place(pady=10)
    


def on_mouse_wheel(event, canvas):
    canvas.yview_scroll(int(-1*(event.delta/120)), "units")
   



def clear_window():
   
    for widget in fenetre.winfo_children():
        widget.place_forget()





menu_connexion()

fenetre.mainloop()



