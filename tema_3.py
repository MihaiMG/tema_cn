import time
import pickle
import sys

_EPSILON = pow(10,-1)

def inmulteste_vectori(lista1, lista2, vector_produs, numar_linie):

    for element1 in lista1:
        for element2 in lista2:
            produs_elemente = 0
            if element1[1] == element2[1]:
                produs_elemente = element1[0]*element2[0]
                element_adunat = False

                for element3 in vector_produs:
                    if element3[1] == element1[1]:
                        produs_elemente += element3[0]

                        index_to_replace = vector_produs.index(element3)
                        vector_produs[index_to_replace] = (produs_elemente, element3[1], numar_linie)
                        element_adunat = True
                if element_adunat is False:
                    vector_produs.append((produs_elemente, element1[1], numar_linie))
    return vector_produs


def aduna_liste_inmultire(numar_linie, lista1, lista2):

    suma = 0
    if len(lista2) > 0:
        for index in range(len(lista1)):
            element_produs = None

            if len(lista2) > 0:
                for aux_elem in lista2:
                    if aux_elem[0] == lista1[index][1]:
                        element_produs = aux_elem[1]
                        break
                if element_produs is not None:
                    suma += suma + (element_produs[0] * lista1[index][0])
    return (numar_linie,suma)


def get_elements_by_col(matrice,coloana):

    returned_list_by_column = []
    for linie in matrice:
        for element in linie:
            if element[1] == coloana:
                returned_list_by_column.append((linie.index(element), element))

    return returned_list_by_column


def inmulteste_matrici(matrice1, matrice2):

    # matrice_inmultita = [list() for x in range(len(matrice1))]
    matrice_inmultita = []
    for line in range(len(matrice1)):
        for coloana in range(len(matrice2)):
            suma = 0
            for element1 in matrice1[line]:
                k = element1[1]
                for element2 in matrice2[k]:
                    if element2[1] == coloana:
                        suma += element1[0]*element2[0]
            #print("linie : ",line)
            if suma != 0:
                matrice_inmultita.append((suma, line, coloana))


    return matrice_inmultita

def inmulteste_linie_vector(linie, vector):

    element_returnat = 0

    for index_linie in range(len(linie)):
        element = linie[index_linie]
        element_returnat += element[0]*vector[element[1]]
    return element_returnat


def produs_matrice_vector(matrice1, vector):

    vector_matrice_inmultit = []

    for linie in matrice1:

        produs_element = inmulteste_linie_vector(linie, vector)
        vector_matrice_inmultit.append(produs_element)

    return vector_matrice_inmultit


def aduna(l1, l2):

    diagonala = l1[-1][1]
    diagonala_inferioara_1 = [l1[index] for index in range(len(l1)-1) if l1[index][1] < diagonala]
    diagonala_inferioara_2 = [l2[index] for index in range(len(l2)-1) if l2[index][1] < diagonala]

    diagonala_superioara_1 = [l1[index] for index in range(len(l1)-1) if l1[index][1] > diagonala]
    diagonala_superioara_2 = [l2[index] for index in range(len(l2)-1) if l2[index][1] > diagonala]

    if len(diagonala_inferioara_1) > len(diagonala_inferioara_2):
        lista_inceput = diagonala_inferioara_1
        second_list = diagonala_inferioara_2
    else:
        lista_inceput = diagonala_inferioara_2
        second_list = diagonala_inferioara_1

    if len(diagonala_superioara_1) > len(diagonala_superioara_2):
        lista_inceput_superioara = diagonala_superioara_1
        second_list_superioara = diagonala_superioara_2
    else:
        lista_inceput_superioara = diagonala_superioara_2
        second_list_superioara = diagonala_superioara_1

    lista_adunare_inferioara = []
    elements_to_remove_inferioara = []
    lista_adunare_superioara = []
    elements_to_remove_superioara = []
    for x in lista_inceput:
        index = 0
        suma = 0
        for index in range(len(second_list)):
            if x[1] == second_list[index][1]:
                suma = x[0]+second_list[index][0]
                lista_adunare_inferioara.append((suma, x[1]))
                elements_to_remove_inferioara.append(second_list[index])
        if suma == 0:
            lista_adunare_inferioara.append(x)
    for x in lista_inceput_superioara:
        index = 0
        suma = 0
        for index in range(len(second_list_superioara)):
            if x[1] == second_list_superioara[index][1]:
                suma = x[0] + second_list_superioara[index][0]
                lista_adunare_superioara.append((suma, x[1]))
                lista_adunare_superioara.append(second_list_superioara[index])
        if suma == 0:
            lista_adunare_superioara.append(x)

    second_list = [x for x in second_list if x not in elements_to_remove_inferioara]
    second_list_superioara = [x for x in second_list if x not in elements_to_remove_superioara]

    #adaugam la vectore elementele din a doua lista care nu au fost adunate - sau nu se gaseau in primul vector
    lista_adunare_inferioara += second_list
    lista_adunare_superioara += second_list_superioara

    #sortam descrescator dupa valoare si adaugam elementele de pe diagonale

    lista_adunare_inferioara.sort(key=lambda x: x[1], reverse=True)
    lista_adunare_superioara.sort(key=lambda x: x[1], reverse=True)
    lista_adunare_inferioara += lista_adunare_superioara
    #print(lista_adunare_inferioara)
    lista_adunare_inferioara.append((l1[-1][0]+l2[-1][0],l1[-1][1]))

    return lista_adunare_inferioara


def inmulteste_vectori(vector_1, vector_2):

    vector_returnat = []
    for x in range(len(vector_1)):
        vector_returnat.append(vector_1[x] * vector_2[x])
    return vector_returnat


def aduna_vectori(vector_1, vector_2):

    vector_returnat = []
    for x in range(len(vector_1)):

        vector_returnat.append(vector_1[x]+vector_2[x])
    return vector_returnat


def aduna_matrici(matrice1, matrice2):

    matrice_aduna = []
    for x in range(len(matrice1)):
        lista_adunata = aduna(matrice1[x], matrice2[x])
        matrice_aduna.append(lista_adunata)
    return matrice_aduna


def aduna_vectori(l1,l2):

    lista_adunata = []
    for x in range(len(l1)):
        lista_adunata.append(l1[x]+l2[x])
    return lista_adunata


def add_element(matrice,element,linie_curenta,coloana_curenta):
    aux_elem = element
    aux_linie = linie_curenta
    aux_coloana = coloana_curenta

    linie_din_matrice = matrice[linie_curenta]
    index = matrice.index(linie_din_matrice)
    #elementul este sub diagonalei
    if coloana_curenta < linie_curenta:
        pivot_stanga = 0
        if linie_din_matrice[len(linie_din_matrice)-1][1] == linie_curenta:
            linie_din_matrice.insert(pivot_stanga, (element, coloana_curenta))
            return

        if len(linie_din_matrice) == 1 and linie_din_matrice[len(linie_din_matrice)-1][1] == linie_curenta:
            linie_din_matrice.insert(0, (element, coloana_curenta))
            return
        if len(linie_din_matrice) == 1 and linie_din_matrice[len(linie_din_matrice)-1][1] != linie_curenta:
            if coloana_curenta < linie_din_matrice[pivot_stanga][1]:
                linie_din_matrice.insert(1, (element, coloana_curenta))
                return
            else:
                linie_din_matrice.insert(0, (element, coloana_curenta))
                return

        while coloana_curenta < linie_din_matrice[pivot_stanga][1]:

            if linie_din_matrice[pivot_stanga][1] > linie_curenta:
                pivot_stanga -= 1
                linie_din_matrice.insert(pivot_stanga, (element, coloana_curenta))
                return
            pivot_stanga += 1
            if pivot_stanga == len(linie_din_matrice):
                linie_din_matrice.insert(pivot_stanga, (element, coloana_curenta))
                return

        linie_din_matrice.insert(pivot_stanga, (element, coloana_curenta))
        return

    #elementul este deasupra diagonalei
    elif coloana_curenta > linie_curenta:

        pivot_dreapta = 0
        ajuns_diagonala = False
        if linie_din_matrice[len(linie_din_matrice)-1][1] == linie_curenta:
            pivot_dreapta = len(linie_din_matrice)-2
        else:
            pivot_dreapta = len(linie_din_matrice)-1

        if pivot_dreapta < 0:
            linie_din_matrice.insert(0, (element, coloana_curenta))
            return

        while coloana_curenta > linie_din_matrice[pivot_dreapta][1]:

            if linie_din_matrice[pivot_dreapta][1] < linie_curenta:
                pivot_dreapta += 1
                linie_din_matrice.insert(pivot_dreapta, (element, coloana_curenta))
                return
            if pivot_dreapta < 0:
                pivot_dreapta = 0
                linie_din_matrice.insert(0, (element, coloana_curenta))
                return

            pivot_dreapta -= 1
        linie_din_matrice.insert(pivot_dreapta+1, (element, coloana_curenta))
        return

    #elementul este pe diagonala, il adaugam la sfarsitul vectorului
    else:
        linie_din_matrice.append((element, coloana_curenta))
        return


def create_matrix(fisier, serialize_matrix, serialize_vector):

    with open(fisier, "r") as fisier:
        numar_elemente = int(fisier.readline())
        fisier.readline()
        vector_b = []
        matrice = [list() for x in range(numar_elemente)]

        for index in range(numar_elemente):
            numar_citit = float(fisier.readline())
            vector_b.append(numar_citit)
        fisier.readline()

        while True:

            linie_citita = (fisier.readline()).rstrip("\n")
            if linie_citita == "":
                break
            linie_citita = linie_citita.split(",")
            element = float(linie_citita[0])
            index_linie = int(linie_citita[1])
            index_coloana = int(linie_citita[2])

            # try:
            linie_curenta = matrice[index_linie]
            if len(linie_curenta) > 0:
                add_element(matrice, element, index_linie, index_coloana)
            # except IndexError:
            else:
                linie_noua = list()
                linie_noua.append((element, index_coloana))
                matrice[index_linie] = linie_noua
            #print(index_linie)

    if serialize_matrix is True:
        output_matrix = open("matrice.pkl", "wb")
        pickle.dump(matrice, output_matrix, -1)

    if serialize_vector is True:
        output_vector = open("vector.pkl", "wb")
        pickle.dump(vector_b, output_vector, -1)
    return (matrice,vector_b)

def cauta_element(valoare,matrice):
    
    for linie in matrice:
        for element in linie:
            if abs(element[0]-valoare) < _EPSILON:
                return True
    return False

def verifica_element_vector(element,rezultat_a):

    for element_2 in rezultat_a:
        if abs(element_2-element) < _EPSILON:
            return True

    return False

def verifica_vectori_inmultiti(rezultat_produs,vector_a):

    numar_failuri = 0
    numar_ok = 0
    for element in rezultat_produs:
        gasit = False
        gasit = verifica_element_vector(element,vector_a)
        if gasit is True:
            numar_ok +=1
        else:
            numar_failuri += 1
            print("Nu am gasit elementul {0}".format(element))
    numar_total = numar_ok+numar_failuri
    print("Numar failuri : {0}, numar succes {1}".format(numar_failuri,numar_ok))
    print("Acuratete succes (vector) {0}".format((float(100 * numar_ok/numar_total))))

def verifica_calcul(matrice_a,matrce_b,fisier,adunare):
    #factor_aprox = epsilon
    matrice,vector = create_matrix(fisier,False,False)
    
    if adunare is True:
        matrice_adunata = aduna_matrici(matrice_a,matrice_b)
        numar_failuri  = 0
        numar_ok = 0
        for linie in matrice_adunata:
            for element in linie:
                gasit=cauta_element(element[0],matrice)
                if gasit is False:
                    #print("Nu am gasit elementul {0} linia {1} /n".format(element[0],matrice_adunata.index(linie)))
                    numar_failuri += 1
                else:
                    numar_ok += 1
        numar_total = numar_failuri + numar_ok
        print("Numar failuri : {0}, numar failuri {1}".format(numar_failuri,numar_ok))
        print("Acuratete succes {0}".format((float(100 * numar_ok/numar_total))))
    else:
        #matrice_adunata = inmulteste_matrici(matrice_a,matrice_b)
        try:
            pickled_file = open("aorib.pkl","rb")
            matrice_adunata = pickle.load(pickled_file)
        except e:
            print("File was not pickled")
            exit()


        numar_failuri  = 0
        numar_ok = 0
        for linie in matrice_adunata:
            for element in linie:
                gasit=cauta_element(element,matrice)
                if gasit is False:
                    #print("Nu am gasit elementul {0} linia {1}".format(element,matrice_adunata.index(linie)))
                    numar_failuri += 1
                    
                else:
                    numar_ok += 1
        numar_total = numar_failuri + numar_ok
        print("Numar failuri : {0}, numar succes {1}".format(numar_failuri,numar_ok))
        print("Acuratete succes {0}".format((float(100 * numar_ok/numar_total))))


if __name__=="__main__":

     
    matrice_a, vector_a = create_matrix("a.txt", True, True)
    #matrice_b, vector_b = create_matrix("b.txt", True, True)
    #matrice_adunata = aduna_matrici(matrice_a,matrice_b)
    
    vector_inmultire = [i for i in range(0,2018)]
    rezultat_produs = produs_matrice_vector(matrice_a,vector_inmultire)
    vector_1_sort = sorted(rezultat_produs,key= lambda x : x)
    vector_2_sort = sorted(vector_a,key= lambda x : x)
    for i in range(len(rezultat_produs)):
        print("Vector 1 {0}      -     Vector 2 {1}".format(vector_1_sort[i],vector_2_sort[i]))
    #print(rezultat_produs)
    #verifica_vectori_inmultiti(rezultat_produs,vector_a)
    #fisier_inmultire = open("aorib.pkl","r")

    #matrice_i = pickle.load(fisier_inmultire)
    #print(matrice_i)
    #matrice_inmultita = inmulteste_matrici(matrice_a,matrice_b)
    #output_matrice = open("aorib.pkl","wb")
    #pickle.dump(matrice_inmultita,output_matrice,-1)
    #verifica_calcul(matrice_a,matrice_b,"aplusb.txt",True)
    #verifica_calcul(matrice_a,matrice_b,"aorib.txt",False)
    # matrice_b, vector_b = create_matrix("b.txt")

    # vector_inmultit = produs_matrice_vector(matrice_a, vector_a)
    # vector_c = inmulteste_vectori(vector_a, vector_b)
    # vector_d = aduna_vectori(vector_a, vector_b)
    # pics =1
    # matrice_adunata = aduna_matrici(matrice_a, matrice_b)
    # matrice_inmultita = inmulteste_matrici(matrice_a, matrice_b)
