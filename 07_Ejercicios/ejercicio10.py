"""
recibir la nota de 15 alumnos y que al final diga cuantos han aprobado y cuantos han perdido
"""
aprobados=0
reprobados=0

for alumno in range(0,15):
    nota=float(input(f"Ingrese la nota del alumno {alumno}: "))
    if nota>=3:
        aprobados+=1
    else:
        reprobados+=1

print(f"La cantidad de alumnos que reprobaron es: {reprobados}")
print(f"La cantidad de alumnos que aprobaron es: {aprobados}")