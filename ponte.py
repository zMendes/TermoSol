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
            Kg_c = np.delete(self.Kg,self.restric_matrix,0)
            Kg_c = np.delete(Kg_c,self.restric_matrix,1)
            F_c = np.delete(self.F, self.restric_matrix)
            u_temp = np.linalg.inv(Kg_c).dot(F_c)
            j = 0
            for i in range(len(self.U)):
                if i not in self.restric_matrix:
                    self.U[i] = u_temp[j]
                    j +=1
    
    def getReact(self):
        return self.Kg.dot(self.U)
        
            


