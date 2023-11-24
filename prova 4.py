import heapq





def changePriority(w,L,D):
    for i in range(len(D)):
        if D[i][1] == w:
            position = i
            break
    D[position] = (L[w],w)
    heapq._siftdown(D,0,position)
    return




def Dijkstra(n,m):
    price = []
    infinity = 999  # numero grande marcado como infinito
    n_out=[[] *n for i in range(n)]
    for i in range(n):
        linha = []
        for j in range(n):
            if i == j:
                linha.append(0)
            else:
                linha.append(infinity)
        price.append(linha)
    for j in range(m):
        a, b, c = input().split() # lendo arestas de a para b com custo c
        a = int(a)
        b = int(b)
        c = int(c)
        n_out[a].append(b) # b é vizinho de saida de a
        price[a][b]=c

    marked = n*[0] # todos os vertices desmarcados
    source = int(input("Digite a raiz: "))
    L=n*[infinity] # custos dos caminhos otimos
    L[source]=0 # caminho otimo para a raiz é 0
    D = [(0,source)] # prioridade e no
    for w in range(0,n):
        if w != source:
            heapq.heappush(D,(L[w],w))
    father = n*[-1]
    while D!= []:
        Lmin,v = heapq.heappop(D)
        marked[v]=1
        for w in n_out[v]:
            if marked[w] == 0:
                if L[v] + price[v][w]<L[w]: #Guloso, procurando o menor caminho de v para w
                    L[w]=L[v]+price[v][w] #atualiza o valor do caminho otimo de w
                    changePriority(w,L,D) #reposiciona a prioridade de w no heap
                    father[w]=v # muda o pai de w
    cont=0
    arrival =int(input("Qual a chegada? "))
    print(f"O caminho mais curto entre {source} e {arrival} é {L[arrival]}")
    print("")
    for i in range(n):
        print(f"Caminho minimo entre {source}--{i} = {L[i]}")
    print(" ")
    print(f"Arvore de caminhos minimos com a raiz {source}")
    print(father)





n,m=input().split()
n=int(n)
m=int(m)
Dijkstra(n,m)