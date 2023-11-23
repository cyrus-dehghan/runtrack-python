def cinqfruitsetlégumes (type, saison):
    if type=="fruits":
        if saison=="hiver":
            print ("orange, mandarine et kiwi")
        elif saison=="ete":
            print ("Poire, fraise, cassis")
        else:
            print ("autre")
    elif type=="legume":
        if saison=="hiver":
            print ("carotte, topinambour, endive")
        elif saison=="ete":
            print ("artichaut, aubergine,navet")
    else:
        print ("fraise, framboise, myrtille")

cinqfruitsetlégumes("fruits", "hiver")
cinqfruitsetlégumes("fruits", "ete")
cinqfruitsetlégumes("legume", "hiver")
cinqfruitsetlégumes("legume", "ete")