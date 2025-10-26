package Grafo;

import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        if (args.length < 1) {
            System.out.println("Uso: java Main <arquivo.txt>");
            return;
        }

        String caminho = args[0];
        System.out.println("Carregando grafo de " + caminho);
        Grafo g = Grafo.carregarDeArquivo(caminho);

        int n = g.vertices.size();
        System.out.printf("Grafo com %d vértices.\n", n);

        // Força o uso de memória
        System.out.printf("Criando matriz densa %d x %d...\n", n, n);
        double[][] matriz = new double[n][n];
        for (int i = 0; i < n; i++) {
            for (int j : g.retornarVizinhos(i)) {
                matriz[i][j] = g.pesoAresta(i, j);
            }
        }

        System.out.println("Executando Prim...");
        Prim.executar(g, 0);
    }
}
