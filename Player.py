from Pion import Pion
class Player:
    def __init__(self,name,start1,start2,brplavih,brzelenih):
        self.name=name
        self.start1=start1 
        self.start2=start2
        self.racunar=False
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
               # self.brojZelenihZidova-=1 
                return True
            else: 
                return False
        else:
            if(self.brojPlavihZidova>0):
               # self.brojPlavihZidova-=1 
                return True
            else: 
                return False
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