# Napisati program koji na osnovu zadate sirine i visine lista
# papira (pravougaonog oblika) u milimetrima odredjuje njegovu
# povrsinu u kvadratnim milimetrima.

# Ulaz: U jednoj liniji standardnog ulaza nalaze se dve
# celobrojne vrednosti V i S (0<V<=300,0<S<=300) koje
# predstavljaju sirinu i visinu lista papira izrazenu u
# milimetrima.

# Izlaz: Jedan ceo broj koji predstavlja povrsinu lista u
# kvadratnim milimetrima.

s= int(input("sirina lista papira izrazena u milimetrima je:"))
d= int(input("visina lista papira izrazena u milimetrima je:"))

P= s*d
print("Povrsina lista papira u kvadratnim milimetrima",P)