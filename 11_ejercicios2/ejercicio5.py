"""
crear una lista con el contenido de esta tabla

ACCION  AVENTURA            DEPORTES
GTA     Assasins creed      Fifa 21
COD     Crash               Moto GP
PUGB    Prince of persia    Forza Horizon
"""

tabla=[
    {
        'Categoria':"Acción",
        'Juegos':['GTA', 'Paladins', 'PugB']
    },
    {
        'Categoria':"Aventura",
        'Juegos':['Assasins Cred', 'Crash', 'Prince of persia']
    },
    {
        'Categoria':"Deportes",
        'Juegos':['Fifa 21', 'Moto GP', 'Forza Horizon']
    }
]


tabla2=[
    {
        'Videojuegos':[
            {
                'Categoria':"Acción",
                'Juegos':['GTA', 'Paladins', 'PugB']
            },
            {
                'Categoria':"Aventura",
                'Juegos':['Assasins Cred', 'Crash', 'Prince of persia']
            },
            {
                'Categoria':"Deportes",
                'Juegos':['Fifa 21', 'Moto GP', 'Forza Horizon']
            }
        ]
    }
]

for categoria in tabla2[0]["Videojuegos"]:
    print(f"-------------{categoria['Categoria']}------------")
    contador=1
    for juego in categoria['Juegos']:
        print (f"{contador}. {juego}")
        contador+=1
    print("\n\n")