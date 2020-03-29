import math
import numpy as np
class Element():
    def __init__(self, point_a, point_b, area, E,nodes):
        self.point_a = point_a
        self.point_b =  point_b
        self.area = area
        self.E = E
        self.nodes = nodes
        self.gdl = [nodes[0]*2-2, nodes[0]*2-1,nodes[1]*2-2,nodes[1]*2-1]
        self.L = math.sqrt((self.point_b[0]-self.point_a[0])**2 + (self.point_b[1]-self.point_a[1])**2)
        self.sen = (self.point_b[1]-self.point_a[1])/self.L
        self.cos = (self.point_b[0]-self.point_a[0])/self.L
        self.U = []
        #print(self.gdl)

        
    # Deformacoes
    def getEpsi(self):
        m = np.array([-self.cos,-self.sen,self.cos,self.sen])
        self.Epsi = (1/self.L) * (m.dot(self.U)) 
    
    # Tensoes normais internas
    def getTi(self):
        self.Ti = self.E * self.Epsi
    
    # Esforcos normais internos
    def getFi(self):
        self.Fi = self.Ti*self.area
    
    def getK(self):
        self.K = (self.E*self.area/self.L) * np.array([
            [self.cos**2,self.cos*self.sen,-(self.cos**2),-(self.cos*self.sen)],
            [self.cos*self.sen,self.sen**2,-(self.cos*self.sen),-(self.sen**2)],
            [-(self.cos**2),-(self.cos*self.sen),self.cos**2,self.cos*self.sen],
            [-(self.cos*self.sen),-(self.sen**2),self.cos*self.sen,self.sen**2]
        ])
    

