"""Formulas
   Potencia V*i, V^2 / R, R*i^2
   Intensidad  V/R, P/V, 
   RESISTENCIA V/I, 
   tension R*I, P/I
"""

def _I_(v,r):
    print("La intensidad es de ", v / r)

def _V_(i,r):
    print("El voltaje es de ", i* r)

def _R_(v, i):
    print("La resistencia es de ", v / i)

class Circuito_Paralelo():
    def __init__(self):
        self._Resistencias = []
        self._Suma = 0

    def __add__(self, resistencia):
        self._Resistencias.append(resistencia)


    def __RT__(self):
        for i in self._Resistencias:
            self._Suma += 1/i 
            suma_total = 1/self._Suma
        print(f"La resistencia total del circuito es {suma_total}")


class Circuito_Serie():
    def __init__(self):
        self._Resistencias = []
        self._Suma = 0
    def __add__(self, resistencia):
        self._Resistencias.append(resistencia)

    def __RT__(self):
        for i in self._Resistencias:
            self._Suma += i
        print(f"La resistencia total es {self._Suma}")

