import numpy as np

class Ponte():
    def __init__(self, elements, F, U, n_nos,restric_matrix):
        self.elements = elements
        self.F = F
        self.U = U
        self.n_nos = n_nos
        self.restric_matrix = restric_matrix
        self.Kg = np.zeros([n_nos*2,n_nos*2])

    def getKis(self):
        for element in self.elements:
            element.getK()
    
    def getKg(self):
        for element in self.elements:
            self.Kg[element.gdl[0]:element.gdl[1]+1,element.gdl[0]:element.gdl[1]+1] += element.K[0:2,0:2]
            self.Kg[element.gdl[2]:element.gdl[3]+1,element.gdl[2]:element.gdl[3]+1] += element.K[2:4,2:4] 
            self.Kg[element.gdl[0]:element.gdl[1]+1,element.gdl[2]:element.gdl[3]+1] += element.K[0:2,2:4] 
            self.Kg[element.gdl[2]:element.gdl[3]+1,element.gdl[0]:element.gdl[1]+1] += element.K[2:4,0:2]

    def condicContorno(self):
            self.Kg = np.delete(self.Kg,self.restric_matrix,0)
            self.Kg = np.delete(self.Kg,self.restric_matrix,1)
            self.F = np.delete(self.F, self.restric_matrix)
            # self.U = np.linalg.inv(self.Kg) * self.F
            self.U = np.linalg.inv(self.Kg).dot( self.F)
    
            


