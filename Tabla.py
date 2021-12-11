from Polje import Polje
from Player import Player
class Tabla:

    def __init__(self,dimX,dimY):
        self.dimX=int(dimX)
        self.dimY=int(dimY)
        self.matrica=[[] * self.dimY] * self.dimX
        for i in range(dimX):
                self.matrica[i] = [Polje(i, j, " ") for j in range(dimY) ]

             
    def postaviPolje(self,posX,posY,Pion):
        self.matrica[posX-1][posY-1].vrednost=Pion.name
        
    def pomeriPiona(self,posX,posY,Pion):
        i=Pion.vratitrenutnomestoX() -1
        j=Pion.vratitrenutnomestoY() -1
     
        x=posX-1
        y=posY-1
        h=False
        h=self.possible(i,j,x,y)
        if(h==True):
            self.matrica[i][j].vrednost=" "
            Pion.postavinove(posX,posY)
            self.postaviPolje(x+1,y+1,Pion)
        else:
            print("Ne moze se preci na to mesto!")
        
    

    def possible(self,i,j,x,y):
        s=True
        if(x<i):
            if(x==i-1 and y==j-1):
               s=self.funcgorelevo(x,y,i,j)
            elif(x==i-1 and y==j+1):
               s=self.funcgoredesno(x,y,i,j)
            elif(x==i-2 and y==j):
                s=self.funcgore(x,y,i,j)
            else: return False
        elif(x>i):
            if(x==i+1 and y==j-1):
                s=self.funcdolelevo(x,y,i,j)
            elif(x==i+1 and y==j+1):
                s=self.funcdoledesno(x,y,i,j)
            elif(x==i+2 and y==j):
                s=self.funcdole(x,y,i,j)
            else: return False
        else:
            if(x==i and y==j-2):
                s=self.funclevo(x,y,i,j)
            elif(x==i and y==j+2):
                s=self.funcdesno(x,y,i,j)
            else: return False
        return s
    def funcdesno(self,x,y,i,j):
        if(self.matrica[i][j+2].levizid=="I" or self.matrica[i][j].desnizid=="I"):
            return False
        return True
    def funclevo(self,x,y,i,j):
        if(self.matrica[i][j-2].desnizid=="I" or self.matrica[i][j].levizid=="I"):
            return False
        return True
    def funcgore(self,x,y,i,j):
        if(self.matrica[i-2][j].donjizid=="=" or self.matrica[i][j].gornjizid=="="):
            return False
        return True
    def funcdole(self,x,y,i,j):
        if(self.matrica[i+2][j].gornjizid=="=" or self.matrica[i][j].donjizid=="="):
            return False
        return True
    def funcdoledesno(self,x,y,i,j):
        if(self.matrica[i+1][j+1].gornjizid=="=" and self.matrica[i+1][j+1].levizid=="I"):
            return False
        if(self.matrica[i][j].donjizid=="=" and self.matrica[i][j].desnizid=="I"):
            return False
        if(self.matrica[i+1][j+1].gornjizid=="=" and self.matrica[i][j].donjizid=="="):
            return False
        if(self.matrica[i+1][j+1].levizid=="I" and self.matrica[i][j].desnizid=="I"):
            return False
        return True
    def funcdolelevo(self,x,y,i,j):
        if(self.matrica[i+1][j-1].gornjizid=="=" and self.matrica[i+1][j-1].desnizid=="I"):
            return False
        if(self.matrica[i][j].donjizid=="=" and self.matrica[i][j].levizid=="I"):
            return False
        if(self.matrica[i+1][j-1].gornjizid=="=" and self.matrica[i][j].donjizid=="="):
            return False
        if(self.matrica[i+1][j-1].desnizid=="I" and self.matrica[i][j].levizid=="I"):
            return False
        return True
    def funcgorelevo(self,x,y,i,j):
        if(self.matrica[i-1][j-1].donjizid=="=" and self.matrica[i-1][j-1].desnizid=="I"):
            return False
        if(self.matrica[i][j].gornjizid=="=" and self.matrica[i][j].levizid=="I"):
            return False
        if(self.matrica[i-1][j-1].donjizid=="=" and self.matrica[i][j].gornjizid=="="):
            return False
        if(self.matrica[i-1][j-1].desnizid=="I" and self.matrica[i][j].levizid=="I"):
            return False
        return True
    def funcgoredesno(self,x,y,i,j):
        if(self.matrica[i-1][j+1].donjizid=="=" and self.matrica[i-1][j+1].levizid=="I"):
            return False
        if(self.matrica[i][j].gornjizid=="=" and self.matrica[i][j].desnizid=="I"):
            return False
        if(self.matrica[i-1][j+1].donjizid=="=" and self.matrica[i][j].gornjizid=="="):
            return False
        if(self.matrica[i-1][j+1].levizid=="I" and self.matrica[i][j].desnizid=="I"):
            return False
        return True
    def postavizid(self,posX,posY,boja):
        m=int(posX)
        n=int(posY)
        if(boja=="Z"):
            if(self.matrica[m-1][n-1].desnizid!="I" and self.matrica[m][n-1].desnizid!="I"):
                self.matrica[m-1][n-1].desnizid="I"
                self.matrica[m-1][n].levizid="I"
                self.matrica[m][n-1].desnizid="I"
                self.matrica[m][n].levizid="I"
                return True
            else:
                return False
        elif(boja=="P"):
            if(self.matrica[m-1][n-1].donjizid!="=" and self.matrica[m-1][n].donjizid!="="):
                self.matrica[m-1][n-1].donjizid="=" 
                self.matrica[m][n-1].gornjizid="=" 
                self.matrica[m-1][n].donjizid="="
                self.matrica[m][n].gornjizid="="  
                return True
            else:
                return False
        else:
            return False
        
    def vratiPolje(self,posx,posy):
            return self.matrica[posx][posy]

    def valid_move(node, tabla):
        if node.dimX < 0 or node.dimX > 7 or node.dimY < 0 or node.dimY > 7 or tabla[node.dimX][node.dimY] == "X" or tabla[node.dimX][node.dimY] == "O" :
             return False
        return True
    
    def InicijalizacijaZidova(self):
            for i in range(self.dimX):
                for j in range(self.dimY):
                    self.matrica[i][j].levizid=self.matrica[i][j].desnizid="|"
                    self.matrica[i][j].gornjizid=self.matrica[i][j].donjizid="-"
                    self.matrica[i][j].gornjizid="=" if(i==0) else "-"
                    self.matrica[i][j].donjizid="=" if(i==self.dimX-1) else "-"
                    self.matrica[i][j].levizid="I" if(j==0) else "|"
                    self.matrica[i][j].desnizid="I" if(j==self.dimY-1) else "|"
    

    def get_destination(Polje,matrica):
        all_destinations= [matrica[Polje.dimX-2][Polje.dimY], 
        matrica[Polje.dimX-1][Polje.dimY-1],
        matrica[Polje.dimX-1][Polje.dimY+1],
        matrica[Polje.dimX][Polje.dimY-2],
        matrica[Polje.dimX][Polje.dimY+2],
        matrica[Polje.dimX+1][Polje.dimY-1],
        matrica[Polje.dimX+1][Polje.dimY+1],
        matrica[Polje.dimX+2][Polje.dimY]]
        #return list(x for x in all_destinations if valid_move(x, matrica))
    
    def Stampanje(self):
        
                    for i in range(1,self.dimY+1):
                        print("  ",format(i, 'X'), end='')
                    print()
                    for i in range(1,self.dimY+1):
                        print("  ","=", end='')
                    print()
                    for i in range(0,self.dimX):
                            for t in range(2):
                                for j in range(self.dimY):
                                    
                                        if(t==0):
                                            p=i+1
                                            if(j==0):
                                                print(format(p, 'X'),self.matrica[i][j].levizid, end='')
                                                print(self.matrica[i][j].vrednost,end=" ")
                                                print(self.matrica[i][j].desnizid,end=" ")
                                            elif(j==self.dimY-1):
                                                print(self.matrica[i][j].vrednost,end=" ")
                                                print(self.matrica[i][j].desnizid,format(p, 'X'), end='')
                                            else:
                                                print(self.matrica[i][j].vrednost,end=" ")
                                                print(self.matrica[i][j].desnizid,end=" ")
                                        else:
                                            print("  ",self.matrica[i][j].donjizid,end="")
                                print()
                    for i in range(1,self.dimY+1):
                        print("  ",format(i, 'X'), end='')
                    print()
            
                    
