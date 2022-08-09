# Napisi program koji izracunava i ispisuje rastojanje izmedju
# tacaka zadatih svojim koordinatama.

# Ulaz: Sa standardnog ulaza unose se cetiri realna broja,svaki
# u posebnom redu. Prva dva broja Ax i Ay predstavljaju
# koordinate tacke A= (Ax,Ay), dok druga dva broja Bx i By 
# predstavljaju koordinate tacke B=(Bx,By).

# Izlaz: Na standardni izlaz ispisati jedan realan broj koji
# predstavlja rastojanje izmedju tacaka A i B, zaokruzen na pet
# decimala.

import math

ax = float(input("tacka ax"))
ay = float(input("tacka ay"))
bx = float(input("tacka bx"))
by = float(input("tacka by"))
d=math.sqrt((bx-ax)**2+(by-ay)**2)
print(format(d,'.5f'))