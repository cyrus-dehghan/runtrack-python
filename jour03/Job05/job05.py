def calcule (n1, operator, n2):
    if operator=="+":
        return n1 + n2
    elif operator=="-":
        return n1-n2
    elif operator=="*":
        return n1*n2
    elif operator=="/":
        return n1//n2
    elif operator=="%":
        return n1%n2

print (calcule(8,"+",1))
print (calcule(10,"-",1))
print (calcule(9,"*",1))
print (calcule(18,"/",2))
print (calcule(9,"%",9))