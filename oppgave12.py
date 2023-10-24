import math
import numpy as np
import matplotlib.pyplot as plt

start = 0.0
end = 2*math.pi
number_of_points = 361
h = 1

# Lager 361 punkter mellom start og slutt
vinkel_liste = np.linspace(start, end, 361)

def s(phi: float) -> float:
    #s som definert i oppgaveteksten oppg 8
    """Tar imot en vinkel mellom 0 og 4"""
    if phi < 1:
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

kam_y = []

#Evaluer funksjonen s for punktene og lagre dem i en liste
for vinkel in vinkel_liste:
    # s tar imot et tall mellom 0 og 4 og vi deler derfor på pi/2 (se oppg 11 for forklaring)
    vinkel = vinkel / (math.pi/2)
    kam_y.append(s(vinkel))

print(kam_y)

#plot funksjonen
plt.plot(vinkel_liste, kam_y, "o")
plt.xticks([0, math.pi/2, math.pi, 3* math.pi / 2, 2 * math.pi], ['0', 'π/2', 'π', '3π/2', '2π'])
plt.yticks([1, 2], ["1h", "2h"])
plt.title("s evaluert mellom 0 og 2π")
plt.show()


