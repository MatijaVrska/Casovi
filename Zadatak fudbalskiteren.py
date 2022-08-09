# Fudbalski teren dimenzija d*s treba ograditi pravodugaonom
# ogradom tako da je rastojanje stranica ograde od linije
# terena r.
# Napisi program koji odredjuje duzinu ograde.

# Ulaz: U tri reda standardnog ulaza nalaze se tri cela broja:
#       d-duzina terena u metrima(90<=d=<120)
#       s-sirina terena u metrima(45<=s<90)
#       r-rastojanje ograde od terena u metrima(2<=r<=10)

# Izlaz: Duzina ograde u metrima.

d= int(input("duzina ivice pravougaonog terena d je:"))
s= int(input("sirina ivice pravougaonog terena s je:"))
r= int(input("rastojanje ograde od terena u metrima r je:"))
O= (2*d+2*r)+(2*s+2*r)
print(O)


