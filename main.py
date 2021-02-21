from ohm import *
import ohm as o

_Paralelo = Circuito_Paralelo()
_Serie = Circuito_Serie()
circuito = 0

def suma_resistencias(tipo):
    if  tipo == 1:
        circuito = _Paralelo
    else:
        circuito = _Serie

    ingresa_resistencias = int(input("Cuantas resistencias son?: "))
    for i in range(ingresa_resistencias):
        circuito.__add__(int(input("Ingresa resistencia: ")))
    print(circuito.__RT__())


tipo_circuito = int(input(""" Ingresa el tipo de Circuito 1. Paralelo, 2.Serie """))
suma_resistencias(tipo_circuito)

        
