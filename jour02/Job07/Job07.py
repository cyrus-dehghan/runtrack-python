chaine = "abcdefghijklmnopqrstuvwxyz"[:26]

pyramide = ""
for i in range(1, len(chaine) + 1):
    partie_gauche = chaine[:i]
    ligne = partie_gauche
    pyramide += ligne + "\n"

print(pyramide)