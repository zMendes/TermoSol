import math

class Viga():
    def __init__(self, point_a, point_b, area, E,nodes):
        self.point_a = point_a
        self.point_b =  point_b
        self.area = area
        self.E = E
        self.gdl = [nodes[0]*2-2, nodes[0]*2-1,nodes[1]*2-2,nodes[1]*2-1]

    
    def getK(self):
        L = math.sqrt((point_b[0]-point_a[0])**2 + (point_b[1]-point_a[1])**2)
        sen = (point_b[1]-point_a[1])/L
        cos = (point_b[0]-point_a[0])/L

        self.K = np.array([
            [cos**2,cos*sen,-(cos**2),-(cos*sen)],
            [cos*sen,sen**2,-(cos*sen),-(s**2)],
            [-(cos**2),-(cos*sen),cos**2,cos*sen],
            [-(cos*sen),-(sen**2),cos*sen,s**2]
        ])
        self.K = self.K * E*A/L 
    
    def createM(self):

