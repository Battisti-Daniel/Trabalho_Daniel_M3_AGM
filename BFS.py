import numpy as np
from Grafos import Grafos

def bfs(grafo: Grafos, start: int):
    visitados = np.zeros(len(grafo.vertices), dtype=bool)
    fila = [start]
    visitados[start] = True
    ordem_visita = []

    while fila:
        atual = fila.pop(0)
        ordem_visita.append(grafo.labelVertice(atual))

        for vizinho in grafo.retornarVizinhos(atual):
            if not visitados[vizinho]:
                visitados[vizinho] = True
                fila.append(vizinho)

    return ordem_visita
