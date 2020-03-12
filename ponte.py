

class Ponte():
    def __init__(self, elements, F, U, n_nos):
        self.elements = elements
        self.F = F
        self.U = U
        self.n_nos = n_nos
        self.Kg = np.zeros([n_nos*2,n_nos*2])

    def getKis(self):
        for element in self.elements:
            element.getK()
    
    def getKg(self):
        for element in self.elements:
            self.Kg[element.gdl[0]:element.gdl[1]+1][element.gdl[0]:element.gdl[1]+1] += element.k[0:2][0:2]
            self.Kg[element.gdl[2]:element.gdl[3]+1][element.gdl[2]:element.gdl[3]+1] += element.k[2:4][2:4] 
            self.Kg[element.gdl[0]:element.gdl[1]+1][element.gdl[2]:element.gdl[3]+1] += element.K[0:2][2:4] 
            self.Kg[element.gdl[2]:element.gdl[3]+1][element.gdl[0]:element.gdl[1]+1] += element.k[2:4][0:2] 



