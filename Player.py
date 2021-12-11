from Pion import Pion
class Player:
    def __init__(self,name,start1,start2,brplavih,brzelenih):
        self.name=name
        self.start1=start1 
        self.start2=start2
        self.lista=[Pion(start1[0],start1[1],1,self.name),Pion(start2[0],start2[1],2,self.name)]
        self.brojPlavihZidova=int(brplavih)
        self.brojZelenihZidova=int(brzelenih)
    def s1(self,posx,posy):
        if(self.start1[0] ==posx and self.start1[1]==posy):
            return True
        return False
    def s2(self,posx,posy):
        if(self.start2[0] ==posx and self.start2[1]==posy):
            return True
        return False
    def stampanje(self):
        print("Broj preostalih plavih zidova je: ",self.brojPlavihZidova)
        print("Broj preostalih zelenih zidova je: ",self.brojZelenihZidova)
    def get__start1(self):
            return self.Polje
    def oduzmizid(self,boja):
        if(str(boja)=='Z'):
            self.brojZelenihZidova-=1 
        else:
            self.brojPlavihZidova-=1 
    
    def promeniPoziciju(self,node):
            self.Polje.vrednost=" "
            self.Polje=node