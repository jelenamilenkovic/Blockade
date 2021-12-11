
class Pion:
    def __init__(self,trX,trY,rednibroj,name):
        self.name=name
        self.trX=trX
        self.trY=trY
        self.rednibroj=rednibroj

    def vratitrenutnomestoX(self):
          return self.trX
    def vratitrenutnomestoY(self):
          return self.trY
    def postavinove(self,trXX,trYY):
        self.trX=trXX
        self.trY=trYY