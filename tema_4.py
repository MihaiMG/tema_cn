import tema_3
import pickle
import sys
import numpy

_EPSILON = pow(10,-8)


def calculate_sum_2(index_linie, vector_xp, linie_matrice):

    elemente_peste_index = [x for x in linie_matrice if x[1] > index_linie]
    vector_peste_index = [x for x in range(index_linie, len(linie_matrice)-1)]

    suma =0
    for element in elemente_peste_index:
        el1 = element[0]
        el2 = vector_xp[element[1]]
        suma += element[0] * vector_xp[element[1]]

    return suma

def calculate_sum(index_linie, vector_xp, linie_matrice):

    elemente_sub_index = [x for x in linie_matrice if x[1] < index_linie]
    vector_sub_index = [x for x in range(index_linie)]
    suma = 0
    for element in elemente_sub_index:
        suma += element[0] * vector_xp[element[1]]

    return suma

if __name__ == "__main__":

    try:
        pickle_matrice = open("m_rar_5.pkl","rb")
        pickle_vector = open("m_rar_5_vector.pkl","rb")

        matrice_1 = pickle.load(pickle_matrice)
        vector_1 = pickle.load(pickle_vector)
    except:
        (matrice_1, vector_1) = tema_3.create_matrix("m_rar_5.txt",True,True)
    numar_elemente = len(vector_1)

    xc = [0*numar_elemente for x in range(numar_elemente)]
    xp = [0*numar_elemente for x in range(numar_elemente)]
    k = 0
    delta_x = 10000
    kmax = 20

    for k in range(kmax):
        xp = xc.copy()

        for i in range(len(matrice_1)):
            if matrice_1[i][-1][0] == 0:
                print("Nu se poate calcula, avem element 0 pe linia {0} coloana {1} \n".format(i,matrice_1[i][-1][1]))
                print(matrice_1[i][-1][0],matrice_1[i][-1][1])
                break
            suma_1 = 0
            index_coloana_1 = 0
            coloana_diagonala_1 = matrice_1[i][-1][1]
            coloana_curenta_1 = matrice_1[i][index_coloana_1][1]

            while coloana_curenta_1 < coloana_diagonala_1-1:
                suma_1 += matrice_1[i][index_coloana_1][0]*xc[coloana_curenta_1]
                coloana_curenta_1 = matrice_1[i][index_coloana_1][1]
                index_coloana_1 += 1

            suma_2 = 0
            index_coloana_2 = len(matrice_1[i])-2
            coloana_diagonala_2 = matrice_1[i][-1][1]
            coloana_curenta_2 = matrice_1[i][index_coloana_2][1]

            while coloana_curenta_2 > coloana_diagonala_2-1 and index_coloana_2 > 0:
                suma_2 += matrice_1[i][index_coloana_2][0]*xc[coloana_curenta_2]
                coloana_curenta_2 = matrice_1[i][index_coloana_2][1]
                index_coloana_2 -= 1
            
           
            suma_finala = (vector_1[i]-suma_1-suma_2)/matrice_1[i][-1][0]
            #print(suma_1,suma_2,suma_finala)
            xc[i] = suma_finala
            diferenta = numpy.subtract(vector_1,xc)
            delta_x = numpy.linalg.norm(xc)

            print("numar_iterate {0} diferenta {1}".format(k,delta_x))
            if numpy.allclose(vector_1,xc,_EPSILON):
                print("allclose Numar iteratii "+str(k))
                break

            if delta_x < _EPSILON or delta_x > pow(10,8):
                print("delta exceeded Numar iterati : "+str(k))
                break
        #print(xc)
        #break
    if delta_x < _EPSILON:
        print("Convergenta")
        #print(xc)
    else:
        print("Divergenta")
        print(xc)
        norma = numpy.linalg.norm(xc)
        print(norma)