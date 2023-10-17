

# Oppgave 6

Begrunn hvorfor det er 5. grad polynom

> Begrunnelse for 5. gradspolynom
i betingelsene har vi fått vite at den deriverte og den andrederiverte to nullpunkter i samme punkt ($x=0$ og $x=1$), når den andredervierte er lik 0, betyr det at det er et topp, bunn eller terrassepunkt for den deriverte. Hvis funksjonen skal være definert for hele intervallet, så må det være et topppunkt for den deriverte mellom disse to punktene

Hvis det er mer kan du ikke lage systemet av likninger.

Hvis det er mer enn fem grader vil de ekstra konstantene kunne være alle reele tall

Femte grad gir ikke de konstantene.

Funksjonen må også ha mer enn tre pga. to røtter i andre deriverte og to røtter i første.



Likningene vi har:

1.   $p(φ)=c_5x^5+c_4x^4+c_3x^3+c_2x^2+c_1x+c_0$

2.   $p'(φ)=5c_5x^4+4c_4x^3+3c_3x^2+2c_2x+c_1$

3.   $p''(φ)=20c_5x^3+12c_4x^2+6c_3x+2c_2$



Vi har også følgende betingelser satt ut:

$p(0)=h,    p(1)=2h,    p'(0)= 0,    p'(1)= 0,    p''(0)= 0,    p''(1)= 0$



Utifra det kan vi utlede:

    $p(0)= h=c_0$

    $p'(0)= 0 = c_1$

    $p''(0)=0=c_2$



Likningene blir dermed nå:

    $p(φ)=c_5φ^5+c_4φ^4+c_3φ^3+h$

    $p'(φ)=5c_5φ^4+4c_4φ^3+3c_3φ^2$

    $p''(φ)=20c_5φ^3+12c_4φ^2+6c_3φ$



Vi kan videre utlede et system av 3 likninger med 3 ukjente:

$p(1)=2h= c_5+c_4+c_3+h$

4.     $c_5+c_4+c_3 = h$



$p'(1)=0= 5c_5+4c_4+3c_3$

5.     $5c_5+4c_4+3c_3 = 0$



$p''(1)= 0 = 20c_5+12c_4+6c_3$

6.     $20c_5+12c_4+6c_3 = 0$



Likning fem utledet for $c_5$:

$c_5=-\frac{4}{5}c_4-\frac{3}{5}c_3$



Likning fem i likning fire:

$-\frac{4}{5}c_4-\frac{3}{5}c_3+c_4+c_3 = h$

$c_4+2c_3=5h$



Utledet for $c_4$:

$c_4=5h-c_3$



Likning x i likning seks:

$20(-\frac{4}{5}c_4-\frac{3}{5}c_3)+12c_4+6c_3 = 0$

$c_4=-\frac{3}{2}c_3$



$-\frac{3}{2}c_3=5h-c_3$

$c_3=10h$



Likning $c_3$ i likning x:

$c_4=-\frac{3}{2}10h$

$c_4=-15h$



Likning fire med $c_4$ og $c_3$:

 $c_5-15h+10h = 1h$

$c_5=6h$



Likningen blir da:

$p(φ)=6φ^5-15φ^4+10φ^3+h$



Funker for alle betingelsene testet i geogebra med $h=1$.

Bare skriv om likningene slik at det er h istedet for tall



# Oppgave 7

Rykket vil bli kalkulert ved bruk av tredje deriverte av $p(x)$:

$p'''(φ)=360φ^2-360φ+60$



Rykket i $p(0)$ vil være:

$p'''(0)=60$



Rykket i p(1)

$p'''(1)=360-360+60$

$p'''(1)=60$



# Oppgave 8



![](C:\Users\gabriel\AppData\Roaming\marktext\images\2023-10-09-19-07-06-image.png)



$q(\phi)= 6(\phi-2)^5-15(\phi-2)^4+10(\phi-2)^3+4$

eller

$q(\phi)=-p(\phi-2)+3$



kom fram til det i testing
