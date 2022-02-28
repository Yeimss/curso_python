cantantes=['2pac','axel', 'di caprio', 'toreto']
numeros=[1, 4,5,7,2,56,32,8,10]



#ordenar lista
print(numeros)
numeros.sort()
print(f"{numeros}\n")


#añadir elementos
cantantes.append("porta")
cantantes.append("axel")

print(cantantes)
cantantes.insert(2, "David Bisbal")
print(f"{cantantes}\n")


#eliminar elementos
cantantes.pop(4)
print(cantantes)
cantantes.remove("axel")
print(f"{cantantes}\n")



#dar la vuelta / permutar / cambiar el orden / poner al reves
print(f"\n{numeros}")
numeros.reverse()
print(f"{numeros}\n")


#Buscar en una lista
print('2pac' in cantantes)

#contar elementos
print(len(cantantes))

for x in cantantes:
    print(f"{cantantes.index(x)}: {x}")


#¿cuantas veces aparece un elemento?
print(f"\n{numeros.count(8)}")
numeros.append(8)
print(f"{numeros.count(8)}\n")



#conseguir indice
print(cantantes.index('2pac'))
print(cantantes.index('axel'))

#unir listas
cantantes.extend(numeros)
print(cantantes)
cantantes.reverse()
print(cantantes)

