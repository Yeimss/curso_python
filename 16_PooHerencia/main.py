import clases

persona= clases.Persona()
persona.setNombre("James")
persona.setAltura("190cm")
persona.setApellido("Herrera")
persona.setEdad(21)

print(f"{persona.getNombre()} {persona.getApellido()} tiene {persona.getEdad()} años y mide {persona.getAltura()}")
print("\n----------------------------------------------------\n")

##vamos a instanciar un objeto de la clase informatico

desarrollador=clases.Informatico()
desarrollador.setNombre("Yesid")
desarrollador.setAltura("172cm")
desarrollador.setApellido("Acevedo")
desarrollador.setEdad(21)

print(f"el informatico es: {desarrollador.getNombre()}")
print(f"Y sabe los lenguajes: {desarrollador.getLenguajes()}")
print("\n----------------------------------------------------\n")


tecnico=clases.TecnicoRedes()
tecnico.setNombre("Mauricio")

print(f"Tecnico: {tecnico.getNombre()}\nExperiencia en redes: {tecnico.getExperienciaRedes()}")
print("")




