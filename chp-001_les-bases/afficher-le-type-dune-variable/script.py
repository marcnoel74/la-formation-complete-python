number_exo = input("Entrez un nombre: ")
print(type(number_exo))  # retourne <class 'str'>. La fonction input retourne toujours une chaîne de caractères.

# Vous pouvez par la suite convertir la variable nombre en nombre entier grâce à la fonction int
number_exo = int(number_exo)
print(type(number_exo))  # retourne <class 'int'>. La variable a bien été convertie.