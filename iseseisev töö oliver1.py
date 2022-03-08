#python ylessanne nr 3.4
#Oliver Kahn
#08.03.2022

gmail = input("Sisesta oma gmail: ")
if "@" in gmail:
    nimi = gmail.split("@", 1)[0]
    enimi = nimi.split(".", 1)[0]
    lopp = gmail.split("@", 1)[1]
    server = lopp.split(".", 1)[0]
    domeen = lopp.split(".", 1)[1]

    print("Tere " + enimi + ", sinu email on serveris " + server + " ja domeeniks on sul " + domeen)
else:
    print("Sisesta gmail uuesti")

