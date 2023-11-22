def pair_impair (nb):
    if nb>0 and isinstance(nb, int):
        if nb%2==0:
            print ("pair")
        else:
            print ("impair")
    else:
        print ("erreur")

pair_impair (18)
pair_impair (19)
pair_impair (-9)
pair_impair (9.9)   