import math
import numpy as np
import matplotlib.pyplot as plt

start = 0.0
end = 2*math.pi
number_of_points = 361
h = 1

vinkel_liste = np.linspace(start, end, 361)

def s(phi) -> float:

    #konverter så gradene faller innenfor intervallet 0, 4
    phi = phi/(math.pi/2)

    if phi < 1:
        return p(phi)
    if phi <= 2:
        return 2 * h
    if phi < 3:
        return q(phi)
    #if phi <= 4:
    else:
        return h

def p(phi) -> float:
    return (6*phi**5 - 15*phi**4 + 10*phi**3 + h)

def q(phi) -> float:
    return p(3 - phi)

kam_y = []

for vinkel in vinkel_liste:
    kam_y.append(s(vinkel))

print(kam_y)

plt.plot(vinkel_liste, kam_y, "o")
plt.xticks([0, math.pi/2, math.pi, 3* math.pi / 2, 2 * math.pi], ['0', 'π/2', 'π', '3π/2', '2π'])
plt.show()


