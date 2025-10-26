import numpy as np
from Grafos import Grafos

def dijkstra(grafo: Grafos, inicio: int):
    n = len(grafo.vertices)

    aberto = np.ones(n, dtype=bool)
    anterior = np.full(n, -1, dtype=int)
    distancia = np.full(n, np.inf)
    distancia[inicio] = 0

    while True:
        candidatos = np.where(aberto)[0]
        if len(candidatos) == 0:
            break
        atual = candidatos[np.argmin(distancia[candidatos])]
        
        if distancia[atual] == np.inf:
            break

        for vizinho in grafo.retornarVizinhos(atual):
            peso = grafo.pesoAresta(atual, vizinho)
            nova_dist = distancia[atual] + peso
            if nova_dist < distancia[vizinho]:
                distancia[vizinho] = nova_dist
                anterior[vizinho] = atual

        aberto[atual] = False

    print("Menores distâncias de", grafo.labelVertice(inicio))
    for destino in range(n):
        if distancia[destino] == np.inf:
            print(f"{grafo.labelVertice(inicio)} -> {grafo.labelVertice(destino)}: inatingível")
        else:
            caminho = []
            atual = destino
            while atual != -1:
                caminho.insert(0, grafo.labelVertice(atual))
                atual = anterior[atual]
            print(f"{grafo.labelVertice(inicio)} -> {grafo.labelVertice(destino)}: distância = {distancia[destino]}, caminho = {' -> '.join(caminho)}")
