import time
import numpy as np

def gerar_combinacoes(n, ncor):
    combinacoes = []
    atual = [0] * n
    def backtrack(pos):
        if pos == n:
            combinacoes.append(atual[:])
            return
        for cor in range(ncor):
            atual[pos] = cor
            backtrack(pos + 1)
    backtrack(0)
    return combinacoes

def forca_bruta(grafo):
    teste = 0
    v = len(grafo.vertices)
    inicio = time.time()
    melhor = (v, list(range(v)))
    validas = []
    for i in range(2, v + 1):
        combinacoes = gerar_combinacoes(v, i)
        for cor in combinacoes:
            teste += 1
            valido = True
            for ver in range(v):
                for vizinho in grafo.retornarVizinhos(ver):
                    if cor[ver] == cor[vizinho]:
                        valido = False
                        break
                if not valido:
                    break
            if valido:
                validas.append((i, cor[:]))
                if i < melhor[0]:
                    melhor = (i, cor[:])
    print(f"\nTodas as combinações válidas:")
    print(validas)
    print(f"\nTotal de combinações possíveis: {len(validas)}")
    print(f"\nMelhor coloração encontrada usa {melhor[0]} cores: {melhor[1]}")
    return (melhor[0], melhor[1], time.time() - inicio)

def welsh_powell(grafo):
    inicio = time.time()
    v = len(grafo.vertices)
    grau = sorted([(i, len(grafo.retornarVizinhos(i))) for i in range(v)], key=lambda x: -x[1])
    cores = np.full(v, -1, dtype=int)
    cor_atual = 0

    for g in grau:
        vertice = g[0]
        if cores[vertice] == -1:
            cores[vertice] = cor_atual
            for gr in grau:
                vg = gr[0]
                if cores[vg] == -1:
                    viz = grafo.retornarVizinhos(vg)
                    if all(cores[viz[i]] != cor_atual for i in range(len(viz))):
                        cores[vg] = cor_atual
            cor_atual += 1
    return (cor_atual, cores.tolist(), time.time() - inicio)

def dsatur(grafo):
    inicio = time.time()
    v = len(grafo.vertices)
    cores = np.full(v, -1, dtype=int)
    saturacao = np.zeros(v, dtype=int)
    graus = np.array([len(grafo.retornarVizinhos(i)) for i in range(v)])

    for _ in range(v):
        candidatos = np.where(cores == -1)[0]
        escolhido = max(candidatos, key=lambda i: (saturacao[i], graus[i]))

        vizinhos = grafo.retornarVizinhos(escolhido)
        viz_cores = np.zeros(v, dtype=bool)
        for viz in vizinhos:
            if cores[viz] != -1:
                viz_cores[cores[viz]] = True

        cor = 0
        while cor < v and viz_cores[cor]:
            cor += 1
        cores[escolhido] = cor

        for viz in vizinhos:
            if cores[viz] == -1:
                vizinhos_viz = grafo.retornarVizinhos(viz)
                cores_usadas = set(cores[w] for w in vizinhos_viz if cores[w] != -1)
                saturacao[viz] = len(cores_usadas)

    return (cores.max() + 1, cores.tolist(), time.time() - inicio)

def lookahead(grafo):
    inicio = time.time()
    n = len(grafo.vertices)
    cores = np.full(n, -1, dtype=int)
    max_cores = n

    for v in range(n):
        viz = grafo.retornarVizinhos(v)
        usadas = np.zeros(max_cores, dtype=bool)
        for u in viz:
            if cores[u] != -1:
                usadas[cores[u]] = True

        melhor_cor = -1
        maior_liberdade = -1

        for cor in range(max_cores):
            if usadas[cor]:
                continue
            liberdade = 0
            for u in viz:
                if cores[u] == -1:
                    viz_u = grafo.retornarVizinhos(u)
                    bloqueadas = set(cores[w] for w in viz_u if cores[w] != -1 or w == v)
                    if cor not in bloqueadas:
                        liberdade += max_cores - len(bloqueadas)
            if liberdade > maior_liberdade:
                maior_liberdade = liberdade
                melhor_cor = cor

        if melhor_cor == -1:
            melhor_cor = np.where(~usadas)[0][0]

        cores[v] = melhor_cor

    return (cores.max() + 1, cores.tolist(), time.time() - inicio)
