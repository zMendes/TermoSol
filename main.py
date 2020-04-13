# -*- Coding: UTF-8 -*-
#coding: utf-8
##imports
import math
import numpy as np 
from funcoesTermosol import importa, plota, geraSaida 
from elemento import Element 
from ponte import Ponte

ruptura = 18e6

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

Epsi_ = np.matrix(Epsi)
Fi_ = np.matrix(Fi)
Ti_ = np.matrix(Ti)
geraSaida("nice",F,U, Epsi_.getT(),Fi_.getT(),Ti_.getT())
quebrou = []
deformou = []
deslocou = []

for i in Ti:
    # print(i)
    if np.abs(i)> ruptura:
        quebrou.append(i)
if (quebrou != []):
    print("O membro ultrapassou a tensão de ruptura em tração/compressão. Membros: ",quebrou)

for i in Epsi:
    if np.abs(i)>0.5:
        deformou.append(i)
if (deformou != []):
    print("Algum membro teve deformação maior do que 5%. Membros: ",deformou)

for i in U:
    if np.abs(i)>0.02:
        deslocou.append(i)
if (deslocou != []):
    print("Algum nó se deslocou mais do que 20mm em X ou em Y. Membros: ", deslocou)
