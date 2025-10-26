from GrafosLista import GrafoLista
from GrafosMatriz import GrafoMatriz
from BFS import bfs
from DFS import dfs
from Dijkstra import dijkstra
from GrafoImage import grafoImage
from Coloracao import *
from FordFulkerson import FordFulkerson
import pandas as pd
from Prim import prim
from Kruskal import kruskal

def data(arquivo: str) -> []:
    with open(arquivo, 'r') as f:
        index = f.readlines()
    v, a, d, p = map(int, index[0].strip().split())
    grafoL = GrafoLista(direcionado=bool(d), ponderado=bool(p))
    grafoM = GrafoMatriz(direcionado=bool(d), ponderado=bool(p))
    for i in range(v):
        grafoL.inserirVertice(f"V{i}")
        grafoM.inserirVertice(f"V{i}")
    for i in index[1:]:
        partes = i.strip().split()
        origem = int(partes[0])
        destino = int(partes[1])
        peso = float(partes[2]) if p and len(partes) > 2 else 1.0
        grafoL.inserirAresta(origem, destino, peso)
        grafoM.inserirAresta(origem, destino, peso)
    return [grafoL, grafoM]


[grafoL, grafoM] = data("g3.txt")

n = len(grafoL.vertices)

matriz = np.zeros((n, n), dtype=np.float64)


for v in range(n):
    for viz in grafoL.retornarVizinhos(v):
        matriz[v][viz] = grafoL.pesoAresta(v, viz)

prim(grafoL, 0)
