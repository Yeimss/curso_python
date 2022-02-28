mi_texto="master"
#mi-texto2="python"#está mal crar variables con un -
mi_texto2="en \"Python\""

#se pueden unir variables

texto_unido=mi_texto+" "+mi_texto2
print(texto_unido)


#valores especiales dentro de los trings
texto_unido=mi_texto+" \n "+mi_texto2 #\n sirve para un salto de linea
print(texto_unido)

texto_unido=mi_texto+" \t "+mi_texto2 #\t una tabulacion en el string
print(texto_unido)

texto_unido=mi_texto+" \r "+mi_texto2 #\r borra todo lo que haya antes de este caracter especial
print(texto_unido)
