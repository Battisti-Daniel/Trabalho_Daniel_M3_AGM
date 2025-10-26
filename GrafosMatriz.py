import numpy as np
from Grafos import *

class GrafoMatriz(Grafos):
    def __init__(self, direcionado: bool, ponderado: bool):
        super().__init__(direcionado, ponderado)
        self.matriz = np.zeros((0, 0))  # Matriz de adjacência inicial

    def inserirVertice(self, label: str) -> bool:
        if not super().inserirVertice(label):
            return False
        tamanho = len(self.vertices)
        nova_matriz = np.zeros((tamanho, tamanho))
        nova_matriz[:self.matriz.shape[0], :self.matriz.shape[1]] = self.matriz
        self.matriz = nova_matriz
        return True

    def removerVertice(self, indice: int) -> bool:
        if not super().removerVertice(indice):
            return False
        self.matriz = np.delete(self.matriz, indice, axis=0)  # Remove linha
        self.matriz = np.delete(self.matriz, indice, axis=1)  # Remove coluna
        return True

    def labelVertice(self, indice: int) -> str:
        return self.vertices[indice]

    def imprimeGrafo(self):
        print("   ", *self.vertices)
        for i, linha in enumerate(self.matriz):
            print(self.vertices[i], linha.tolist())

    def inserirAresta(self, origem: int, destino: int, peso=1.0) -> bool:
        if origem >= len(self.vertices) or destino >= len(self.vertices):
            return False
        valor = peso if self.ponderado else 1
        self.matriz[origem][destino] = valor
        if not self.direcionado:
            self.matriz[destino][origem] = valor
        return True

    def removerAresta(self, origem: int, destino: int) -> bool:
        if origem >= len(self.vertices) or destino >= len(self.vertices):
            return False
        self.matriz[origem][destino] = 0
        if not self.direcionado:
            self.matriz[destino][origem] = 0
        return True

    def existeAresta(self, origem: int, destino: int) -> bool:
        return self.matriz[origem][destino] != 0

    def pesoAresta(self, origem: int, destino: int) -> float:
        return self.matriz[origem][destino]

    def retornarVizinhos(self, vertice: int) -> list:
        return list(np.where(self.matriz[vertice] != 0)[0])
