def verso(liste):
    if len(liste) > 0:
        liste[0], liste[-1] = liste[-1], liste[0]

ma_liste = [1, 2, 3, 4, 5]

print(ma_liste)

verso(ma_liste)

print(ma_liste)