import numpy as np
from Grafos import *

class GrafoLista(Grafos):
    class Aresta:
        def __init__(self, destino: int, peso: float):
            self.destino = destino
            self.peso = peso

    def __init__(self, direcionado: bool, ponderado: bool):
        super().__init__(direcionado, ponderado)
        self.lista_adj = []

    def inserirVertice(self, label: str) -> bool:
        if not super().inserirVertice(label):
            return False
        self.lista_adj.append(np.array([], dtype=object))
        return True

    def removerVertice(self, indice: int) -> bool:
        if not super().removerVertice(indice):
            return False
        self.lista_adj.pop(indice)
        for i in range(len(self.lista_adj)):
            nova_lista = []
            for aresta in self.lista_adj[i]:
                if aresta.destino != indice:
                    destino_corrigido = aresta.destino - 1 if aresta.destino > indice else aresta.destino
                    nova_lista.append(self.Aresta(destino_corrigido, aresta.peso))
            self.lista_adj[i] = np.array(nova_lista, dtype=object)
        return True

    def labelVertice(self, indice: int) -> str:
        return self.vertices[indice]

    def imprimeGrafo(self):
        for index, arestas in enumerate(self.lista_adj):
            conexoes = [(self.vertices[a.destino], a.peso) for a in arestas]
            print(f"{self.vertices[index]} -> {conexoes}")

    def inserirAresta(self, origem: int, destino: int, peso=1.0) -> bool:
        if origem >= len(self.vertices) or destino >= len(self.vertices):
            return False
        peso_real = peso if self.ponderado else 1.0
        self.lista_adj[origem] = np.append(self.lista_adj[origem], self.Aresta(destino, peso_real))
        if not self.direcionado:
            self.lista_adj[destino] = np.append(self.lista_adj[destino], self.Aresta(origem, peso_real))
        return True

    def removerAresta(self, origem: int, destino: int) -> bool:
        if origem >= len(self.vertices) or destino >= len(self.vertices):
            return False
        self.lista_adj[origem] = np.array([a for a in self.lista_adj[origem] if a.destino != destino], dtype=object)
        if not self.direcionado:
            self.lista_adj[destino] = np.array([a for a in self.lista_adj[destino] if a.destino != origem], dtype=object)
        return True

    def existeAresta(self, origem: int, destino: int) -> bool:
        return any(a.destino == destino for a in self.lista_adj[origem])

    def pesoAresta(self, origem: int, destino: int) -> float:
        for a in self.lista_adj[origem]:
            if a.destino == destino:
                return a.peso
        return float('inf')

    def retornarVizinhos(self, vertice: int) -> list:
        return [a.destino for a in self.lista_adj[vertice]]
