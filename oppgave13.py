"""
samme som oppgave 12, bortsett fra at vi har fjernet plottingen og satt h=5 for å tegne kamskiven på rutepapir hvor 2h = 10cm
"""

import math

# h er satt til 5 for å tegne det på et ark hvor 2h = 10cm
h = 5

def s(phi: float) -> float:
    """Tar imot en vinkel mellom 0 og 4"""
    #s som definert i oppgaveteksten oppg 8
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

# lag en liste med
degreeslist = list(range(0, 361, 10))

for degree in degreeslist:
    #konverter grader til radianer l
    # s tar imot et tall mellom 0 og 4 og vi deler derfor på pi/2 (se oppg 11 for forklaring)
    radian = math.radians(degree)

    print(degree, (s(radian/(math.pi/2))))


