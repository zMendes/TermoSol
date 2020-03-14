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
            self.Kg_c = np.delete(self.Kg,self.restric_matrix,0)
            self.Kg_c = np.delete(self.Kg_c,self.restric_matrix,1)
            self.F_c = np.delete(self.F, self.restric_matrix)
            u_temp = np.linalg.inv(self.Kg_c).dot(self.F_c)
            j = 0
            for i in range(len(self.U)):
                if i not in self.restric_matrix:
                    self.U[i] = u_temp[j]
                    j +=1
    
    def getReact(self):
        return self.Kg.dot(self.U)
    
    def gauss(self, iteration, tolerance):
        X = np.zeros(len(self.F_c))
        i = 0
        last = X
        X[0]= ( self.F_c[0] - self.Kg_c[0][1] * X[1] - self.Kg_c[0][2] * X[2])/self.Kg_c[0][0]
        X[1] = ( self.F_c[1] - self.Kg_c[1][0] * X[0] - self.Kg_c[1][2] * X[2])/self.Kg_c[1][1]
        X[2] = ( self.F_c[2] - self.Kg_c[2][0] * X[0] - self.Kg_c[2][1] * X[1])/self.Kg_c[2][2]

        current = abs((max(X)-max(last))/max(X)*100)
        while(current>tolerance or i<iteration):
            X[0] = ( self.F_c[0] - self.Kg_c[0][1] * X[1] - self.Kg_c[0][2] * X[2])/self.Kg_c[0][0]
            X[1] = ( self.F_c[1] - self.Kg_c[1][0] * X[0] - self.Kg_c[1][2] * X[2])/self.Kg_c[1][1]
            X[2] = ( self.F_c[2] - self.Kg_c[2][0] * X[0] - self.Kg_c[2][1] * X[1])/self.Kg_c[2][2]
            last = X
            i+=1
            current = abs((max(X)-max(last))/max(X)*100)
        print("N iteraçoes: ", i)

        return X
            

    def jacobi(self, iteration, tolerance):
        X = np.zeros(len(self.F_c))
        
        D = np.diag(self.Kg_c)
        R = self.Kg_c - np.diagflat(D)
        i = 0
        current = 100
        while (current>tolerance or i<iteration):
            last = X
            X = (self.F_c - np.dot(R,X))/ D
            current = abs((max(X)-max(last))/max(X)*100)
            i+=1
        return X



