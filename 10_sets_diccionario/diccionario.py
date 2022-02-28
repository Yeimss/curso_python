"""
Diccionario es un tipo de dato que almacena un conjuto de datos
en formato clave:valor, es parecido a un array asociativo en formato json
"""
persona={
    "nombre":"james",
    "apellidos":"herrera acevedo",
    "edad":20
}
print(persona)
print(persona["apellidos"])


#lista con diccionarios

contactos=[
    {
        'nombre':'antonio',
        'email':'antonio@antonio.com',
        'edad':28,
    },
    {
        'nombre':'pedro',
        'email':'pedro@pedro.com',
        'edad':28,
    },
    {
        'nombre':'luis',
        'email':'luis@luis.com',
        'edad':28,
    }
]

print(contactos[2]["email"])

for contacto in contactos:
    print(f"El nombre del contacto es: {contacto['nombre']}")
    print(f"El email del contacto es: {contacto['email']}")
    print(f"La edad del contacto es: {contacto['edad']}\n\n")
