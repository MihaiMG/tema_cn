import random

random_list = [random.randint(0,1000) for x in range(20)]

def binary_search(lista,element):

    low = 0
    high = len(lista)-1

    while low <= high:

        mid = int((low+high)/2)
        src = lista[mid]

        if src == element:
            print("Am gasit elementul {0} la indexul {1}".format(element,mid))
            return
        else:
            if element < src:
                high = mid - 1
            else:
                low = mid + 1
    print("Nu s-a gasit elementul")


def get_index(list_to_insert,element):

    if len(list_to_insert) == 0:
        list_to_insert.append(element)
    else:
        if len(list_to_insert) == 1:
            if element > list_to_insert[0]:
                list_to_insert.append(element)
            else:
                list_to_insert.insert(0,element)
        else:
            index_inceput = 0
            
            try :
                while element > list_to_insert[index_inceput] and index_inceput < len(list_to_insert) - 1:
                    index_inceput += 1
                list_to_insert.insert(index_inceput,element)
            except:
                print("Eroare la elementul {0} cu pozitia {1} cu vectorul {2} avand lungimea {3}".format(element,index_inceput,list_to_insert,len(list_to_insert)))


sorted_list = []
for element in random_list:
    get_index(sorted_list,element)
    #print("element {0} cu indexul : {1} -> vectorul {2}".format(element,random_list.index(element),sorted_list))
print(random_list[15])
print(sorted_list)
ele = random_list[15]
binary_search(sorted_list,ele)
