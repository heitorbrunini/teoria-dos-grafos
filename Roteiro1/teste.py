from bibgrafo.grafo_lista_adjacencia import GrafoListaAdjacencia
from meu_grafo import *
g_p = MeuGrafo(['J','C','E','P','M','T','Z'])

g_p.adicionaAresta('a1','J','C')
g_p.adicionaAresta('a2','C','E')
g_p.adicionaAresta('a3','C','E')
g_p.adicionaAresta('a4','P','C')
g_p.adicionaAresta('a5','P','C')
g_p.adicionaAresta('a6','T','C')
g_p.adicionaAresta('a7','M','C')
g_p.adicionaAresta('a8','M','T')
g_p.adicionaAresta('a9','T','Z')

g= MeuGrafo(['J','C'])

g.adicionaAresta('a1','J','C')
g.adicionaAresta('a2','J','J')
g.adicionaAresta('a3','C','C')
g.adicionaAresta('a4','C','J')

g.vertices_nao_adjacentes()