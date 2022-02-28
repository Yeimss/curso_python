print("************* LISTA DE CONTACTOS *************")
contactos=[
    [
        'Antonio',
        58,
        'antonio@gmail.com'
    ],
    [
        'Luis',
        40,
        'Luis@gmail.com'
    ],
    [
        'sergio',
        26,
        'sergio@gmail.com'
    ],
    [
        'mayi',
        36,
        'mayi@gmail.com'
    ],
    [
        'majo',
        23,
        'majo@gmail.com'
    ],
    [
        'marcos',
        14,
        'marcos@gmail.com'
    ],
]

for contacto in contactos:
    for elemento in contacto:
        if contacto.index(elemento)==0:
            print(f"Nombre: {elemento}")
        elif contacto.index(elemento)==1:
            print(f"Edad: {elemento}")
        elif contacto.index(elemento)==2:
            print(f"Correo: {elemento}")
    print("\n")


print(contactos[3])