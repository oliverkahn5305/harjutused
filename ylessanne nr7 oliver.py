#ylessanne nr7
#oliver kahn
#15.02.2022

#ruumala leidmise programm

import math

def kuup(a):
    v = a ** 3
    return v

def kera(r):
    v = round(4/3*math.pi*r**3,2)
    return v

def koonus(r, h):
    v = round(1/3*math.pi*r**2*h,2)
    return v

def silinder(r, h):
    v = round(math.pi*r**2*h,2)
    return v

loop = 1

print("******************* LEIAME RUUMALA *********************")
print("vali kujund:\n1 kuup\n2 kera\n3 koonus\n4 silinder\n5 EXIT")
valik = int(input("vali soovitud kujundi number : "))
if valik== 1:
    print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-\valisid kuubi ruumala arvutamise")
    a = int(input("sisesta kuubi külje pikkus a="))
    print(kuup(a ))

if valik== 2:
    print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-\valisid kera ruumala arvutamise")
    a = int(input("sisesta kera raadius r="))
    print(kera(r ))    

if valik== 3:
    print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-\valisid koonuse ruumala arvutamise")
    a = int(input("sisesta koonuse raadius r="))
    
    print(koonus(r, h ))








'''
#loob funktsiooni atribuutidega
def tervita(nimi, keel="de"):
    if keel=="et":
       print(f"Tere {nimi}!")
    elif keel=="en":
        print(f"Hi {nimi}!")
    else:
        print(f"Hallo {nimi}!")



keel = input("Vali keel et/en/de: ")
nimi = input("Sisesta oma nimi: ")
#funktsiooni väljakutsumine
tervita(nimi)
'''
