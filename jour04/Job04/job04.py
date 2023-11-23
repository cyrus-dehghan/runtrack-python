def mango():
    fruits = ["pomme", "cerise", "orange", "Melon"]
    if "orange" in fruits:
        index_orange = fruits.index("orange")

        fruits[index_orange] = "Mangue"
    
    return fruits

liste_fruits = mango()

print(liste_fruits)