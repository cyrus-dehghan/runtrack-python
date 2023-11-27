def WC(marches, hauteur_marche):
    nombre_jours_semaine = 7
    nombre_allers_retours_par_jour = 2

    distance_parcourue = marches * hauteur_marche * nombre_allers_retours_par_jour * nombre_jours_semaine / 100  
    return distance_parcourue

nombre_marches = int(input("Veuillez entrer le nombre de marches du phare : "))
hauteur_marche = int(input("Veuillez entrer la hauteur de chaque marche en cm : "))

distance_parcourue = WC(nombre_marches, hauteur_marche)

print(f"Pour {nombre_marches} marches de {hauteur_marche} cm, le gardien parcourt {distance_parcourue:.2f} m par semaine.")