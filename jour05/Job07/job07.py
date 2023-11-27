def Luke(liste_notes):
    notes_arrondies = []

    for note in liste_notes:
        if note < 40:
            notes_arrondies.append(note)
        else:
            prochain_multiple_5 = (note // 5 + 1) * 5

            if prochain_multiple_5 - note < 3:
                notes_arrondies.append(prochain_multiple_5)
            else:
                notes_arrondies.append(note)

    return notes_arrondies

liste_notes = [83, 68, 42, 99, 76, 23]
notes_arrondies = Luke(liste_notes)

print("Notes d'origine :", liste_notes)
print("Notes arrondies :", notes_arrondies)