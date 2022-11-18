from Pion import Pion
from math import inf
import heapq
class Player:
    def __init__(self,name,start1,start2,brplavih,brzelenih):
        self.name=name
        self.start1=start1 
        self.start2=start2
        self.lista=[Pion(start1[0],start1[1],1,self.name),Pion(start2[0],start2[1],2,self.name)]
        self.brojPlavihZidova=int(brplavih)
        self.brojZelenihZidova=int(brzelenih)
    def s1(self,posx,posy):
        return (self.start1[0] ==posx and self.start1[1]==posy)
    def s2(self,posx,posy):
        return (self.start2[0] ==posx and self.start2[1]==posy)
    def stampanje(self):
        print("Broj preostalih plavih zidova je: ",self.brojPlavihZidova)
        print("Broj preostalih zelenih zidova je: ",self.brojZelenihZidova)
    
    def proveri_zid(self,boja):
        if(str(boja)=='Z'):
            if(self.brojZelenihZidova>0):
                return True
            else: 
                return False
        else:
            if(self.brojPlavihZidova>0):
                return True
            else: 
                return False
          
    def menhetn_rastojanje(self,racunar,tabela):
        suma=0
        for pesak in tabela.Xpoz:
            d1=abs(pesak[0]-tabela.Ostart[0][0])+abs(pesak[1]-tabela.Ostart[0][1])
            d2=abs(pesak[0]-tabela.Ostart[1][0])+abs(pesak[1]-tabela.Ostart[1][1])
            if(racunar=="X"):
                if d1==0 or d2==0:
                    return inf
                else:
                    suma+=1/d1 + 1/d2
            else:
                if d1==0 or d2==0:
                    return-inf
                else:
                    suma-=1/d1 + 1/d2

        for pesak in tabela.Opoz:
            d1 = abs(pesak[0]-tabela.Xstart[0][0])+abs(pesak[1]-tabela.Xstart[0][1])
            d2 = abs(pesak[0]-tabela.Xstart[1][0])+abs(pesak[1]-tabela.Xstart[1][1])
            if(racunar=="O"):
                if d1==0 or d2==0:
                    return inf
                else:
                    suma+=1/d1 + 1/d2
            else:
                if d1==0 or d2==0:
                    return-inf
                else:
                    suma-=1/d1 + 1/d2
        return suma
    def oduzmi_zid(self,boja):
        if(str(boja)=='Z'):
            if(self.brojZelenihZidova>0):
                self.brojZelenihZidova-=1 
                return True
            else: 
                return False
        else:
            if(self.brojPlavihZidova>0):
                self.brojPlavihZidova-=1 
                return True
            else: 
                return False
class Covek(Player):
    def __init__(self,name,start1,start2,brplavih,brzelenih):
        super().__init__(name,start1,start2,brplavih,brzelenih)
class Kompjuter(Player):
    def __init__(self, name, start1, start2, brplavih, brzelenih):
        super().__init__(name, start1, start2, brplavih, brzelenih)