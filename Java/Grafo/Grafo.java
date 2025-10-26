package Grafo;

import java.io.*;
import java.util.*;

public class Grafo {
    public int nVertices;
    public boolean direcionado;
    public boolean ponderado;
    public double[][] matriz;
    public List<String> vertices;

    public Grafo(boolean direcionado, boolean ponderado) {
        this.direcionado = direcionado;
        this.ponderado = ponderado;
        this.vertices = new ArrayList<>();
        this.matriz = new double[0][0];
    }

    private void expandirMatriz() {
        int n = vertices.size();
        double[][] nova = new double[n][n];
        for (int i = 0; i < matriz.length; i++) {
            System.arraycopy(matriz[i], 0, nova[i], 0, matriz[i].length);
        }
        matriz = nova;
    }

    public void inserirVertice(String label) {
        vertices.add(label);
        expandirMatriz();
    }

    public void inserirAresta(int origem, int destino, double peso) {
        if (origem >= vertices.size() || destino >= vertices.size()) return;
        matriz[origem][destino] = ponderado ? peso : 1;
        if (!direcionado)
            matriz[destino][origem] = ponderado ? peso : 1;
    }

    public List<Integer> retornarVizinhos(int v) {
        List<Integer> viz = new ArrayList<>();
        for (int i = 0; i < matriz[v].length; i++) {
            if (matriz[v][i] != 0)
                viz.add(i);
        }
        return viz;
    }

    public double pesoAresta(int origem, int destino) {
        return matriz[origem][destino];
    }

    public String labelVertice(int indice) {
        return vertices.get(indice);
    }

    public static Grafo carregarDeArquivo(String caminho) throws IOException {
        BufferedReader br = new BufferedReader(new FileReader(caminho));
        String[] cabecalho = br.readLine().trim().split(" ");
        int v = Integer.parseInt(cabecalho[0]);
        int a = Integer.parseInt(cabecalho[1]);
        boolean d = Integer.parseInt(cabecalho[2]) == 1;
        boolean p = Integer.parseInt(cabecalho[3]) == 1;

        Grafo g = new Grafo(d, p);
        for (int i = 0; i < v; i++) {
            g.inserirVertice("V" + i);
        }

        for (int i = 0; i < a; i++) {
            String[] linha = br.readLine().trim().split(" ");
            int origem = Integer.parseInt(linha[0]);
            int destino = Integer.parseInt(linha[1]);
            double peso = p ? Double.parseDouble(linha[2]) : 1.0;
            g.inserirAresta(origem, destino, peso);
        }
        br.close();
        return g;
    }
}
