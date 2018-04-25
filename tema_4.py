import tema_3
import pickle
import sys

_EPSILON = sys.float_info.epsilon


def calculate_sum_2(index_linie, vector_xp, linie_matrice):

def calculate_sum(index_linie, vector_xp, linie_matrice):

    elemente_sub_index = [x for x in linie_matrice if x[1] < index_linie]
    vector_sub_index = [x for x in range(index_linie)]
    suma = 0
    for element in elemente_sub_index:
        suma += element[0] * vector_sub_index[element[1]]

    return suma

if __name__ == "__main__":

    try:
        pickle_matrice = open("matrice.pkl","rb")
        pickle_vector = open("vector.pkl","rb")

        matrice = pickle.load(pickle_matrice)
        vector = pickle.load(pickle_vector)
    except:
        (matrice_1, vector_1) = tema_3.create_matrix("m_rar_1.txt",True,True)
    numar_elemente = len(vector)

    xc = [0*numar_elemente for x in range(numar_elemente)]
    xp = [0*numar_elemente for x in ramge(numar_elemente)]
    k = 0
    delta_x = 10000
    kmax = 10000

    while (delta_x >= _EPSILON) and (kmax > k) and (delta_x <= pow(10, 8)):

        xp = xc.copy()

        for i in range(numar_elemente):
            if matrice[-1][0] < _EPSILON:
                print("Nu se poate calcula, avem element pe diagonala {0} 0 \n".format(i))
                break
            suma_1 = calculate_sum(i, xp, matrice[i])
            suma_2 = calculate_sum_2(i, xp, matrice[i])
            print(suma_1)

        k += 1

    print(_EPSILON)
