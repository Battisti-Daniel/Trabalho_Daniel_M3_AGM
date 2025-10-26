import numpy as np
from Grafos import Grafos

def dfs(grafo: Grafos, start: int):
    visitados = np.zeros(len(grafo.vertices), dtype=bool)
    ordem_visita = []

    def visitar(v):
        visitados[v] = True
        ordem_visita.append(grafo.labelVertice(v))
        for vizinho in grafo.retornarVizinhos(v):
            if not visitados[vizinho]:
                visitar(vizinho)

    visitar(start)
    return ordem_visita
