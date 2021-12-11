class Polje:
    def __init__(self,posX,posY,vrednost):
            self.posY=posY
            self.posX=posX
            self.vrednost=vrednost
            self.startnoPolje=False
            self.levizid="|"
            self.desnizid="|"
            self.gornjizid="-"
            self.donjizid="-"

    def dalijestartno(self):
        return True if(self.startnoPolje==True) else False
    def promenizid(self):
        self.desnizid="I"
