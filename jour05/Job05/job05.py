def Cesar(message, decalage):
    resultat = ""
    for char in message:
        if char.isalpha():
            if char.isupper():
                resultat += chr((ord(char) - ord('A' ) + decalage) % 26 + ord('A'))
            else:
                resultat += chr((ord(char) - ord('a' ) + decalage) % 26 + ord('a'))
        else:
            resultat += char
    return resultat

message_original = "Ceci est un message codé."
decalage = 3
message_code = Cesar(message_original, decalage)

print("Message original:", message_original)
print("Message codé:", message_code)