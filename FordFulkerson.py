import numpy as np
import copy

class FordFulkerson:
    def __init__(self, grafo):
        self.grafo_original = grafo

    def find_my_p(self, grafo, origem, destino):
        visitados = [False] * len(grafo.vertices)
        caminho = []
    
        def dfs(u):
            if u == destino:
                return True
            visitados[u] = True
    
            if hasattr(grafo, "lista_adj"):
                arestas = grafo.lista_adj[u]
                for aresta in arestas:
                    v = aresta.destino
                    if not visitados[v] and aresta.peso > 0:
                        caminho.append((u, v))
                        if dfs(v):
                            return True
                        caminho.pop()
            else:
                for v in grafo.retornarVizinhos(u):
                    if not visitados[v] and grafo.pesoAresta(u, v) > 0:
                        caminho.append((u, v))
                        if dfs(v):
                            return True
                        caminho.pop()
            return False
    
        if dfs(origem):
            return caminho
        return None

    def calcular_fluxo_maximo(self, origem, destino):
        grafo_novo = copy.deepcopy(self.grafo_original)
        fluxo_maximo = 0
        iteracao = 1
    
        while True:
            caminho = self.find_my_p(grafo_novo, origem, destino)
            if not caminho:
                break
    
            capacidade_min = min(grafo_novo.pesoAresta(u, v) for u, v in caminho)
            print(f"\n[Iteração {iteracao}] Capacidade mínima: {capacidade_min}")
            for u, v in caminho:
                print(f"{(u)} → {(v)}")
    
            for u, v in caminho:
                if hasattr(grafo_novo, "lista_adj"):
                    for aresta in grafo_novo.lista_adj[u]:
                        if aresta.destino == v:
                            aresta.peso -= capacidade_min
                    for aresta in grafo_novo.lista_adj[v]:
                        if aresta.destino == u:
                            aresta.peso += capacidade_min
                else:
                    grafo_novo.matriz[u][v] -= capacidade_min
                    grafo_novo.matriz[v][u] += capacidade_min
    
            fluxo_maximo += capacidade_min
            print(f"Fluxo: {fluxo_maximo}")
    
            if hasattr(grafo_novo, "lista_adj"):
                for u in range(len(grafo_novo.vertices)):
                    for aresta in grafo_novo.lista_adj[u]:
                        pass
            else:
                for u in range(len(grafo_novo.vertices)):
                    for v in range(len(grafo_novo.vertices)):
                        if grafo_novo.matriz[u][v] != 0:
                            pass

    
            iteracao += 1
    
        print(f"Fluxo máximo: {fluxo_maximo}\n")
        return fluxo_maximo


    def inverter_aresta(self, grafo, u, v):
        peso = grafo.pesoAresta(u, v)
        grafo.removerAresta(u, v)
        grafo.removerAresta(v, u)
        grafo.inserirAresta(v, u, peso)



    def busca_local(self, origem, destino):
        melhor_fluxo = self.calcular_fluxo_maximo(origem, destino)
        melhor_grafo = copy.deepcopy(self.grafo_original)
        passos = 0
    
        for u in range(len(self.grafo_original.vertices)):
            if hasattr(self.grafo_original, "lista_adj"):
                vizinhos = [aresta.destino for aresta in self.grafo_original.lista_adj[u]]
            else:
                vizinhos = self.grafo_original.retornarVizinhos(u)
    
            for v in vizinhos:
                if not self.grafo_original.existeAresta(v, u):
                    grafo_testado = copy.deepcopy(self.grafo_original)
                    self.inverter_aresta(grafo_testado, u, v)
                    solver_teste = FordFulkerson(grafo_testado)
                    fluxo_teste = solver_teste.calcular_fluxo_maximo(origem, destino)
                    passos += 1
                    if fluxo_teste > melhor_fluxo:
                        print(f"Trocou aresta ({u}, {v}) por ({v}, {u}) -> Novo fluxo: {fluxo_teste}")
                        melhor_fluxo = fluxo_teste
                        melhor_grafo = grafo_testado

        return melhor_fluxo, passos, melhor_grafo
