import random
import sys
import time

def gerar_grafo(arquivo: str, num_vertices: int, densidade: float = 0.01, ponderado: bool = True, direcionado: bool = False):
    """
    Gera um grafo aleatório grande e salva em arquivo no formato:
    v a d p
    origem destino [peso]
    """

    print(f"🧩 Gerando grafo com {num_vertices} vértices e densidade {densidade:.2%}...")

    inicio = time.time()
    arestas = set()
    total_arestas = int(num_vertices * (num_vertices - 1) * densidade)
    ponderado_flag = int(ponderado)
    direcionado_flag = int(direcionado)

    with open(arquivo, "w") as f:
        f.write(f"{num_vertices} {total_arestas} {direcionado_flag} {ponderado_flag}\n")

        while len(arestas) < total_arestas:
            origem = random.randint(0, num_vertices - 1)
            destino = random.randint(0, num_vertices - 1)
            if origem == destino:
                continue

            # Evita duplicatas em grafos não direcionados
            if not direcionado and (destino, origem) in arestas:
                continue

            if (origem, destino) in arestas:
                continue

            arestas.add((origem, destino))
            peso = random.randint(1, 100) if ponderado else 1
            f.write(f"{origem} {destino} {peso}\n")

            # Print progressivo a cada 1 milhão de arestas
            if len(arestas) % 1_000_000 == 0:
                print(f"   ➤ {len(arestas):,} arestas geradas...")

    fim = time.time()
    print(f"✅ Grafo '{arquivo}' gerado com sucesso.")
    print(f"   → {num_vertices:,} vértices")
    print(f"   → {len(arestas):,} arestas")
    print(f"   ⏱️ Tempo total: {fim - inicio:.2f}s\n")


if __name__ == "__main__":
    # Parâmetros padrão (pode ajustar conforme sua RAM)
    num_vertices = 20000     # 20 mil vértices
    densidade = 0.002        # 0.2% das possíveis conexões (≈ 4 milhões de arestas)
    arquivo_saida = "g_grande.txt"

    # Permite alterar via linha de comando: python GerarGrafo.py 10000 0.01
    if len(sys.argv) >= 2:
        num_vertices = int(sys.argv[1])
    if len(sys.argv) >= 3:
        densidade = float(sys.argv[2])
    if len(sys.argv) >= 4:
        arquivo_saida = sys.argv[3]

    gerar_grafo(arquivo_saida, num_vertices, densidade)
