import math
import numpy as np
import matplotlib.pyplot as plt

start = 0.0
end = 2*math.pi
number_of_points = 361
h = 1

vinkel_liste = np.linspace(start, end, 361)

def s(phi) -> float:
    if phi < math.pi / 2:
        phi = phi/(math.pi/2)
        return p(phi)
    if phi <= math.pi:
        return 2 * h
    if phi < math.pi + math.pi / 2:
        phi = phi/(math.pi/2)
        return q(phi)
    if phi <= 2 * math.pi:
        return h

def p(phi) -> float:
    return (6*phi**5 - 15*phi**4 + 10*phi**3 + h)

def q(phi) -> float:
    return p(3 - phi)

kam_x = []
kam_y = []
for vinkel in vinkel_liste:
    kam_y.append(s(vinkel))

print(kam_y)

plt.plot(vinkel_liste, kam_y, "o")
plt.show()


