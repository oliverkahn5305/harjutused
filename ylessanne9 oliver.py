#Oliver Kahn
#28.02.2022
#Harjutus nr9

#tänane kuupäev
import datetime
from datetime import date
kuup = date.today()
today = kuup.strftime("%d %B %Y")
print(today)

#isikukood
ik = "50509260293"
aasta= int("20" + ik[1] + ik[2])
kuu = int(ik[3] + ik[4])
paev = int(ik[5] + ik[6])
vanus = date.today() - datetime.date(aasta, kuu, paev)
avanus = str(vanus).split(" ")
print(int(int(avanus[0])/(365)))  