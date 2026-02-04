operacion = input()

terminos = []
actual = ""

for i in range(len(operacion)):
    c = operacion[i]

    if (c == "+" or c == "-") and i != 0:
        terminos.append(actual)
        actual = c
    else:
        actual += c

terminos.append(actual)

print(terminos)

'''
#coef = ""
#indice = ""
before = True

for c in terminos[0]:
    if c == "i":
        before = False
    else:
        if before:
            coef += c
        else:
            indice += c

print(coef)
print(indice)


partes = terminos[0].split("i")

coef = int(partes[0])
indice = int(partes[1])

print(coef)
print(indice)
'''

