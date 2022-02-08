#Ylessanne nr4
#03.02.2022
#Oliver Kahn


#






















'''
#paaris ja paaritu

for a in range(1,101):
    
    jaak = a%int(2)
        
    if jaak == 0:
        print(a,"paarisarv")
    else:
        print(a,"paaritu arv")
'''



'''
#loto

import random

for e in range(1,6):
    a = int(random.randint(0,9))
    print(a,end="")
'''



'''
#tärnid

for e in range(1,6):
    for a in range(1,6):
        print ("* ",end="")
    print()
print ("-"*10)

for e in range(1,6):
    print(e*"* ")
print ("-"*10)
k = 6
for e in range(1,6):
   print(k*"* ")
   k = k -1
    
'''




'''
#Jalgpalli meeskond

sugu = input ("sisestage oma sugu: ")

if sugu=="mees":
    vanus = int(input("sisestage oma vanus: "))
    if vanus >= 16 and vanus <=18:
        print("sobid meeskonda")
    else:
        print("ei ole sobilik")
        
else:
    ()
    
'''


'''
#Müük
hind = int(input("Sisesta toote hind: "))
if hind<10:
    ale = 0.1
else:
    ale = 0.2
vastus = hind-(hind*ale)
print(vastus)
'''    


'''
#juubel
sunnipaev = input("utle mulle oma sünnikuupäev kujul dd.mm.dddd: ")
dd, mm, dddd = sunnipaev.split(".")
praegu = 2022
vanus = praegu-int(dddd)
jaak = vanus%5
if jaak==0:
    print("juubel")
else:
    print("ei ole juubelit")
'''


'''
#matemaatika
arv1 = int(input("Sisesta üks arv: "))
arv2 = int(input("Sisesta teine arv: "))
tehe = input("vali tehe + - * / ")
if tehe == "+":
    vastus = arv1 + arv2 
if tehe== "-":
    vastus = arv1 - arv2

if tehe== "*":
    vastus = arv1 * arv2

if tehe== "/":
    vastus = arv1 / arv2

print(f"{arv1}{tehe}{arv2}={vastus}")
'''

'''
#ruut
a = int(input("1.kylg: "))
b = int(input("2.kylg: "))

if a==b:
    print("see on ruut")
else:
    print("see on ristkülik")
'''