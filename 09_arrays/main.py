peliculas=["spiderman", "narnia", "el señor de los anillos", "trolls", "merlin"]
cantantes=list(('2pac','axel', 'di caprio', 'toreto'))
years=list(range(2020, 2050))
variada=["Karonte", 20, 1000.2, True, "Jeje"]

#indices
print("\n"+peliculas[1])
print(cantantes[-3])
print(peliculas[1:4])
print(f"{peliculas[1:]}\n\n")


#modificar indices
cantantes[2]="Julio Jaramillo"
print(cantantes[2]+"\n")


#añadir elementos a la lista
cantantes.append("Kase O")
cantantes.append("Mario b")
print(f"{cantantes}\n\n")

#recorrer lista
nueva_pelicula=""
while nueva_pelicula != "parar":
    nueva_pelicula=input("\n\nIngrese una nueva pelicula: ")
    if nueva_pelicula.upper()!= "PARAR":
        peliculas.append(nueva_pelicula)

    for x in peliculas:
        print(f"{peliculas.index(x)+1}. {x}")