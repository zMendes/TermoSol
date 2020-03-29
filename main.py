##imports
import math
import numpy as np 
from funcoesTermosol import importa, plota, geraSaida 
from elemento import Element 
from ponte import Ponte

##Pegando dados da tabela
[n_nos, nos_coord, n_elements, param , n_force, force_matrix, n_restric, restric_matrix] = importa('entrada.xlsx')
#plota(nos_coord,param)
element = []
nodes = []
plota(nos_coord,param)
dict_nos = {}
U = np.zeros([n_nos*2])
for i in param:
    #print(i[0],i[1])
    nodes.append(np.array([int(i[0]),int(i[1])]))
for i in range(0,n_nos):

    dict_nos[i+1] = [nos_coord[0][i], nos_coord[1][i]]
for i in range(0,n_elements):    
    #print()
    element.append(Element(dict_nos.get(int(param[i][0])),dict_nos.get(int(param[i][1])),param[i][3],param[i][2],nodes[i]))

ponte = Ponte(element,force_matrix,U,n_nos,restric_matrix,n_restric)
ponte.getKis()
ponte.getKg()
ponte.condicContorno()
ponte.setU()
#FORÇAS DE REAÇÃO
#geraSaida("Nice", F,U,)
ponte.getReact()
F,U, Epsi,Fi,Ti = ponte.makeGraph()
geraSaida("nice",F,U, Epsi,Fi,Ti)
#print("\nCálculo de U utilizando método de Jacobi: ", ponte.jacobi(10,0.001))
#print("\n Cálculo de U utilizando o método de Gauss: ", ponte.gauss(10,0.1))
