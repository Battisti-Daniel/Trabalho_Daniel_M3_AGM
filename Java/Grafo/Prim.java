package Grafo;

import java.util.*;

public class Prim {
    public static void executar(Grafo g, int verticeInicial) {
        long inicio = System.nanoTime();

        int n = g.vertices.size();
        boolean[] visitado = new boolean[n];
        List<int[]> arvore = new ArrayList<>();

        visitado[verticeInicial] = true;

        while (true) {
            double menor = Double.POSITIVE_INFINITY;
            int origem = -1;
            int destino = -1;

            for (int i = 0; i < n; i++) {
                if (visitado[i]) {
                    for (int j : g.retornarVizinhos(i)) {
                        if (!visitado[j]) {
                            double peso = g.pesoAresta(i, j);
                            if (peso < menor) {
                                menor = peso;
                                origem = i;
                                destino = j;
                            }
                        }
                    }
                }
            }

            if (origem == -1) break;

            arvore.add(new int[]{origem, destino});
            visitado[destino] = true;
        }

        long fim = System.nanoTime();
        double tempo = (fim - inicio) / 1e9;

        System.out.println("AGM (Prim):");
        for (int[] e : arvore) {
            System.out.printf("%s - %s (%.2f)\n",
                g.labelVertice(e[0]), g.labelVertice(e[1]),
                g.pesoAresta(e[0], e[1]));
        }
        System.out.printf("Tempo de execução: %.6f segundos\n", tempo);
    }
}
