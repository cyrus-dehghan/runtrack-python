def chiffres():
    L = [1, 2, 3, 4, 5]
    
    print (L)

    print(L[1])

    remplacer_par_somme(L)

    print(L)

    print(L[-1])

def remplacer_par_somme(liste):
    if len(liste) >= 5:
        liste[3] = liste[2] + liste[4]

chiffres()
