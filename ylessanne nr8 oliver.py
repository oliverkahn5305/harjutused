#ylessanne nr8
#Oliver Kahn
#16.02.2022

#Sinu esimene klass ja objekt

class Auto:
    #atribuudid
    mark = 'teadmata'
    aasta = 'teadmata'
    hind = 0
    kiirus = 'teadmata'
    varv = 'teadmata'
    
    #meetodid
   
    def __init__(self,x,y,z,g,h):
        self.mark = x
        self.hind = y
        self.aasta = z
        self.kiirus = g
        self.varv = h
   
    def kuva(self):        
        print(f'Mark: {self.mark} \nHind: {self.hind} \nAasta: {self.aasta} \nKiirus: {self.kiirus} \nVarv: {self.varv}')

   
  
    

uusobjekt = Auto("bemm", 18000, 1998, "213km/h", "must")
uusobjekt.kuva()
print("--------------------")
oliveriauto = Auto("lada", 500, 1987, "140km/h", "beez")
oliveriauto.kuva()

