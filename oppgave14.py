import math
import numpy as np
import matplotlib.pyplot as plt

start = 0.0
end = 2*math.pi
number_of_points = 361
h = 1

vinkel_liste = np.linspace(start, end, 361)

def s(phi) -> float:
    """Tar imot en vinkel mellom 0 og 4"""
    #s som definert i oppgaveteksten oppg 8
    if phi < 1:
        print(phi)
        return p(phi)
    if phi <= 2:
        return 2 * h
    if phi < 3:
        return q(phi)
    if phi <= 4:
        return h
    #unreachable
    return 0

def p(phi) -> float:
    """p funksjon fra oppgave 6"""
    return (6*phi**5 - 15*phi**4 + 10*phi**3 + h)

def q(phi) -> float:
    """q funksjon fra oppgave 8"""
    return p(3 - phi)

kam_x = []
kam_y = []
for vinkel in vinkel_liste:
    # s tar imot et tall mellom 0 og 4 og vi deler derfor på pi/2 (se oppg 11 for forklaring)
    kam_y.append(math.sin(vinkel)*s(vinkel/(math.pi/2)))
    kam_x.append(math.cos(vinkel)*s(vinkel/(math.pi/2)))

plt.plot(kam_x, kam_y, "o")
plt.show()



