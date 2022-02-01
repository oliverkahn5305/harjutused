#harjutus 3
#oliver kahn
#01.02.2022











#palindroom
sisestus = input("sisesta palindroom: ")
print(sisestus == sisestus[::-1])





#tundide ajad

aeg1 = input("Algusaeg: ")
aeg2 = input("Lopuaeg: ")
hh1, mm1 = aeg1.split(":")
hh2, mm2 = aeg2.split(":")
vastus = (int(hh2)*60+int(mm2)) - (int(hh1)*60+int(mm1))
h = vastus//60
m = vastus%60          
print("Õpilase päeva pikkus on {}:{} h ööpäevas".format(h,m))




'''
#korralik nimi
int(input"Mis su nimi on?")
'''