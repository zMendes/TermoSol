##imports
import math
import numpy as np 
from funcoesTermosol import importa 
from elemento import Element 
from ponte import Ponte

##Pegando dados da tabela
[n_nos, nos_coord, n_elements, param , n_force, force_matrix, n_restric, restric_matrix] = importa('entrada.xlsx')
#print(param)
element = []
nodes = []
U = [0,0,0]
force_matrix = force_matrix[3:6]
for i in param:
    nodes.append(np.array([int(i[0]),int(i[1])]))
# print(nodes)

dict_nos = {}

for i in range(0,n_nos):
    dict_nos[i+1] = [nos_coord[0][i], nos_coord[1][i]]
    
for i in range(0,n_nos):    
    element.append(Element(dict_nos.get(int(param[i][0])),dict_nos.get(int(param[i][1])),param[i][3],param[i][2],nodes[i]))


ponte = Ponte(element,force_matrix,U,n_nos)
ponte.getKis()
ponte.getKg()
print(ponte.Kg)
