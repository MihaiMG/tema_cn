import numpy as np
import os
import copy as cp
import random as rnd
_EPSILON = pow(10,-10)


def calculeaza_factor(a, matrice_initiala, sir):

    b = np.multiply(matrice_initiala,-1)
    c = np.multiply(b,sir)
    for index in range(0,len(c)):
        c[index,index] = c[index,index]+a

    return c

def li_2(numar_linii_coloane,genereaza,matrix):

    if genereaza is True:
        matrice = create_example_matrix(numar_linii_coloane)
    else:
        matrice_np = cp.deepcopy(matrix)

    #Am aflat V0 cu formula initiala
    #matrice_np = np.matrix(matrice)
    transpusa = np.transpose(matrice_np)

    #Calculam normele
    try:
        norma_1 = np.linalg.norm(matrice_np,ord=1)
        norma_inf = np.linalg.norm(matrice_np,ord=np.inf)
        produs = 1/(norma_1*norma_inf)
    except:
        print("Division by 0")
        return
    matrice_v0 = transpusa*produs
    matrice_v1 = cp.copy(matrice_v0)
    k =0 
    kmax = 10000

    norma_v0_v1 = _EPSILON+1
    limita_putere = pow(10,10)

    for k in range(kmax):

        matrice_v0 = cp.copy(matrice_v1)
        determinant = np.linalg.det(matrice_np)
        determinant3 = 3*determinant
        a_v0_3 = np.multiply(matrice_np,matrice_v0)
        #a_v0_3 *= -1
        #a_v0_3 += determinant3
        a_v0_3 -= (3*determinant)
        a_v0_patrat = np.multiply(a_v0_3,a_v0_3)

        a_v0_1 = np.multiply(matrice_v0,matrice_np)
        a_v0_1 -= determinant
        a_v0 = np.multiply(a_v0_1,a_v0_3)
        a_v0 *= 0.25
        a_v0 += determinant
        matrice_v1 = np.multiply(a_v0,matrice_v0)

        diferenta_v0_v1 = np.subtract(matrice_v0,a_v0)
        norma_v0_v1 = np.linalg.norm(diferenta_v0_v1)


        if norma_v0_v1 < _EPSILON or norma_v0_v1 > limita_putere:
            break
        
    if norma_v0_v1 < _EPSILON:
        print("Matricea este convergenta")
        matrice_inm = np.multiply(matrice_np,matrice_v1)
        det = np.linalg.det(matrice_np)
        matrice_inm -= det
        norma = np.linalg.norm(matrice_inm,ord=1)
        print("Norma: "+str(norma))
        print("Matrice initiala :")
        print(matrice_np)
        print("Matrice inversa : ")
        print(matrice_v1)
    else:
        print("Numarul de iteratii : {0}".format(k))
        print("Maatricea este divergenta")
     


def li_1(numar_linii_coloane,genereaza,matrix):

    if genereaza is True:
        matrice = create_example_matrix(numar_linii_coloane)
    else:
        matrice_np = cp.deepcopy(matrix)

    #Am aflat V0 cu formula initiala
    #matrice_np = np.matrix(matrice)
    transpusa = np.transpose(matrice_np)

    #Calculam normele
    try:
        norma_1 = np.linalg.norm(matrice_np,ord=1)
        norma_inf = np.linalg.norm(matrice_np,ord=np.inf)
        produs = 1/(norma_1*norma_inf)
    except:
        print("Division by 0")
        return

    matrice_v0 = transpusa * produs
    matrice_v1 = cp.copy(matrice_v0)
    k =0 
    kmax = 10000

    norma_v0_v1 = _EPSILON+1
    limita_putere = pow(10,10)
    for k in range(kmax):

        matrice_v0 = cp.copy(matrice_v1)
        
        matrice_a_v = np.multiply(matrice_np,matrice_v0)
        determinant = np.linalg.det(matrice_np)
        matrice_a_v -= (3*determinant)
        matrice_a_v = np.multiply(matrice_v0,matrice_a_v)
        matrice_a_v = np.multiply(matrice_np,matrice_a_v)
        matrice_a_v -= (3*determinant)
        matrice_v1  = np.multiply(matrice_v0,matrice_a_v)

        diferenta_v0_v1 = np.subtract(matrice_v0,matrice_v1)
        norma_v0_v1 = np.linalg.norm(diferenta_v0_v1)
        if norma_v0_v1 < _EPSILON or norma_v0_v1 > limita_putere:
            break
        
    if norma_v0_v1 < _EPSILON:
        print("Matricea este convergenta")
        matrice_inm = np.multiply(matrice_np,matrice_v1)
        det = np.linalg.det(matrice_np)
        matrice_inm -= det
        norma = np.linalg.norm(matrice_inm,ord=1)
        print("Norma: "+str(norma))
        print("Matrice initiala :")
        print(matrice_np)
        print("Matrice inversa : ")
        print(matrice_v1)
    else:
        print("Numarul de iteratii : {0}".format(k))
        print("Maatricea este divergenta")
    

def schultz(numar_linii_coloane,genereaza,matrix):
    
    if genereaza is True:
        matrice = create_example_matrix(numar_linii_coloane)
    else:
        matrice_np = matrix


    #Am aflat V0 cu formula initiala
    #matrice_np = np.matrix(matrice)
    transpusa = np.transpose(matrice_np)

    #Calculam normele
    try:
        norma_1 = np.linalg.norm(matrice_np,ord=1)
        norma_inf = np.linalg.norm(matrice_np,ord=np.inf)
        produs = 1/(norma_1*norma_inf)
    except:
        print("Division by 0")
        return

    matrice_v0 = transpusa*produs
    matrice_v1 = cp.copy(matrice_v0)
    k =0 
    kmax = 1000

    limita_putere =pow(10,10)
    for k in range(kmax):

        matrice_v0 = cp.copy(matrice_v1)

        matrice_a = np.matmul(matrice_np,matrice_v0)
        matrice_a += -(2*np.linalg.det(matrice_np))
        matrice_v1  = np.matmul(matrice_v0,matrice_a)


        diferenta_v0_v1 = np.subtract(matrice_v0,matrice_v1)
        norma_v0_v1 = np.linalg.norm(diferenta_v0_v1)
        if norma_v0_v1 < _EPSILON or norma_v0_v1 > limita_putere:
            break
        
    if norma_v0_v1 < _EPSILON:
        print("Matricea este convergenta")
        matrice_inm = np.multiply(matrice_np,matrice_v1)
        det = np.linalg.det(matrice_np)
        matrice_inm -= det
        norma = np.linalg.norm(matrice_inm,ord=1)
        print("Norma: "+str(norma))
        print("Matrice initiala :")
        print(matrice_np)
        print("Matrice inversa : ")
        print(matrice_v1)
    else:
        print("Numarul de iteratii : {0}".format(k))
        print("Maatricea este divergenta")
        print("Matrice initiala :")
        print(matrice_np)
        print("Matrice inversa : ")
        print(matrice_v1)


def create_example_matrix(numar_linii_coloane):
    matrice = []
    for i in range(numar_linii_coloane):

        if i == numar_linii_coloane - 1:
            linie_matrice = [0 for x in range(i)]
            linie_matrice.append(1)
        else:
            linie_matrice = [0 for x in range(i)]
            linie_matrice.append(1)
            linie_matrice.append(4)
            for x in range(i+2,numar_linii_coloane):
                linie_matrice.append(0)

        matrice.append(linie_matrice)
    return matrice


if __name__ == "__main__":
    
    #matrice = []
    #for x in range(4):
        #lista = [x+1 if x%2==0 else x+10 for x in range(4)]
        #lista = [0 for x in range(4)]
        #matrice.append(lista)
    #matrice2 = np.matrix(matrice)

    forma = 4
    matrice = create_example_matrix(forma)
    matrice2 = np.ndarray(shape=(forma,forma), dtype=float)

    schultz(10,False,matrice2)
    #li_2(10,False,matrice2)
    #li_1(10,False,matrice2)