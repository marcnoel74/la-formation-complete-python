# Demander à l'utilisateur d'entrer un nombre
# Afficher le résultat de l'addition de ce nombre avec le nombre a.
# Par exemple : "Le résultat de l'opération est 15" (dans le cas où l'utilisateur entre le nombre 5)

a = 10

nombre_utilisateur = int(input('Entrez un nombre :'))
print(f'Le résultat de l\'addition de {a} et {nombre_utilisateur} vaut : {a + nombre_utilisateur}')
