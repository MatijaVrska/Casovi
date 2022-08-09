# Sportista se na pocetku treninga zagreva tako sto trci po
# ivicama pravougaonog terena duzine d i sirine s.
# Napisati program kojim se odredjuje koliko metara pretrci
# sportista dok jednom obidje teren.

# Ulaz: U prvoj liniji standardnog ulaza se nalazi celobrojna
# vrednost s(0<s<=100) koje redom predstavljaju duzinu i sirinu
# terena izrazenu u metrima

# Izlaz: Ceo Broj metara koje pretrci sportista dok jednom
# obidje teren.



d =int(input("duzina ivice pravougaonog terena je:"))
s =int(input("sirina ivice pravougaonog terena je:" ))
 
O= 2*d+2*s
print("Sportista pretrci",O)
