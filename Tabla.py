from Polje import Polje
from Player import Player
import heapq
from math import hypot
class Tabla:

    def __init__(self,dimX,dimY,lista1,lista2,lista,lista0):
        self.Xpoz=lista1
        self.Opoz=lista2
        self.Xstart=lista
        self.Ostart=lista0
        self.dimX=int(dimX)
        self.dimY=int(dimY)
        self.matrica=[[] * self.dimY] * self.dimX
        for i in range(dimX):
                self.matrica[i] = [Polje(i, j, " ") for j in range(dimY) ]
    def postavi_(self,igrac,lista):
        if igrac=="X":
            self.Xstart=lista
        else:
            self.Ostart=lista
    def proveri_putanje(self):
        return ( self.a_zvezda(self.Xpoz[0],self.Ostart[0]) or self.a_zvezda(self.Xpoz[0],self.Ostart[1])
        or self.a_zvezda(self.Xpoz[1],self.Ostart[0]) or self.a_zvezda(self.Xpoz[1],self.Ostart[1])
        or self.a_zvezda(self.Opoz[0],self.Xstart[0]) or self.a_zvezda(self.Opoz[0],self.Xstart[1])
        or self.a_zvezda(self.Opoz[1],self.Xstart[0]) or self.a_zvezda(self.Opoz[1],self.Xstart[1]))

    #trazenje kako bismo ustanovili da li dodavanjem zida blokiramo put do nekog pocetnog polja
    def a_zvezda(self,start,cilj):
        lista1=[]
        za_obradu={(start[0],start[1]):True}
        red=[(abs(start[1]-cilj[1])+abs(start[0]-cilj[0]))]
        while len(za_obradu)!=0:
            l=heapq.heappop(red)
            if(l[1]==cilj[0] and l[2]==cilj[1]):
                return True
            for el in self.da_li_je_polje_ogradjeno(l[1],l[2]):
                if el not in za_obradu:
                    za_obradu[el]=True
                    heapq.heappush(za_obradu, (abs(el[1]-cilj[1]) + abs(el[0]-cilj[0]),*el))
        return False
    #funkcija koja se poziva uokvviru a_zvezda funkcije
    def da_li_je_polje_ogradjeno(self,i,j):
        lista_mogucih=[]
        if j>0 and not self.matrica[i][j].levizid=="I": #levo
            lista_mogucih.append([i,j-1])
        if j<self.dimY-1 and not self.tabela[i][j].desnizid=="I": #desno
            lista_mogucih.append([i,j+1])
        if i>0:
            if not self.matrica[i][j].gornji=="=":
                lista_mogucih.append([i-1,j])
            if j>0 and self.matrica[i][j].gorelevo():
                lista_mogucih.append([i-1,j-1])
            if j<self.dimY-1 and self.matrica[i][j].goredesno():
                lista_mogucih.append([i-1,j+1])
        if i<self.dimY-1:
            if not self.matrica[i][j].donji=="=":
                lista_mogucih.append([i+1,j])
            if j>0 and self.matrica[i][j].dolelevo():
                lista_mogucih.append([i+1,j-1])
            if j<self.dimY-1 and self.matrica[i][j].doledesno():
                lista_mogucih.append([i+1,j+1])
        return lista_mogucih
    #postavlja se vrednost na odredjeno polje
    def postavi_polje(self,posX,posY,tekst):
        if(self.matrica[posX-1][posY-1].vrednost==" "):
            self.matrica[posX-1][posY-1].vrednost=tekst
            return True
        else: return False
    #provera da li je doslo do kraja igre
    def da_li_je_kraj(self,IgracX,IgracO):
        if(IgracX.s1(self.Opoz[0][0],self.Opoz[0][1]) 
        or IgracX.s2(self.Opoz[1][0],self.Opoz[1][1])
        or IgracX.s1(self.Opoz[1][0],self.Opoz[1][1]) 
        or IgracX.s2(self.Opoz[0][0],self.Opoz[0][1])):
            print("Pobednik je igrac O.")
            return True
        elif(IgracO.s1(self.Xpoz[0][0],self.Xpoz[0][1]) 
        or IgracO.s2(self.Xpoz[1][0],self.Xpoz[1][1]) 
        or IgracO.s1(self.Xpoz[1][0],self.Xpoz[1][1]) 
        or IgracO.s2(self.Xpoz[0][0],self.Xpoz[0][1])):
            print("Pobednik je igrac X. ")
            return True
        else: return False
    #funkcija u kojoj se odigrava potez
    def potez_pesak(self,posX,posY,igrac,broj):
        x=posX-1
        y=posY-1
        if igrac=="X":
            i=self.Xpoz[broj][0]-1
            j=self.Xpoz[broj][1]-1
            self.matrica[i][j].vrednost=" "
            self.Xpoz[broj][0]=posX
            self.Xpoz[broj][1]=posY
            self.postavi_polje(x+1,y+1,"X")
        else:
            i=self.Opoz[broj][0]-1
            j=self.Opoz[broj][1]-1
            self.matrica[i][j].vrednost=" "
            self.Opoz[broj][0]=posX
            self.Opoz[broj][1]=posY
            self.postavi_polje(x+1,y+1,"O")
    def da_li_je_startno(self,posX,posY,igrac):
        if(igrac=="X"):
            if((self.Ostart[0][0]==posX and self.Ostart[0][1]==posY) or (self.Ostart[1][0]==posX and self.Ostart[1][1]==posY) ):
                return True
            else: return False
        else:
            if((self.Xstart[0][0]==posX and self.Xstart[0][1]==posY) or (self.Xstart[1][0]==posX and self.Xstart[1][1]==posY) ):
                return True
            else: return False


    #provera da li pesak moze da predje na trazeno polje
    def validno_polje(self,posX,posY,igrac,broj):
        pesak=self.Xpoz if igrac=="X" else self.Opoz
        i=pesak[broj][0]-1
        j=pesak[broj][1]-1
        x=posX-1
        y=posY-1
        s=True
        if(x<i):
            if(x==i-1 and y==j-1):
               s=self.gore_levo(i,j)
            elif(x==i-1 and y==j+1):
               s=self.gore_desno(i,j)
            elif(x==i-2 and y==j):
                s=self.gore(i,j)
            elif(x==i-1 and y==j):
                s=self.da_li_je_startno(i-1,j,igrac)
            else: return False
        elif(x>i):
            if(x==i+1 and y==j-1):
                s=self.dole_levo(i,j)
            elif(x==i+1 and y==j+1):
                s=self.dole_desno(i,j)
            elif(x==i+2 and y==j):
                s=self.dole(i,j)
            elif(x==i+1 and y==j):
                s=self.da_li_je_startno(i+1,j,igrac)
            else: return False
        else:
            if(x==i and y==j-2):
                s=self.levo(i,j)
            elif(x==i and y==j+2):
                s=self.desno(i,j)
            elif(x==i and y==j-1):
                s=self.da_li_je_startno(i,j-1,igrac)
            elif(x==i and y==j+1):
                s=self.da_li_je_startno(i,j+1,igrac)
            else: return False
        return s
    def desno(self,i,j):
        return not (self.matrica[i][j+1].desnizid=="I" or self.matrica[i][j].desnizid=="I")
    def levo(self,i,j):
        return not (self.matrica[i][j-1].levizid=="I" or self.matrica[i][j].levizid=="I")
    def gore(self,i,j):
        return not (self.matrica[i-1][j].gornjizid=="=" or self.matrica[i][j].gornjizid=="=")
    def dole(self,i,j):
        return not (self.matrica[i+1][j].donjizid=="=" or self.matrica[i][j].donjizid=="=")
    def dole_desno(self,i,j):
        if(self.matrica[i+1][j+1].gornjizid=="=" and self.matrica[i+1][j+1].levizid=="I"):
            return False
        if(self.matrica[i][j].donjizid=="=" and self.matrica[i][j].desnizid=="I"):
            return False
        if(self.matrica[i+1][j+1].gornjizid=="=" and self.matrica[i][j].donjizid=="="):
            return False
        if(self.matrica[i+1][j+1].levizid=="I" and self.matrica[i][j].desnizid=="I"):
            return False
        return True
    def dole_levo(self,i,j):
        if(self.matrica[i+1][j-1].gornjizid=="=" and self.matrica[i+1][j-1].desnizid=="I"):
            return False
        if(self.matrica[i][j].donjizid=="=" and self.matrica[i][j].levizid=="I"):
            return False
        if(self.matrica[i+1][j-1].gornjizid=="=" and self.matrica[i][j].donjizid=="="):
            return False
        if(self.matrica[i+1][j-1].desnizid=="I" and self.matrica[i][j].levizid=="I"):
            return False
        return True
    def gore_levo(self,i,j):
        if(self.matrica[i-1][j-1].donjizid=="=" and self.matrica[i-1][j-1].desnizid=="I"):
            return False
        if(self.matrica[i][j].gornjizid=="=" and self.matrica[i][j].levizid=="I"):
            return False
        if(self.matrica[i-1][j-1].donjizid=="=" and self.matrica[i][j].gornjizid=="="):
            return False
        if(self.matrica[i-1][j-1].desnizid=="I" and self.matrica[i][j].levizid=="I"):
            return False
        return True
    def gore_desno(self,i,j):
        if(self.matrica[i-1][j+1].donjizid=="=" and self.matrica[i-1][j+1].levizid=="I"):
            return False
        if(self.matrica[i][j].gornjizid=="=" and self.matrica[i][j].desnizid=="I"):
            return False
        if(self.matrica[i-1][j+1].donjizid=="=" and self.matrica[i][j].gornjizid=="="):
            return False
        if(self.matrica[i-1][j+1].levizid=="I" and self.matrica[i][j].desnizid=="I"):
            return False
        return True
    #funkcija postavljanja zida
    def potez_zid(self,posX,posY,boja):
        m=int(posX)
        n=int(posY)
        if(boja=="Z"):
            self.matrica[m-1][n-1].desnizid="I"
            self.matrica[m-1][n].levizid="I"
            self.matrica[m][n-1].desnizid="I"
            self.matrica[m][n].levizid="I"
        elif(boja=="P"):
            self.matrica[m-1][n-1].donjizid="=" 
            self.matrica[m][n-1].gornjizid="=" 
            self.matrica[m-1][n].donjizid="="
            self.matrica[m][n].gornjizid="=" 
    #provera mogucnosti postavljanja zida
    def postavi_zid(self,posX,posY,boja):
        m=int(posX)
        n=int(posY)
        if(boja=="Z"):
           return True if(self.matrica[m-1][n-1].desnizid!="I" and self.matrica[m][n-1].desnizid!="I") else False
        elif(boja=="P"):
            if(posY<self.dimY):
                return True if(self.matrica[m-1][n-1].donjizid!="=" and self.matrica[m-1][n].donjizid!="=") else False
            else: return False
        else:
            return False
        
    def vrati_polje(self,posx,posy):
            return self.matrica[posx][posy]
   #inicijalizacija zidova na svakom polju
    def inicijalizacija_zidova(self):
            for i in range(self.dimX):
                for j in range(self.dimY):
                    self.matrica[i][j].levizid=self.matrica[i][j].desnizid="|"
                    self.matrica[i][j].gornjizid=self.matrica[i][j].donjizid="-"
                    self.matrica[i][j].gornjizid="=" if(i==0) else "-"
                    self.matrica[i][j].donjizid="=" if(i==self.dimX-1) else "-"
                    self.matrica[i][j].levizid="I" if(j==0) else "|"
                    self.matrica[i][j].desnizid="I" if(j==self.dimY-1) else "|"
    # stampanje matrice nakon svakog poteza
    def stampanje(self):
                    print(end=" ")
                    for i in range(1,self.dimY+1):
                        print(" ",str(i),end=" ") if i<=9 else print(" ",chr(55+i),end=" ")
                    print(" ")
                    for i in range(1,self.dimY+1):
                        print("  ","=", end='')
                    print()
                    for i in range(0,self.dimX):
                            for t in range(2):
                                for j in range(self.dimY):
                                    
                                        if(t==0):
                                            p=i+1
                                            if(j==0):
                                                print(str(p)+'I',end=" ") if p<=9 else print(chr(55+p)+'I',end=" ")
                                                print(self.matrica[i][j].vrednost,end=" ")
                                                print(self.matrica[i][j].desnizid,end=" ")
                                            elif(j==self.dimY-1):
                                                print(self.matrica[i][j].vrednost,end=" ")
                                                print('I'+str(p),end=" ") if p<=9 else print('I'+chr(55+p),end=" ")
                                            else:
                                                print(self.matrica[i][j].vrednost,end=" ")
                                                print(self.matrica[i][j].desnizid,end=" ")
                                        else:
                                            if(i<self.dimX-1):
                                                print("  ",self.matrica[i][j].donjizid,end="")
                                            if(i==self.dimX-1):
                                                print("  ","=",end="")


                                print()
                    print(end=' ')
                    for i in range(1,self.dimY+1):
                        print(" ",str(i),end=" ") if i<=9 else print(" ",chr(55+i),end=" ")
                    print()
            

