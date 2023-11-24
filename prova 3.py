import timeit
from random import choices, sample
from time import time

def gerador(tamanho):
    valores = range(1, 200000)
    print("Repetindo numero ? 1 - para sim e 2 - para nao")
    opcao=input()
    if opcao == 1:
        return  choices(valores, k=tamanho)
    elif opcao ==2:
        return sample(valores, tamanho)
    else:
        return sample(valores, tamanho)

def mergeSort(alist): #nlog(n)
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid] #DIVISAO
        righthalf = alist[mid:] #DIVISAO

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i] #"CONQUISTA"
                i=i+1
            else:
                alist[k]=righthalf[j] #"CONQUISTA"
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i] #"CONQUISTA"
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j] #"CONQUISTA"
            j=j+1
            k=k+1




def selectionSort(array):  #n^2
    size = len(array)
    for index in range(size-1):
        minIndex = array[index]
        for j in range(index+1,size):
            if array[j] < minIndex:
                swap = minIndex
                minIndex = array[j]
                array[j]=swap
        array[index]=minIndex




def fibonacci(index): # 2^n
    if index == 1 or index == 0:
        return index
    elif index==2:
        return 1
    else:
        return fibonacci(index-1)+fibonacci(index-2)

def fibonacciPGD(n, table = {}): # n
    table[0] = 0
    table[1] = 1
    for cont in range(2, n + 1):
        table[cont] = table[cont - 1] +  table[cont - 2] #MEMORIZAÇAO E CONSTRUÇÂO DA SOLUÇÂO UTILIZANDO OS SUBPROBLEMAS
    return table[n]


class Edge:
    def __init__(self,origin,destiny,pound):
        self.origin=origin
        self.destiny=destiny
        self.pound=pound

class Graph:
    def __init__(self,V,E):
        self.V=V
        self.E=E
class Sub:
    def __init__(self,father,classify):
        self.father=father
        self.classify=classify

def findMGT(Graph): # E * log(E) onde E é a quantidade de arestas.
    n= Graph.V
    edges= Graph.E

    mgt=[]
    sub=[]

    def find(sub,i):
        if sub[i].father != i:
            sub[i].father= find(sub,sub[i].father)
        return sub[i].father

    def union(sub, x, y):
        x= find(sub, x)
        y= find(sub, y)

        if sub[x].classify < sub[y].classify:
            sub[x].father = y
        elif sub[x].classify > sub[y].classify:
            sub[y].father = x
        else:
            sub[y].father = x
            sub[x].classify += 1

    edges.sort(key=lambda x: x.pound) # ORDENADO LOGO ESTAMOS OLHANDO PARA OS MENORES

    for i in range(n):
        sub.append(Sub(i,0))
    i=0

    while len(mgt)<n-1 and i<len(edges):
        edge = edges[i]

        origin = find(sub,edge.origin)
        destiny = find(sub,edge.destiny)

        if origin != destiny:
            mgt.append(edge)
            union(sub,origin,destiny)
        i += 1

    print("Arestas da Arvore Geradora Minima: ")
    for edge in mgt:
        print(f"{edge.origin} -- {edge.destiny} (peso {edge.pound})")






loop=True

while loop:
    print("1 para mergeSort - 2 para SelectionSort - 3 para fibonacci recursivo - 4 para fibonacci Programação Dinâmica - 5 para Kruskal - 6 para sair")
    opcao = int(input())

    if opcao ==1 :
        #lista = [54, 26, 93, 17, 77, 31, 44, 55, 20]
        print("Tamanho:")
        tamanho = int(input())
        lista=gerador(tamanho)
        print("ANTES:")
        print(lista)
        inicio = timeit.default_timer()
        mergeSort(lista)
        fim = timeit.default_timer()
        print("DEPOIS:")
        print(lista)
        print(f"Tempo : {fim-inicio}")
    elif opcao == 2:
        #lista2 = [54,26,93,17,77,31,44,55,20]
        print("Tamanho:")
        tamanho = int(input())
        lista2 = gerador(tamanho)
        print("ANTES:")
        print(lista2)
        inicio= timeit.default_timer()
        selectionSort(lista2)
        fim= timeit.default_timer()
        print("DEPOIS:")
        print(lista2)
        print(f"Tempo : {fim - inicio}")
    else:
        if opcao == 3:
            index=int(input("Digite index:"))
            resultado=fibonacci(index)
            print(resultado)
        elif opcao == 4:
            index = int(input("Digite index:"))
            resultado = fibonacciPGD(index)
            print(resultado)
        else:
            if opcao == 5:
                edges = [
                    Edge(0, 1, 5558),
                    Edge(0, 2, 3469),
                    Edge(0, 3, 214),
                    Edge(0, 4, 5075),
                    Edge(0, 5, 5959),
                    Edge(1, 2, 2090),
                    Edge(1, 3, 5725),
                    Edge(1, 4, 7753),
                    Edge(1, 5, 7035),
                    Edge(2, 3, 3636),
                    Edge(2, 4, 6844),
                    Edge(2, 5, 6757),
                    Edge(3, 4, 5120),
                    Edge(3, 5, 6053),
                    Edge(4, 5, 1307)
                ]

                graph = Graph(6, edges)
                findMGT(graph)
            else:
                print("Voce saiu :(")
                loop=False
