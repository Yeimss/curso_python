"""
todas las tablas del 1 al 10
"""

for multiplicando in range (1,11):
    multiplicador=1
    print(f"\n\n\n------------TABLA DEL {multiplicando}------------\n")
    while multiplicador<=10:
        producto=multiplicando*multiplicador
        print(f"{multiplicando} * {multiplicador} = {producto}")
        multiplicador+=1
    
else:
    print("\nesas son todas las tablas del 1 al 10\n")