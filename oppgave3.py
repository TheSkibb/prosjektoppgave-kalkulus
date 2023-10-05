import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0.0, 4.0, 101) # 101 as then 0 is included
h = 1

def derivert(x):
    y = []
    for element in x:
        if element >= 0 and element <= 1:
            y.append(h)
        if element > 1 and element < 2:
            y.append(0)
        if element >= 2 and element <= 3:
            y.append(-h)
        if element > 3 and element <= 4:
            y.append(0)
    return y


y = derivert(x)

print(len(y))
print(len(x))
#plt.xlim(0, max(x))
plt.plot(x, y, "o")
plt.show()
