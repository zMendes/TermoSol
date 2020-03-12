##imports
import math
import numpy as np 
from funcoesTermosol import importa 
from elemento import Element 
from ponte import Ponte

##Pegando dados da tabela
[n_nos, nos_coord, n_elements, param , n_force, force_matrix, n_restric, restric_matrix] = importa('entrada.xlsx')
print(param)

element = []

for i in range(0,n_elements):
    print(nos_coord[0][i], nos_coord[1][i])
    #element.append(Element(nos_coord[0][i],nos_coord[1][i],param[i][3],param[i][2],[param[i][0],param[i][1]]))
    #element[i].getK()


#print(len(element.k))