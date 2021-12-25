from Tabla import Tabla
from Player import Player
from Polje import Polje
import itertools
from re import fullmatch
from copy import deepcopy

def validacija_dimenzija(vrsta,limit):
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
def konverzija_zidova( karakter):
        lista_brojeva=['0','1','2','3','4','5','6','7','8','9']
        return int(karakter)  if karakter in lista_brojeva else ord(karakter)-ord('A')+10
class Igra:
    def __init__(self):
            
            self.tabela=None
            self.n=None
            self.m=None
            self.IgracX=None
            self.IgracO=None
    #startna funkcija koja se poziva pri pokretanju programa
    #kako bi se objekti inicijalizovali
    def zapocni_igru(self):
        self.n=validacija_dimenzija("paran",22)
        self.m=validacija_dimenzija("neparan",28)
        brojzelenih=int(input("Unesite broj zelenih zidova po igracu: "))
        brojplavih=int(input("Unesite broj plavih zidova po igracu: "))
        p=input("Da li zelite da prvo igra racunar?[DA/NE] ")
        #self.postavi_racunar(p)
        print("Unesite startne pozicije X igraca: ")
        list1=[]
        for i in range(0, 2):
                    ele = [int(input(),16), int(input(),16)]
                    list1.append(ele)
        self.IgracX=Player("X",list1[0],list1[1],brojplavih,brojzelenih)
        print("Unesite startne pozicije Y igraca: ")
        list2=[]
        for i in range(0, 2):
                    ele = [int(input(),16), int(input(),16)]
                    list2.append(ele)
        self.IgracO=Player("O",list2[0],list2[1],brojplavih,brojzelenih)
        self.tabela=Tabla(self.n,self.m,list1,list2)
        self.tabela.postavi_polje((list1[0])[0],(list1[0])[1],"X")
        self.tabela.postavi_polje((list1[1])[0],(list1[1])[1],"X")
        self.tabela.postavi_polje((list2[0])[0],(list2[0])[1],"O")
        self.tabela.postavi_polje((list2[1])[0],(list2[1])[1],"O")
        self.tabela.stampanje()
    #provera da li je doslo do kraja igre tj.
    #da li je neki od pesaka dosao na pocetnu poziciju pesaka suprotnog igraca
    def da_li_je_kraj(self):
      return self.tabela.da_li_je_kraj(self.IgracX,self.IgracO)
    #funkcija koja se poziva kada je potrebno odigrati potez
    #pozivaju se i funkcije koje proveravaju da li je moguce odigrati potez
    #definisanim parametrima sa inputa
    def odigraj_potez(self,igrac):
        potez=' '
        zid_fleg=False
        p_fleg=False
        while(zid_fleg and p_fleg)==False:
            print("Unesite potez u formatu: [X/O 0/1] [x_pesaka y_pesaka] [Z/P x_zida y_zida]")
            potez=input("Potez:")
            if not fullmatch("\[[XO] [01]] \[[1-9A-Z] [1-9A-Z]]?( \[[ZP] [1-9A-Z] [1-9A-Z]])", potez):
               print("Nevalidan format! Format mora biti: [X/O 0/1] [x_pesaka y_pesaka] [Z/P x_zida y_zida]")
            else:
                zid_fleg=self.proveri_zid(potez[1],potez[13],potez[15],potez[17])
                p_fleg=self.proveri_pesaka(potez[1],potez[3],potez[7],potez[9])
        self.moguce_situacije(igrac)
        #self.promena_stanja(potez)
        #self.tabela.stampanje()
        #self.promena_stanja(potez)
    #proveravamo da li se specificiran zid moze postaviti za zeljenim koordinatama
    #vracamo True ukoliko je to moguce
    def proveri_zid(self,igrac,boja,posX,posY):
        if(self.preostali_zidovi(igrac)!=0):
                h1= posX if isinstance(posX,int) else konverzija_zidova(posX)
                h2= posY if isinstance(posY,int) else konverzija_zidova(posY)
                if(str(boja)!='Z' and str(boja)!='P'):
                    print("Format boje nije odgovarajuci, pokusajte ponovo: ")
                    return False
                elif(h1>self.tabela.dimX or h2>self.tabela.dimY):
                    print("Koordinate zida su vece od dimenzije table, pokusajte ponovo: ")
                    return False
                elif(self.tabela.postavi_zid(h1,h2,boja)==False):
                    print("Nemoguce je postaviti zid na poziciji gde se on vec nalazi!")
                    return False
                elif((self.IgracX.proveri_zid(boja) if(igrac=='X') else self.IgracO.proveri_zid(boja))==False):
                    print("Nemate vise zidova ove boje, pokusajte sa nekom drugom!")
                    return False
                else:
                    return True
        else:
            print("Nemate vise zidova")
            return False
    #vraca ukupni broj preostalih zidova jednog igraca
    def preostali_zidovi(self,igrac):
     return self.IgracX.brojPlavihZidova + self.IgracX.brojZelenihZidova  if(igrac=='X') else self.IgracO.brojPlavihZidova + self.IgracO.brojZelenihZidova
    #proveravamo da li ne ogradjujemo startno polje posto pravila igre to ne dozvoljavaju
    def da_li_je_startno(self,posX,posY,boja):
        if(boja=="P"):
            if(self.IgracO.s1(posX,posY) or self.IgracO.s2(posX,posY) or self.IgracO.s1(posX+1,posY+1) or 
            self.IgracO.s2(posX+1,posY+1) or self.IgracO.s1(posX+1,posY) or self.IgracO.s2(posX+1,posY) or 
            self.IgracO.s1(posX,posY+1) or self.IgracO.s2(posX,posY+1) or self.IgracX.s1(posX,posY) or 
            self.IgracX.s2(posX,posY) or self.IgracX.s1(posX+1,posY+1) or self.IgracX.s2(posX+1,posY) or 
            self.IgracX.s2(posX+1,posY+1) or self.IgracX.s1(posX+1,posY) or 
            self.IgracX.s1(posX,posY+1) or self.IgracX.s2(posX,posY+1)):
                return True
            else:
                return False
        elif(boja=="Z"):
            if(self.IgracO.s1(posX,posY) or self.IgracO.s2(posX,posY) or self.IgracO.s1(posX+1,posY) or self.IgracO.s2(posX+1,posY) 
            or self.IgracO.s1(posX+1,posY+1) or self.IgracO.s2(posX+1,posY+1) or self.IgracO.s1(posX,posY+1) or self.IgracO.s2(posX,posY+1)
            or self.IgracX.s1(posX,posY) or self.IgracX.s2(posX,posY) or self.IgracX.s1(posX+1,posY) or self.IgracX.s2(posX+1,posY) 
            or self.IgracX.s1(posX+1,posY+1) or self.IgracX.s2(posX+1,posY+1) or self.IgracX.s1(posX,posY+1) or self.IgracX.s2(posX,posY+1)
            ):
                return True
            else:
                return False
        else:
            return False
    #proveravamo da li je moguce pomeriti odredjenog pesaka na zeljeno polje
    def proveri_pesaka(self,t,p,i,j):
            i= i if isinstance(i,int) else konverzija_zidova(i)
            j= j if isinstance(j,int) else konverzija_zidova(j)
            try:
                for l in self.tabela.Opoz:
                    if(l[0]==i and l[1]==j):
                        print("Na izabranom polju se vec nalazi O igrac!")
                        return False
                for l in self.tabela.Xpoz:
                    if(l[0]==i and l[1]==j):
                        print("Na izabranom polju se vec nalazi X igrac!")
                        return False
                if self.tabela.validno_polje(i,j,t,int(p))==False:
                    print("Ne moze se preci na to polje!")
                    return False
                else: return True
            except ValueError:
                print("Molimo Vas unesite brojeve")
                return False
            return True
    #ovo je funkcija obicnog igraca(ne kompjutera) koja se poziva nakon sto se proveri i dokaze da je potez apsolutno validan
    #poziva se uokviru funkcije odigraj_potez() i prosledjuje sa taj validan input potez 
    def promena_stanja(self,potez):
        self.tabela.potez_pesak(int(potez[7]),int(potez[9]),potez[1],int(potez[3])) 
        self.IgracX.oduzmi_zid(potez[13]) if(potez[1]=='X') else self.IgracO.oduzmi_zid(potez[13])
        self.tabela.potez_zid(potez[15],potez[17],potez[13])
        self.tabela.stampanje()
    #ovo je funkcija slicna prethodnoj, menja trenutno stanje, ali je poziva kompjuter
    #samim tim se uokviru nje ne poziva promena broja zidova, zato sto ova funkcija 
    def nova_situacija(self,i,j,pesak,igrac,boja,x,y):
        nova_tabela=deepcopy(self.tabela)
        nova_tabela.potez_pesak(i,j,igrac,pesak)
        nova_tabela.potez_zid(x,y,boja)
      #  nova_tabela.stampanje()
        return nova_tabela
    def moguce_situacije(self,igrac):
        combined=[]
        lista_pesak=self.lista_mogucih_pomeraja(igrac)
        lista_zid=self.lista_mogucih_zidova(igrac)
        combined=list(itertools.product(lista_pesak,lista_zid))
        for el in combined:
           
            self.nova_situacija(el[0][0],el[0][1],el[0][2],igrac,el[1][0],el[1][1],el[1][2])
        f=len(combined)
        print(f)
    def lista_mogucih_pomeraja(self,igrac):
        lista_pomeraja=[]
        if(igrac=="X"):
            for el in range(2):
                trX=self.tabela.Xpoz[el][0]
                trY=self.tabela.Xpoz[el][1]
                for i in range(trX-2,trX+3):
                    for j in range(trY-2,trY+3):
                        if self.granice_dimenzija(i-1,j-1):
                            if self.proveri_pesaka(igrac,el,i,j):
                                lista_pomeraja.append([i,j,el])
        else:
            for el in range(2):
                trX=self.tabela.Opoz[el][0]
                trY=self.tabela.Opoz[el][1]
                for i in range(trX-2,trX+3):
                    for j in range(trY-2,trY+3):
                        if self.granice_dimenzija(i-1,j-1):
                            if self.proveri_pesaka(igrac,el,i,j):
                                lista_pomeraja.append([i,j,el])
        return lista_pomeraja

      
    def lista_mogucih_zidova(self,igrac):
        lista_zidova=[]
        lista_boja=["Z","P"]
        for boja in lista_boja:
            for i in range(1,self.tabela.dimX):
                for j in range(1,self.tabela.dimY):
                    if self.proveri_zid(igrac,boja,i,j):
                       # i=konverzija_zidova(str(i)) if(i<=9) else ord(i)-ord('A')+10
                       # j=konverzija_zidova(str(j))
                        lista_zidova.append([boja,i,j])
        return lista_zidova




    def granice_dimenzija(self,i,j):
        return False if i<0 or i>self.tabela.dimX or j<0 or j>self.tabela.dimY else True
    def postavi_racunar(self,p):
       if(p=="DA" or "da"):
            self.IgracX.racunar=True 
       else:  
           self.IgracO.racunar=True
    
    
            
if __name__ == '__main__':
   # n=validacija_dimenzija("paran",22)
   # m=validacija_dimenzija("neparan",28)
   # i=Igra(n,m)
    i=Igra()
    Igra.zapocni_igru(i)
    
    while(i.da_li_je_kraj()==False):
        
        i.odigraj_potez('X')

        i.odigraj_potez('O')
        
    print("Igra je zavrsena!")

