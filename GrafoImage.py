import networkx as nx
import matplotlib.pyplot as plt

def grafoColorido(grafo, cores):
    G = nx.Graph()

    for i, label in enumerate(grafo.vertices):
        G.add_node(i, label=label)

    for origem in range(len(grafo.vertices)):
        for destino in grafo.retornarVizinhos(origem):
            if origem < destino:
                G.add_edge(origem, destino)

    pos = nx.spring_layout(G)
    labels = {i: grafo.labelVertice(i) for i in G.nodes()}
    nx.draw(
        G, pos, labels=labels, with_labels=True,
        node_color=[cores[i] for i in range(len(cores))],
        cmap=plt.cm.get_cmap('tab20'),
        node_size=500, font_size=10
    )
    plt.title("Coloração do Grafo")
    plt.show()

def grafoImage(grafo):
    G = nx.DiGraph() if grafo.direcionado else nx.Graph()

    for i, label in enumerate(grafo.vertices):
        G.add_node(i, label=label)

    for origem in range(len(grafo.vertices)):
        for aresta in grafo.retornarVizinhos(origem):
            destino = aresta if isinstance(aresta, int) else aresta.destino
            peso = grafo.pesoAresta(origem, destino)
            G.add_edge(origem, destino, weight=peso)

    pos = nx.spring_layout(G)
    labels = {i: grafo.labelVertice(i) for i in G.nodes()}
    edge_labels = nx.get_edge_attributes(G, 'weight')

    nx.draw(G, pos, labels=labels, with_labels=True, node_color='lightblue', node_size=300, font_size=5)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.show()
