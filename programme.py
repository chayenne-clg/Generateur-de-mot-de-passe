import random
import string

print("=== Générateur de mots de passe ===")

#Demande à l'utilisateur la longueur du mot de passe et les types de caractères à inclure
longueur = int(input("Longueur du mot de passe : "))
majuscules = input("Inclure des majuscules ? (o/n) : ").lower()
chiffres = input("Inclure des chiffres ? (o/n) : ").lower()
speciaux = input("Inclure des caractères spéciaux ? (o/n) : ").lower()

caracteres = string.ascii_lowercase

#En fonction des choix de l'utilisateur, ajoute les types de caractères correspondants à la variable "caracteres"
if majuscules == "o":
    caracteres += string.ascii_uppercase

if chiffres == "o":
    caracteres += string.digits

if speciaux == "o":
    caracteres += string.punctuation

mot_de_passe = ""

#Génère le mot de passe en choisissant aléatoirement des caractères dans la variable "caracteres" pour la longueur choisie par l'utilisateur
for i in range(longueur):
    mot_de_passe += random.choice(caracteres)

#Renvoie le mot de passe généré à l'utilisateur
print("\nMot de passe généré :")
print(mot_de_passe)
