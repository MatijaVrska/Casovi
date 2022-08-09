#Napisati program kojim se izracunava potrebna duzina trake za
#porub stolnjaka kruznog oblika cija je povrsina P.
#kruznog oblika cija je povrsina P.

# Ulaz: U liniji standardnog ulaza se nalazi realna vrednost
# P(1<=P<=1000)
# Potrebna duzina trake za porub
# (realan broj zaokruzen na dve decimale).

import math

P= float(input("povrsina trake stolnjaka kruznog oblika"))
r=math.sqrt(P/math.pi)
O=2*r*math.pi
print(format(O,'.2f'))








