import time
import numpy as np
from Grafos import Grafos

def prim(grafo: Grafos, vertice = 0):
    tempo_inicio = time.time()

    S = []
    Q = list(range(len(grafo.vertices)))
    visitado = np.zeros(len(grafo.vertices), dtype=bool)

    u = vertice
    visitado[u] = True
    Q.remove(u)

    while Q:
        menor = float('inf')
        aresta = (-1, -1)
        for i in range(len(grafo.vertices)):
            if visitado[i]:
                for j in grafo.retornarVizinhos(i):
                    if not visitado[j]:
                        peso = grafo.pesoAresta(i, j)
                        if peso < menor:
                            menor = peso
                            aresta = (i, j)

        if aresta != (-1, -1):
            S.append((aresta[0], aresta[1], menor))
            visitado[aresta[1]] = True
            Q.remove(aresta[1])

    tempo_fim = time.time()

    custo_total = sum([p for _, _, p in S])
    print("AGM:")
    for u, v, p in S:
        print(f"{grafo.labelVertice(u)} - {grafo.labelVertice(v)}: {float(p)}")
    print(f"Custo total: {custo_total}")
    print("Tempo de execução: %.6f segundos\n" % (tempo_fim - tempo_inicio))
