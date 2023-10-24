import math

h = 5
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

def x(phi):
    return math.sqrt((s(phi))**2-(s(phi))**2*math.sin(phi))

def y(phi):
    return math.sqrt(s(phi)**2-s(phi)**2*math.cos(phi))
"""
def x(phi):
    return math.cos(phi)*s(phi)

def y(phi):
    return math.sin(phi)*s(phi)
"""

degreeslist = list(range(0, 361, 10))

for degree in degreeslist:
    radian = math.radians(degree)
    print(degree, (s(radian)))


