import numpy as np
from abc import ABC, abstractmethod

class Grafos(ABC):

    def __init__(self, direcionado: bool, ponderado: bool):
        self.direcionado = direcionado
        self.ponderado = ponderado
        self.vertices = []
        self.matriz = np.zeros((0, 0))

    def _expandir_matriz(self):
        tamanho = len(self.vertices)
        nova_matriz = np.zeros((tamanho, tamanho))
        nova_matriz[:self.matriz.shape[0], :self.matriz.shape[1]] = self.matriz
        self.matriz = nova_matriz

    def inserirVertice(self, label: str) -> bool:
        if label in self.vertices:
            return False
        self.vertices.append(label)
        self._expandir_matriz()
        return True

    def removerVertice(self, indice: int) -> bool:
        if indice < 0 or indice >= len(self.vertices):
            return False
        self.vertices.pop(indice)
        self.matriz = np.delete(self.matriz, indice, axis=0)
        self.matriz = np.delete(self.matriz, indice, axis=1)
        return True

    def labelVertice(self, indice: int) -> str:
        if 0 <= indice < len(self.vertices):
            return self.vertices[indice]
        return ""

    def imprimeGrafo(self):
        print("   ", *self.vertices)
        for i, linha in enumerate(self.matriz):
            print(self.vertices[i], linha)

    def inserirAresta(self, origem: int, destino: int, peso=1.0) -> bool:
        if origem >= len(self.vertices) or destino >= len(self.vertices):
            return False
        self.matriz[origem, destino] = peso if self.ponderado else 1
        if not self.direcionado:
            self.matriz[destino, origem] = peso if self.ponderado else 1
        return True

    def removerAresta(self, origem: int, destino: int) -> bool:
        if origem >= len(self.vertices) or destino >= len(self.vertices):
            return False
        self.matriz[origem, destino] = 0
        if not self.direcionado:
            self.matriz[destino, origem] = 0
        return True

    def existeAresta(self, origem: int, destino: int) -> bool:
        return self.matriz[origem, destino] != 0

    def pesoAresta(self, origem: int, destino: int) -> float:
        return self.matriz[origem, destino]

    def retornarVizinhos(self, vertice: int) -> list:
        return [i for i, peso in enumerate(self.matriz[vertice]) if peso != 0]
