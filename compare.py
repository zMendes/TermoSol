import numpy as np

def gauss(ite,tol,A,b):
    X = []
    x0 = np.array([[0,0,0]])
    X.append(x0)
    i = 0
    tempXa= (b[0] - A[0][1] * X[i][0][1] - A[0][2])/A[0][0]
    tempXb = (b[1]-A[1][0]*X[i][0][0]-A[1][2]*X[i][0][2])/A[1][1]
    tempXc =  (b[2] - A[2][0]*X[i][0][0] - A[2][1]*X[i][0][1])/A[2][2]
    X.append(np.array([[tempXa,tempXb,tempXc]]))
    while ( np.amax(X[i])==0 or np.abs((np.amax(X[i]) - np.amax(X[i-1]))/np.amax(X[i]))>np.amax(tol)):
        tempXa= (b[0] - A[0][1] * X[i][0][1] - A[0][2])/A[0][0]
        tempXb = (b[1]-A[1][0]*X[i][0][0]-A[1][2]*X[i][0][2])/A[1][1]
        tempXc =  (b[2] - A[2][0]*X[i][0][0] - A[2][1]*X[i][0][1])/A[2][2]
        X.append(np.array([[tempXa,tempXb,tempXc]]))
        i +=1

    return X[-1]

    
Kg = np.array([[10e8  * 1.59,10e8 * (-0.4),10e8 *(-0.54)],[10e8  * (-0.4),10e8  * 1.7, 10e8  * 0.4],[10e8  * -0.54,10e8  *0.4,10e8  * 0.54]])

Pg = [0,150,-100]

print(gauss(300,10e-7,Kg,Pg))
