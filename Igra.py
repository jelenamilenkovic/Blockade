from Tabla import Tabla
from Player import Player
from Polje import Polje

def validacijadimenzija(vrsta,limit):
        age=None
        while age is None:
            input_value = input("Unesite {v} broj manji od {l} za dimenziju table: ".format(v=vrsta,l=limit))
            try:
                age = int(input_value)
                if age%2==0 and vrsta=="paran" and age<int(limit):
                    return age
                elif age%2==1 and vrsta=="neparan" and age<int(limit) :
                    return age
                elif age>int(limit):
                    age=None
                    print("Dimenzija je veca od ocekivane")
                else: 
                    age=None
                    print("Parnost dimenzije nije odgovarajuca, pokusajte ponovo")
            except ValueError:
                print("{input} nije broj, molimo Vas unesite broj".format(input=input_value))
class Igra:
    def __init__(self,dimX,dimY):
            
            self.Tabela=Tabla(dimX,dimY)
            #self.startY=[]
            #self.Tabela=Tabla
            self.racunar=False
            self.IgracX=None
            self.IgracO=None

    def dalijestartnopolje(self,a,b):
        True if(self.Tabela.matrica[a][b].startnopolje==True) else False

    def zapocniigru(self):
        self.Tabela.InicijalizacijaZidova()
        self.Tabela.Stampanje()
        brojzelenih=int(input("Unesite broj zelenih zidova po igracu: "))
        brojplavih=int(input("Unesite broj plavih zidova po igracu: "))
        print("Unesite startne pozicije X igraca: ")
        list1=[]
        for i in range(0, 2):
                    ele = [int(input()), int(input())]
                    list1.append(ele)
        self.IgracX=Player("X",list1[0],list1[1],brojplavih,brojzelenih)
       
        print(self.IgracX)
        print("Unesite startne pozicije Y igraca: ")
        list2=[]
        for i in range(0, 2):
                    ele = [int(input()), int(input())]
                    list2.append(ele)
       
        self.IgracO=Player("O",list2[0],list2[1],brojplavih,brojzelenih)
        self.Tabela.postaviPolje((list1[0])[0],(list1[0])[1],self.IgracX.lista[0])
        self.Tabela.postaviPolje((list1[1])[0],(list1[1])[1],self.IgracX.lista[1])
        self.Tabela.postaviPolje((list2[0])[0],(list2[0])[1],self.IgracO.lista[0])
        self.Tabela.postaviPolje((list2[1])[0],(list2[1])[1],self.IgracO.lista[1])
        self.racunar=True
        self.Tabela.Stampanje()
    def proverizidove(self,posX,posY,boja):
        if(boja=="Z"):
            if(self.IgracO.s1(posX,posY) or self.IgracO.s2(posX,posY) or self.IgracO.s1(posX-1,posY) or self.IgracO.s2(posX-1,posY)
           or self.IgracX.s1(posX,posY) or self.IgracX.s2(posX,posY) or self.IgracX.s1(posX-1,posY) or self.IgracX.s2(posX-1,posY)):
                return True
            else:
                return False
        elif(boja=="P"):
            if(self.IgracO.s1(posX,posY) or self.IgracO.s2(posX,posY) or self.IgracO.s1(posX,posY-1) or self.IgracO.s2(posX,posY-1)
           or self.IgracX.s1(posX,posY) or self.IgracX.s2(posX,posY) or self.IgracX.s1(posX,posY-1) or self.IgracX.s2(posX,posY-1)):
                return True
            else:
                return False
        else:
            return False
            
    def stampajstartnepozicije(self):
            print("Startne pozicije prvog igraca",self.startX)
    def pomeripiona(self,t):
        print(t,":")
        p = [x for x in input("Izaberite igraca(0||1): ").split()]
        i=None
        j=None
        while(i==None and j==None):
            i,j=[int(x) for x in input("Izaberite koordinate novog polja: ").split()]
            try:
                for l in self.IgracO.lista:
                    if(l.trY==j and l.trX==i):
                        i=None 
                        j=None
                        print("Na izabranom polju se vec nalazi O igrac")
                for l in self.IgracX.lista:
                    if(l.trY==j and l.trX==i):
                        i=None
                        j=None
                        print("Na izabranom polju se vec nalazi X igrac")
            except ValueError:
                print("Molimo Vas unesite brojeve")
        if(t=="X"):
            if(p=='0'):
                self.Tabela.pomeriPiona(i,j,self.IgracX.lista[0]) 
            else:
                self.Tabela.pomeriPiona(i,j,self.IgracX.lista[1])
        else:
            if(p=='0'): 
                 self.Tabela.pomeriPiona(i,j,self.IgracO.lista[0])
            else:
                self.Tabela.pomeriPiona(i,j,self.IgracO.lista[1])
        
    def postavizid(self,igrac):
        boja='A'
        posX=None
        posY=None
        while(posX==None or posY==None or (boja!='Z' or boja!='P')):
            boja,posX,posY=[x for x in input("Izaberite boju i pocetno polje zida: ").split()]
            if(str(boja)!='Z' and str(boja)!='P'):
                print("Format boje nije odgovarajuci, pokusajte ponovo: ")
                posX=None
            elif(int(posX)>=self.Tabela.dimX or int(posY)>=self.Tabela.dimY):
                print("Koordinate zida su vece od dimenzije table, pokusajte ponovo: ")
                posX=None
            elif(self.proverizidove(int(posX),int(posY),boja)==True):
                print("Startno polje se ne moze ograditi")
                posX=None
            elif(self.Tabela.postavizid(int(posX),int(posY),boja)==False):
                print("Nemoguce je postaviti zid na poziciji gde se on vec nalazi")
                posX=None
            else:
                break
            
        self.IgracX.oduzmizid(boja) if(igrac=='X') else self.IgracO.oduzmizid(boja)
        self.IgracX.stampanje() if(igrac=='X') else self.IgracO.stampanje()
                
    def dalijekraj(self):
        if((self.IgracX.s1(self.IgracO.lista[0].trX,self.IgracO.lista[0].trY) 
        and self.IgracX.s2(self.IgracO.lista[1].trX,self.IgracO.lista[1].trY)) or 
        (self.IgracX.s1(self.IgracO.lista[1].trX,self.IgracO.lista[1].trY) 
        and self.IgracX.s2(self.IgracO.lista[0].trX,self.IgracO.lista[0].trY))):
            print("Pobednik je igrac O. Igra je zavrsena!")
            return True
        elif((self.IgracO.s1(self.IgracX.lista[0].trX,self.IgracX.lista[0].trY) 
        and self.IgracO.s2(self.IgracX.lista[1].trX,self.IgracX.lista[1].trY)) or 
        (self.IgracO.s1(self.IgracX.lista[1].trX,self.IgracX.lista[1].trY) 
        and self.IgracO.s2(self.IgracX.lista[0].trX,self.IgracX.lista[0].trY))):
            print("Pobednik je igrac X. Igra je zavrsena!")
            return True
        else: return False

        
        
            
if __name__ == '__main__':
    n=validacijadimenzija("paran",22)
    m=validacijadimenzija("neparan",28)
    i=Igra(n,m)
    Igra.zapocniigru(i)
    while(i.dalijekraj==False):
        
            
            i.pomeripiona("X")
            i.postavizid("X")
            i.Tabela.Stampanje() 

            i.pomeripiona("O")
            i.postavizid("O")
            i.Tabela.Stampanje() 
        
    print("Igra je zavrsena!")

