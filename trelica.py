import numpy as np
import entradas from funcoesTermosol.py 
a = 0
tamanho =2
A = 0.02
E = 200e9
P = 50e3

nElementos = 3
L = tamanho/nElementos
K = E*A/L * np.array([[1,-1],[-1,1]])
    kGlobal = np.zeros([nElementos+1, nElementos+1])
#print(kGlobal)
for i in range(nElementos):
    kGlobal[i][i] += 1
    kGlobal[i][i+1] += -1
    kGlobal[i+1][i] += -1
    kGlobal[i+1][i+1] += 1  


print(kGlobal * E*A/L )
#F = [0, P]
u = [0, a]
def condicoesContorno(u):
    for i in range(len(u)):
        if u[i] ==0:
            K = np.delete(K,i,0)
            K = np.delete(K,i,1)


#print(K)
#print(np.linalg.inv(K) * F)

