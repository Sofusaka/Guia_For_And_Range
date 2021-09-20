frase=input('Ingrese una frase: ')
print('Las vocales de la frase son: ')

for i in "aeiou":

    if i in frase.lower:
        print(i)
