#Oliver Kahn
#Graafiline yl2-...
#22.03.2022











'''
from tkinter import *
aken = Tk()
aken.title('Tkinter "Kalkulaator"')
aken.geometry("200x200+100+100")
aken.resizable(0, 0)


neli = Button(aken, width=4, text="4", font="Tahoma 12")
neli.grid(row=3, column=0, padx=2, pady=2)
viis = Button(aken, width=4, text="5", font="Tahoma 12")
viis.grid(row=3, column=1, padx=2, pady=2)

kuus = Button(aken, width=4, text="6", font="Tahoma 12")
kuus.grid(row=3, column=2, padx=2, pady=2)
tärn = Button(aken, width=4, text="*", font="Tahoma 12")
tärn.grid(row=3, column=3, padx=2, pady=2)
tekst = Label(aken, text="Siia kunagi tekst!", font="Tahoma 12")
tekst.grid(row=1, columnspan=4, padx=2, pady=2)

seitse = Button(aken, width=4, text="7", font="Tahoma 12")
seitse.grid(row=2, column=0, padx=2, pady=2)
kaheksa = Button(aken, width=4, text="8", font="Tahoma 12")
kaheksa.grid(row=2, column=1, padx=2, pady=2)
üheksa = Button(aken, width=4, text="9", font="Tahoma 12")
üheksa.grid(row=2, column=2, padx=2, pady=2)
kriips = Button(aken, width=4, text="/", font="Tahoma 12")
kriips.grid(row=2, column=3, padx=2, pady=2)


null = Button(aken, width=4, text="0", font="Tahoma 12")
null.grid(row=5, column=0, padx=2, pady=2)
koma = Button(aken, width=4, text=",", font="Tahoma 12")
koma.grid(row=5, column=1, padx=2, pady=2)
vordusmark = Button(aken, width=4, text="=", font="Tahoma 12")
vordusmark.grid(row=5, column=2, padx=2, pady=2)
plus = Button(aken, width=4, text="+", font="Tahoma 12")
plus.grid(row=5, column=3, padx=2, pady=2)


yks = Button(aken, width=4, text="1", font="Tahoma 12")
yks.grid(row=4, column=0, padx=2, pady=2)
kaks = Button(aken, width=4, text="2", font="Tahoma 12")
kaks.grid(row=4, column=1, padx=2, pady=2)
kolm = Button(aken, width=4, text="3", font="Tahoma 12")
kolm.grid(row=4, column=2, padx=2, pady=2)
kriips = Button(aken, width=4, text="-", font="Tahoma 12")
kriips.grid(row=4, column=3, padx=2, pady=2)

'''



'''
from tkinter import *
aken = Tk()
aken.title('Tkinter "Jou mees"')
aken.geometry("140x100+100+100")
aken.resizable(0, 0)
Oliver = "Oliver Kahn \nRühm: IT-21\n2022"
tekst = Label(aken, text=Oliver, font="Tahoma 16 bold italic", foreground="red", background="black", pady=10, padx=0)
tekst.pack(side="left")
aken.mainloop()
'''

'''
pikkus = int(input("Sisesta külje pikkus: "))
import turtle
for i in range(3):
    turtle.forward(pikkus)
    turtle.right(120)
'''    


'''
import turtle

for i in range(5):
    turtle.forward(200)
    turtle.right(145)
    turtle.forward(200)
'''    