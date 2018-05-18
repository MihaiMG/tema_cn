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
        matrice_np = cp.copy(matrix)

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

    matrice_v = transpusa*produs
    matrice_v1 = cp.copy(matrice_v)
    k =0 
    kmax = 1000

    limita_putere =pow(10,10)

    matrice_b = -1 * matrice_v

    for k in range(kmax):

        matrice_v0 = cp.copy(matrice_v1)

        matrice_v0 = cp.copy(matrice_v1)
        matrice_c_1 = np.matmul(matrice_v0,matrice_b)
        for i in range(numar_linii_coloane-1):
            matrice_c_1[i,i] += 0
        matrice_c_1 *= 0.25

        matrice_c_2 = np.matmul(matrice_v0,matrice_b)
        for i in range(numar_linii_coloane-1):
            matrice_c_2[i,i] += 3
        matrice_c_patrat = np.linalg.matrix_power(matrice_c_2,2)
        matrice_f = np.matmul(matrice_c_1,matrice_c_patrat)
        determinant = np.linalg.det(matrice_np)
        matrice_f += determinant

        matrice_finala = np.matmul(matrice_f,matrice_v0)
        matrice_v1 = matrice_finala

        diferenta_v0_v1 = np.subtract(matrice_v1,matrice_v0)
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


def li_1(numar_linii_coloane,genereaza,matrix):

    if genereaza is True:
        matrice = create_example_matrix(numar_linii_coloane)
    else:
        matrice_np = cp.copy(matrix)

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

    matrice_v = transpusa*produs
    matrice_v1 = cp.copy(matrice_v)
    k =0 
    kmax = 1000

    limita_putere =pow(10,10)

    matrice_b = -1 * matrice_v

    for k in range(kmax):

        #matrice_v0 = cp.copy(matrice_v1)
        
        #calculam #3In - AVk0
        matrice_v0 = cp.copy(matrice_v1)
        matrice_c_1 = np.matmul(matrice_b,matrice_v0)
        for i in range(numar_linii_coloane-1):
            matrice_c_1[i,i] += 3
        matrice_v_k = np.matmul(matrice_v0,matrice_c_1)
        matrice_c_2  = np.matmul(matrice_b,matrice_v_k)

        #matrice_d = np.matmul(matrice_b,matrice_v0_0)
        for i in range(numar_linii_coloane-1):
            matrice_c_2[i,i] += 3

        matrice_v1  = np.matmul(matrice_v0,matrice_c_2)

        diferenta_v0_v1 = np.subtract(matrice_v1,matrice_v0)
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
    

def schultz(numar_linii_coloane,genereaza,matrix):
    
    if genereaza is True:
        matrice = create_example_matrix(numar_linii_coloane)
    else:
        matrice_np = matrix


    #Am aflat V0 cu formula initiala
    #matrice_np = np.ndarray(shape=(numar_linii_coloane,numar_linii_coloane), dtype=float)
    transpusa = np.transpose(matrice_np)

    #Calculam normele
    try:
        norma_1 = np.linalg.norm(matrice_np,ord=1)
        norma_inf = np.linalg.norm(matrice_np,ord=np.inf)
        produs = 1/(norma_1*norma_inf)
    except:
        print("Division by 0")
        return

    matrice_v = transpusa*produs
    matrice_v1 = cp.copy(matrice_v)
    k =0 
    kmax = 1000

    limita_putere =pow(10,10)

    matrice_b = -1 * matrice_v
    
    #matrice_c = np.matmul(matrice_b,matrice_v0)
    #for i in range(numar_linii_coloane-1):
    #    matrice_c[i,i] += 2

    for k in range(kmax):

        matrice_v0 = cp.copy(matrice_v1)
        matrice_c = np.matmul(matrice_b,matrice_v0)
        for i in range(numar_linii_coloane-1):
            matrice_c[i,i] += 2
        matrice_v1  = np.matmul(matrice_v0,matrice_c)


        diferenta_v0_v1 = np.subtract(matrice_v1,matrice_v0)
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

    forma = 3
    matrice = create_example_matrix(forma)
    matrice2 = np.asarray(matrice, dtype=float)
    print(matrice2)
    #schultz(3,False,matrice2)
    li_2(3,False,matrice2)
    #li_1(3,False,matrice2)