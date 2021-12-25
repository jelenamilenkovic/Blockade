from Polje import Polje
from Player import Player
class Tabla:

    def __init__(self,dimX,dimY,listaX,listaO):
        self.Xpoz=listaX
        self.Opoz=listaO
        self.dimX=int(dimX)
        self.dimY=int(dimY)
        self.matrica=[[] * self.dimY] * self.dimX
        for i in range(dimX):
                self.matrica[i] = [Polje(i, j, " ") for j in range(dimY) ]
        print(self.Xpoz[0],self.Xpoz[1])
        print(self.Opoz[0],self.Opoz[1])

    
    def postavi_polje(self,posX,posY,tekst):
        self.matrica[posX-1][posY-1].vrednost=tekst
    def da_li_je_kraj(self,IgracX,IgracO):
        if(IgracX.s1(self.Opoz[0][0],self.Opoz[0][1]) 
        or IgracX.s2(self.Opoz[1][0],self.Opoz[1][1])
        or IgracX.s1(self.Opoz[1][0],self.Opoz[1][1]) 
        or IgracX.s2(self.Opoz[0][0],self.Opoz[0][1])):
            print("Pobednik je igrac O. Igra je zavrsena!")
            return True
        elif(IgracO.s1(self.Xpoz[0][0],self.Xpoz[0][1]) 
        or IgracO.s2(self.Xpoz[1][0],self.Xpoz[1][1]) 
        or IgracO.s1(self.Xpoz[1][0],self.Xpoz[1][1]) 
        or IgracO.s2(self.Xpoz[0][0],self.Xpoz[0][1])):
            print("Pobednik je igrac X. Igra je zavrsena!")
            return True
        else: return False
    
    def potez_pesak(self,posX,posY,igrac,broj):
        pesak=self.Xpoz if igrac=="X" else self.Opoz
        i=pesak[broj][0]-1
        j=pesak[broj][1]-1
        x=posX-1
        y=posY-1
        self.matrica[i][j].vrednost=" "
        if igrac=="X":
            self.Xpoz[broj][0]=posX
            self.Xpoz[broj][1]=posY
            self.postavi_polje(x+1,y+1,"X")
        else:
            self.Opoz[broj][0]=posX
            self.Opoz[broj][1]=posY
            self.postavi_polje(x+1,y+1,"O")
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
            else: return False
        elif(x>i):
            if(x==i+1 and y==j-1):
                s=self.dole_levo(i,j)
            elif(x==i+1 and y==j+1):
                s=self.dole_desno(i,j)
            elif(x==i+2 and y==j):
                s=self.dole(i,j)
            else: return False
        else:
            if(x==i and y==j-2):
                s=self.levo(i,j)
            elif(x==i and y==j+2):
                s=self.desno(i,j)
            else: return False
        return s
    def desno(self,i,j):
        return not (self.matrica[i][j+2].levizid=="I" or self.matrica[i][j].desnizid=="I")
    def levo(self,i,j):
        return not (self.matrica[i][j-2].desnizid=="I" or self.matrica[i][j].levizid=="I")
    def gore(self,i,j):
        return not (self.matrica[i-2][j].donjizid=="=" or self.matrica[i][j].gornjizid=="=")
    def dole(self,i,j):
        return not (self.matrica[i+2][j].gornjizid=="=" or self.matrica[i][j].donjizid=="=")
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

    def inicijalizacija_zidova(self):
            for i in range(self.dimX):
                for j in range(self.dimY):
                    self.matrica[i][j].levizid=self.matrica[i][j].desnizid="|"
                    self.matrica[i][j].gornjizid=self.matrica[i][j].donjizid="-"
                    self.matrica[i][j].gornjizid="=" if(i==0) else "-"
                    self.matrica[i][j].donjizid="=" if(i==self.dimX-1) else "-"
                    self.matrica[i][j].levizid="I" if(j==0) else "|"
                    self.matrica[i][j].desnizid="I" if(j==self.dimY-1) else "|"
    
    def stampanje(self):
                    print("  ")
                    for i in range(1,self.dimY+1):
                        print("  ",format(i, 'X'), end="")
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
                                                p=format(p,'X')
                                                m=str(p)+'I'
                                                print(m,end=" ")
                                                print(self.matrica[i][j].vrednost,end=" ")
                                                print(self.matrica[i][j].desnizid,end=" ")
                                            elif(j==self.dimY-1):
                                                print(self.matrica[i][j].vrednost,end=" ")
                                                p=format(p,'X')
                                                m='I'+str(p)
                                                print(m, end='')
                                            else:
                                                print(self.matrica[i][j].vrednost,end=" ")
                                                print(self.matrica[i][j].desnizid,end=" ")
                                        else:
                                            
                                            print("  ",self.matrica[i][j].donjizid,end="")
                                print()
                    for i in range(1,self.dimY+1):
                        print("  ",format(i, 'X'), end='')
                    print()
            

