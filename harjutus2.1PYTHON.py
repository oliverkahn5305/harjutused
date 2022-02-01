import math
# harjutus 2
# Oliver Kahn
# 31.01.2022

#rulluisutajad
kiirus = 29.9
aeg = 0.4
summa = (kiirus/aeg)
print(summa)




#Pitsa
koguhind = 12.90
jootraha = 0.1
sopru = 3
summa=(koguhind+koguhind*jootraha)/sopru
print("igaüks peab maksma",summa,"eurot")




'''
#Kütusekulu arvutamine
liitrid = int(input("Sisestage tangitud kütuse kogus: "))
km = int(input("Sisestage läbitud kilomeetrid: "))
distants = 100
kulu = liitrid/(km/100)
print("kütusekulu 100km kohta keskmiselt on",kulu,"l")
'''




#Arvusüsteemid
arv = int(input("Sisesta arv: "))
print(bin(arv))
print(hex(arv))




'''
#kolmnurga ümbermöödu arvutamine
a = int(input("Sisestage külje pikkus "))
b = int(input("Sisestage külje pikkus "))
c = int(input("Sisestage külje pikkus "))
P = a + b + c
print("Vastus: kolmnurga ümbermõõt on ", str(P)+"cm^2")
'''



#Hüpotenuus
a,b = 16,9
c = math.sqrt(a**2+b**2)
print("hüpotenuus on",c)






#toodete summa arvutamine
hind = 36.75
Soodukas = 0.4
kogus= 3
summa=(hind-(hind*Soodukas))*kogus
print(kogus,"toote hind on",summa)


#Ajateisendus
aeg = int(input("Sisesta aeg minutites"))
h = aeg//60
m = aeg % 60
print(h,":",m)
