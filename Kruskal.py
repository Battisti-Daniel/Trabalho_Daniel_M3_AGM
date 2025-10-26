import time
from Grafos import Grafos

def kruskal(grafo: Grafos):
    tempo_inicio = time.time()

    S = []
    Q = []
    n = len(grafo.vertices)

    F = [{i} for i in range(n)]

    for u in range(n):
        for v in grafo.retornarVizinhos(u):
            if u < v:
                Q.append((grafo.pesoAresta(u, v), u, v))

    Q.sort()

    for peso, u, v in Q:
        arvoU = arvoT = -1
        for i in range(len(F)):
            if u in F[i]:
                arvoU = i
            if v in F[i]:
                arvoT = i

        if arvoU != arvoT:
            S.append((u, v, peso))
            F[arvoU] = F[arvoU].union(F[arvoT])
            F.pop(arvoT)

    tempo_fim = time.time()

    custo_total = sum([p for _, _, p in S])
    print("AGM:")
    for u, v, p in S:
        print(f"{grafo.labelVertice(u)} - {grafo.labelVertice(v)}: {float(p)}")
    print(f"Custo total: {custo_total}")
    print("Tempo de execução: %.6f segundos\n" % (tempo_fim - tempo_inicio))
