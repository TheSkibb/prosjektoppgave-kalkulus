import math
import numpy as np
import matplotlib.pyplot as plt

start = 0.0
end = 2*math.pi
number_of_points = 361
h = 1

x_axis = np.linspace(start, end, 361)

def s(phi):
    if phi < math.pi / 2:
        return p(phi)
    if phi <= math.pi:
        return 2 * h
    if phi < math.pi + math.pi / 2:
        return q(phi)
    if phi <= 2 * math.pi:
        return h

def p(phi):
    return (6*phi**5 - 15*phi**4 + 10*phi**3 + h)

def q(phi):
    return p(3 - phi)

y = []
for x in x_axis:
    y.append(s(x))

print(y)

plt.plot(x_axis, y, "o")
plt.show()


