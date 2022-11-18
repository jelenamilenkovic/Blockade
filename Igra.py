import heapq
import sys
from math import inf
from Tabla import Tabla
from Player import Covek, Kompjuter, Player
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
        self.postavi_racunar(p,brojplavih,brojzelenih,self.n,self.m)
        self.tabela.stampanje()
    #provera da li je doslo do kraja igre tj.
    #da li je neki od pesaka dosao na pocetnu poziciju pesaka suprotnog igraca
    def da_li_je_kraj(self):
      return self.tabela.da_li_je_kraj(self.IgracX,self.IgracO)
    #funkcija koja se poziva kada je potrebno odigrati potez
    #pozivaju se i funkcije koje proveravaju da li je moguce odigrati potez
    #definisanim parametrima sa inputa
    def odigraj_potez(self,klasa,igrac):
        if(isinstance(klasa,Covek)):
            potez=' '
            zid_fleg=False
            p_fleg=False
            if self.preostali_zidovi(igrac!=0):
                while(zid_fleg and p_fleg)==False:
                    print("Unesite potez igraca {i} u formatu: [{i} 0/1] [x_pesaka y_pesaka] [Z/P x_zida y_zida]".format(i=igrac))
                    potez=input("Potez:")
                    if not fullmatch("\[[XO] [01]] \[[1-9A-Z] [1-9A-Z]]?( \[[ZP] [1-9A-Z] [1-9A-Z]])", potez):
                        if(potez=="exit"):
                            sys.exit()
                        else:
                            print("Nevalidan format! Format mora biti: [{i} 0/1] [x_pesaka y_pesaka] [Z/P x_zida y_zida]".format(i=igrac))
                    else:
                        zid_fleg=self.proveri_zid(potez[1],potez[13],potez[15],potez[17])
                        p_fleg=self.proveri_pesaka(potez[1],potez[3],potez[7],potez[9])
                self.promena_stanja(potez)
            else:
                while(p_fleg==False):
                    print("Unesite potez igraca {i} u formatu: [{i} 0/1] [x_pesaka y_pesaka]".format(i=igrac))
                    potez=input("Potez:")
                    if not fullmatch("\[[XO] [01]] \[[1-9A-Z] [1-9A-Z]]", potez):
                        if(potez=="exit"):
                            sys.exit()
                        else:
                            print("Nevalidan format! Format mora biti: [{i} 0/1] [x_pesaka y_pesaka] ".format(i=igrac))
                    else:
                        p_fleg=self.proveri_pesaka(potez[1],potez[3],potez[7],potez[9])
                self.tabela.potez_pesak(int(konverzija_zidova(potez[7])),int(konverzija_zidova(potez[9])),potez[1],int(potez[3])) 
                self.tabela.stampanje()
        elif(isinstance(klasa,Kompjuter)):
                maksimalna=-inf
                if(self.preostali_zidovi(igrac)!=0):
                    for el in self.moguce_situacije(igrac):
                        t=self.nova_situacija(el[0][0],el[0][1],el[0][2],igrac,el[1][0],el[1][1],el[1][2])
                        vrednost=self.minimax(t,True,0,-inf,inf)
                        if vrednost>maksimalna:
                            maksimalna=vrednost
                            potez=el
                    self.nova_situacija_kompjuter(potez[0][0],potez[0][1],potez[0][2],igrac,potez[1][0],potez[1][1],potez[1][2])
                else:
                    for el in self.moguce_situacije(igrac):
                        t=self.nova_situacija(el[0],el[1],el[2],igrac," ",0,0)
                        vrednost=self.minimax(t,True,0,-inf,inf)
                        if vrednost>maksimalna:
                            maksimalna=vrednost
                            potez=el
                    self.nova_situacija_kompjuter(potez[0],potez[1],potez[2],igrac," ",0,0)
    #vrsimo proveru mogucih poteza koje bi mogao da odigra racunar
    #biramo najbolji
    def minimax(self, tabla,fleg, dubina, alfa, beta):
        if dubina == 0 :
            return self.IgracX.menhetn_rastojanje("X",tabla) if isinstance(self.IgracX,Kompjuter) else self.IgracO.menhetn_rastojanje("O",tabla)
        f=True
        if fleg == True:
            igrac=self.IgracX if isinstance(self.IgracX,Kompjuter) else self.IgracO
            maksimalna = -inf
            for el in self.moguce_situacije(igrac):
                f=False
                t=self.nova_situacija(el[0][0],el[0][1],el[0][2],igrac,el[1][0],el[1][1],el[1][2])
                suma = self.minimax(t,not fleg, dubina - 1, alfa, beta)
                maksimalna = max(maksimalna, suma)
                alfa = max(alfa, suma)
                if beta <= alfa:
                    break
            return 0 if f else maksimalna
        else:
            minimalna= inf
            igrac=self.IgracX if isinstance(self.IgracX,Covek) else self.IgracO
            for el in self.moguce_situacije(igrac):
                f = False
                t=self.nova_situacija(el[0][0],el[0][1],el[0][2],igrac,el[1][0],el[1][1],el[1][2])
                suma= self.minimax(t,not fleg, dubina - 1, alfa, beta)
                minimalna = min(minimalna, suma)
                beta = min(beta, suma)
                if beta <= alfa:
                    break
            return 0 if f else minimalna     
    #proveravamo da li se specificiran zid moze postaviti za zeljenim koordinatama
    #vracamo True ukoliko je to moguce 
    def proveri_zid(self,igrac,boja,posX,posY):
        if(self.preostali_zidovi(igrac)!=0):
                h1= posX if isinstance(posX,int) else konverzija_zidova(posX)
                h2= posY if isinstance(posY,int) else konverzija_zidova(posY)
                if(str(boja)!='Z' and str(boja)!='P'):
                    print("Format boje nije odgovarajuci, pokusajte ponovo: ")
                    return False
                elif(h1>self.tabela.dimX or h2>self.tabela.dimY or h1<1 or h2<1):
                    print("Koordinate zida su vece od dimenzije table, pokusajte ponovo: ")
                    return False
                elif(self.tabela.postavi_zid(h1,h2,boja)==False):
                   # print("Nemoguce je postaviti zid na poziciji gde se on vec nalazi!")
                    return False
                elif((self.IgracX.proveri_zid(boja) if(igrac=='X') else self.IgracO.proveri_zid(boja))==False):
                   # print("Nemate vise zidova ove boje, pokusajte sa nekom drugom!")
                    return False
                elif((self.da_li_je_startno(h1,h2,boja))):
                    return False
                else:
                    return True
        else:
            print("Nemate vise zidova")
            return False
    #vraca ukupni broj preostalih zidova jednog igraca
    def preostali_zidovi(self,igrac):
     return self.IgracX.brojPlavihZidova + self.IgracX.brojZelenihZidova  if(igrac=='X') else self.IgracO.brojPlavihZidova + self.IgracO.brojZelenihZidova
    def da_li_se_moze_preci(self,posX,posY,igrac):
        if(igrac=="X"):
            if(self.IgracO.s1(posX,posY) or self.IgracO.s2(posX,posY)):
                return True
        else:
            if(self.IgracX.s1(posX,posY) or self.IgracX.s2(posX,posY)):
                return True
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
                        #print("Na izabranom polju se vec nalazi O igrac!")
                        return False
                for l in self.tabela.Xpoz:
                    if(l[0]==i and l[1]==j):
                       # print("Na izabranom polju se vec nalazi X igrac!")
                        return False
                if self.tabela.validno_polje(i,j,t,int(p))==False:
                    #print("Ne moze se preci na to polje!")
                    return False
                else: return True
            except ValueError:
                print("Molimo Vas unesite brojeve")
                return False
            return True
    #ovo je funkcija obicnog igraca(ne kompjutera) koja se poziva nakon sto se proveri i dokaze da je potez apsolutno validan
    #poziva se uokviru funkcije odigraj_potez() i prosledjuje sa taj validan input potez 
    def promena_stanja(self,potez):
        self.tabela.potez_pesak(int(konverzija_zidova(potez[7])),int(konverzija_zidova(potez[9])),potez[1],int(potez[3])) 
        self.IgracX.oduzmi_zid(potez[13]) if(potez[1]=='X') else self.IgracO.oduzmi_zid(potez[13])
        self.tabela.potez_zid(konverzija_zidova(potez[15]),konverzija_zidova(potez[17]),potez[13])
        self.tabela.stampanje()
    #iskopiramo stanje i odigramo potez nad njim
    def nova_situacija(self,i,j,pesak,igrac,boja,x,y):
        nova_tabela=deepcopy(self.tabela)
        nova_tabela.potez_pesak(i,j,igrac,pesak)
        if(self.preostali_zidovi(igrac)!=0):
            nova_tabela.potez_zid(x,y,boja)
        return nova_tabela
    #odigravanje poteza racunara
    def nova_situacija_kompjuter(self,i,j,pesak,igrac,boja,x,y):
        self.tabela.potez_pesak(i,j,igrac,pesak)
        if(self.preostali_zidovi(igrac)!=0):
            self.IgracX.oduzmi_zid(boja) if(igrac=='X') else self.IgracO.oduzmi_zid(boja)
            self.tabela.potez_zid(x,y,boja)
        self.tabela.stampanje()
    #generisanje svih mogucih poteza
    def moguce_situacije(self,igrac):
        combined=[]
        lista_pesak=self.lista_mogucih_pomeraja(igrac)
        if(self.preostali_zidovi(igrac)!=0):
            lista_zid=self.lista_mogucih_zidova(igrac)
            combined=list(itertools.product(lista_pesak,lista_zid))
            return combined
        else:
            return lista_pesak
    #lista svih mogucih pomeraja pesaka
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
    #lista svih mogucih postavka zidova
    def lista_mogucih_zidova(self,igrac):
        lista_zidova=[]
        lista_boja=["Z","P"]
        for boja in lista_boja:
            for i in range(1,self.tabela.dimX):
                for j in range(1,self.tabela.dimY):
                    if self.proveri_zid(igrac,boja,i,j):
                        lista_zidova.append([boja,i,j])
        return lista_zidova
    #provera granica table
    def granice_dimenzija(self,i,j):
        return False if i<0 or i>self.tabela.dimX or j<0 or j>self.tabela.dimY else True
    #postavka igraca i tabele
    def postavi_racunar(self,p,brplavih,brzelenih,n,m):
       if(p=="DA" or p=="da"):
            if(m>9 and n>9):
                lista1=[4,8],[8,8]
            else:
                lista1=[1,2],[1,4]
            self.IgracX=Kompjuter(True,lista1[0],lista1[1],brplavih,brzelenih)
            list2=[]
            A=False
            while(A==False):
                print("Unesite startne koordinate vaseg igraca")
                for i in range(0, 2):
                            ele = [konverzija_zidova(input()), konverzija_zidova(input())]
                            list2.append(ele)
                if(list2==lista1): A=False
                else: A=True
            self.tabela=Tabla(n,m,deepcopy(lista1),deepcopy(list2),deepcopy(lista1),deepcopy(list2) )
            self.tabela.postavi_polje(lista1[0][0],lista1[0][1],"X")
            self.tabela.postavi_polje(lista1[1][0],lista1[1][1],"X")
            self.tabela.postavi_polje((list2[0])[0],(list2[0])[1],"O")
            self.tabela.postavi_polje((list2[1])[0],(list2[1])[1],"O")
            self.IgracO=Covek(False,list2[0],list2[1],brplavih,brzelenih)
            
       else:  
            list2=[]
            A=False
            while(A==False):
                print("Unesite startne koordinate vaseg igraca")
                for i in range(0, 2):
                            ele = [konverzija_zidova(input()), konverzija_zidova(input())]
                            list2.append(ele)
                if(n>9 and m>9):
                    lista1=[4,8],[8,8]
                else:
                    lista1=[1,2],[1,4]
                if(list2==lista1): 
                    A=True
                    if(n>10 and m>10):
                        lista1=[4,4],[8,4]
                    else:
                        lista1=[1,1],[2,2]
                else: A=True
            self.tabela=Tabla(n,m,deepcopy(list2),deepcopy(lista1),deepcopy(list2),deepcopy(lista1) )
            self.tabela.postavi_polje((list2[0])[0],(list2[0])[1],"X")
            self.tabela.postavi_polje((list2[1])[0],(list2[1])[1],"X")
            self.tabela.postavi_polje(lista1[0][0],lista1[0][1],"O")
            self.tabela.postavi_polje(lista1[1][0],lista1[1][1],"O")
            self.IgracX=Covek(False,list2[0],list2[1],brplavih,brzelenih)
            self.IgracO=Kompjuter(True,lista1[0],lista1[1],brplavih,brzelenih)
    
        
            

            
if __name__ == '__main__':
    i=Igra()
    Igra.zapocni_igru(i)
    
    while(i.da_li_je_kraj()==False):
        
        i.odigraj_potez(i.IgracX,"X")
        i.odigraj_potez(i.IgracO,"O")
        
    print("Igra je zavrsena!")

