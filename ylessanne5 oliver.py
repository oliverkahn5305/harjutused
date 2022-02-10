#ylessanne 5
#oliver kahn
#10.02.2022

#tärnid

import random

arvud = []
for a in range(5):
    arvud.append(random.randint(1,99))
print(arvud)
for a in range(len(arvud)):
    print("*"*arvud[a])







'''
#vanused

import random 
vanused = []
for i in range (5):
    vanused.append(random.randint(1,99))

print(vanused)
'''

'''
#duplikaadid

opilased = ['juhan','kalle','kati','mario','mati']
puhtad_opilased = []

for i in range(len(opilased)):
    if opilased[i] not in puhtad_opilased:
        puhtad_opilased.append(opilased[i])
    
for i in range(len(puhtad_opilased)):
    print(puhtad_opilased[i],end=", ")
'''

'''
#nimede lisamine loendisse

nimed = []
for a in range(5):
    nimi = input("lisa nimi: ")
    nimed.append(nimi)
nimed.sort()
print(nimed)
'''

'''
#opilased

opilased = ['kalle','malle','anne','tõnis','juhan']

print("vali number, mis soovid muuta: ")
for a in range (len(opilased)):
    print(f"{a+1}. {opilased[a]}")
valik = int(input("sisestage number: "))
del opilased[valik-1]
u_nimi = input("sisestage uus nimi: ")
opilased.insert(valik-1,u_nimi)
print("nimi uuendatud")
print(opilased)
'''