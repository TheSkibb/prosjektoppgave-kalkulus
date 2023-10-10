[Flyttet til](file:///home/kristian/skolearbeidUiA/matte/prosjektoppgave-kalkulus/prosjektOppgave.md)
## oppgave 1

Finne $c_0$ og $c_1$
Løste ved å sette inn i funksjonen
$$
s(0)=c_0+c_1*0=h \Leftrightarrow c_0 = h
$$
setter så $c_0=h$ inn i den for å finne $c_1$
$$
s(1)=h+c_1*1=2h \Leftrightarrow c_1=h
$$
vi har dermed $c_0=h$ og $c_1=h$

Finne $d_0$ og $d_1$
Løser ved å sette opp ligningssett
$$
\text{I } d_0+2d_1=2h
$$
$$
\text{II } d_0+3d_1=h
$$

vi finner $d_0$ i Ligning I
$$
\text{I } d_0+2d_1=2h \Leftrightarrow d_0=2h-2d_1
$$

setter $d_0$ inn i ligning II og finner $d_1$
$$
\text{II } 2h-2d_1+3d_1=h \Leftrightarrow d_1=-h
$$

setter $d_1=-1$ inn i ligning I og får:
$$
\text{I } d_0+2*-h=2h \Leftrightarrow d_0 = 4h
$$

## oppgave 2

Hastigheten for funksjonen er definert for de fire intervallene er:

for intervallet $[0,1]$ er funksjonen $s(\Phi)=h+h\Phi$
$$
v=s'(\Phi)=h
$$
for intervallet $(1,2)$ er funksjonen $s(\Phi)=2h$
$$
v=s'(\Phi)=0
$$
for intervallet $[2,3]$ er funksjonen $s(\Phi)=4h-h\Phi$
$$
v=s'(\Phi)=-h
$$
for intervallet $(3,4)$ er funksjonen $s(\Phi)=h$
$$
v=s'(\Phi)=0
$$

i punktene 1, 2, 3 og 4 så er ikke $v$ definert. Dette er fordi den deriverte er definert ved formen $\lim_{h\to0}\frac{f(x+h)-f(x)}{h}$, denne grensa er ikke definert i 1, 2, 3 og 4 fordi i disse punktene så er grensene definert forskjellig ettersom hvilken side man er på.

## Oppgave 3

## Oppgave 4

Betingelsene sier at vi har et punkt med to forskjellige punkter hvor vi vet at den deriverte er $0$, en 2-gradsfunksjone kan kun ha ett punkt hvor den deriverte er $0$, derfor vet vi at $n$ må minst være $3$

Vi finner koeffesientene ved å sette inn betingelsene i grafene våre

Vi har:
$$
p(\Phi) = c_0 + c_1\Phi + c_2\Phi^2 + c_3\Phi^3
$$

$$
p(\Phi) = c_1 + 2c_2\Phi + 3c_3\Phi^2
$$

Vi setter inn betingelsen $p(0)=h$ i $p(\phi)$

$$
p(0) = c_0 + c_1*0 + c_2*0^2 + c_3*0^3 \Leftrightarrow c_0 = h
$$

Vi setter inn betingelsen $p'(0)=0$ i $p'(\Phi)$
$$
p(0) = c_1 + 2c_2*0 + 3c_3*0^2 \Leftrightarrow c_1 = 0
$$

Ved å dette inn betingelsene $p(1)=2h$ og $p'(1)=0$ har vi nå et ligningssett med to ukjente

$$
\text{I } 2h = h + 0 + c_2 + c_3 \Leftrightarrow h = c_2 + c_3
$$

$$
\text{II } 0 = 0 + 2c_2 + 3c_3 \Leftrightarrow 2c_2 + 3c_3 = 0
$$

Finner $c_2$ uttrykt ved $c_3$ i ligning $I$
$$
h = c_2 + c_3 \Leftrightarrow c_2 = h - c_3
$$

Setter $c_2$ inn i ligning $II$
$$
2c_2 + 3c_3 = 0 \Leftrightarrow 2(h-c_3) + 3c_3 = 0 \Leftrightarrow -2h + 3c_3 = -2h \Leftrightarrow c_3 = -2h
$$

Setter $c_3$ inn i ligning $I$
$$
h=c_2-2h \Leftrightarrow c_2 = 3h
$$

Vi ender opp med polynomet
$$
p(\Phi)=h+3x^2-2x^3
$$


