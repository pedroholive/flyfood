# 🚁 FlyFood

Solução desenvolvida para o projeto FlyFood da disciplina de Projeto Interdisciplinar II — UFRPE.

O algoritmo determina a rota de menor custo para um drone sair de um ponto de origem **R**, visitar todos os pontos de entrega exatamente uma vez e retornar à base, utilizando **força bruta com permutações** e **Distância de Manhattan** como métrica de custo.

---

## 📋 Descrição do Problema

Dado um mapa representado por uma matriz n×m, onde cada célula contém `0` (vazia) ou o identificador de um ponto relevante, o algoritmo encontra a permutação de menor custo entre todos os pontos de entrega, garantindo a rota ótima para o drone.

---

## ⚙️ Como executar

**Pré-requisitos:** Python 3.x instalado.

1. Clone o repositório
```bash
git clone https://github.com/pedroholive/flyfood.git
```
2. Coloque o arquivo de matriz na pasta do projeto
3. Execute o algoritmo
```bash
python flyfoodteste.py
```

---

## 📂 Formato do arquivo de entrada

4 5
0 R 0 0 0
0 0 0 A 0
0 B 0 0 0
0 0 0 0 C

- Primeira linha: dimensões da matriz (linhas e colunas)
- `R` — ponto de origem e retorno do drone
- Letras — pontos de entrega
- `0` — células vazias

---

## 📊 Resultados obtidos

| Cidades | Tempo de execução |
|---|---|
| 4 | < 0,001 segundos |
| 7 | < 0,02 segundos |
| 9 | 0,28 segundos |
| 10 | 2,78 segundos |
| 11 | 28 segundos |
| 12 | 9,35 minutos |
| 13 | 106 minutos |

---

## 🛠️ Tecnologias utilizadas

- Python 3
- Biblioteca `itertools` (permutações)

