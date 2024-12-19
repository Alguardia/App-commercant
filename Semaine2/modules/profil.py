import os
import pandas as pd
import hashlib
import pwnedpasswords

def haveibeenpwnd_password():
    print("1) Vérification de mot de passe compromis")
    password = input("Mettre votre mot de passe :")
    pwnded_password = pwnedpasswords.check(password)
    print(f"Votre mot de passe a été compromis : {pwnded_password}")

haveibeenpwnd_password()




