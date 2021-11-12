from bibgrafo.grafo_lista_adjacencia import GrafoListaAdjacencia
from bibgrafo.grafo_exceptions import *


class MeuGrafo(GrafoListaAdjacencia):
    def inverter(txt):
        #inverte um texto
            return txt[::-1]

    def vertices_nao_adjacentes(self):
        '''
        Provê uma lista de vértices não adjacentes no grafo. A lista terá o seguinte formato: [X-Z, X-W, ...]
        Onde X, Z e W são vértices no grafo que não tem uma aresta entre eles.
        :return: Uma lista com os pares de vértices não adjacentes
        '''
        lista = []
        aresta = ""
        for a in self.A:
            aresta = self.A[a].getV1()+a+self.A[a].getV2()
            lista.append(aresta)
        print (lista)
        print (self.A[0])

    def ha_laco(self):
        '''
        Verifica se existe algum laço no grafo.
        :return: Um valor booleano que indica se existe algum laço.
        '''
        #vertice self.A[a].getV1()
        for a in self.A:
            if self.A[a].getV1() == self.A[a].getV1():
                return True
        return False

    def grau(self, V=''):
        '''
        Provê o grau do vértice passado como parâmetro
        :param V: O rótulo do vértice a ser analisado
        :return: Um valor inteiro que indica o grau do vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        grau = 0 
        for a in self.A:
            if self.A[a].getV1() == V or self.A[a].getV2() == V :
                if self.A[a].getV1() != self.A[a].getV2():
                    grau+=1
                else:
                    grau+=2
        return grau

    def ha_paralelas(self):
        '''
        Verifica se há arestas paralelas no grafo
        :return: Um valor booleano que indica se existem arestas paralelas no grafo.
        '''
        
        lista = []
        aresta = ""
        for a in self.A:
            aresta = self.A[a].getV1()+self.A[a].getV2()
            lista.append(aresta)
        for aresta in lista:
            for paralelo in lista:
                paralelo = self.inverter(paralelo)
                if aresta == paralelo and aresta[0]!=aresta[1]:
                    return True
        return False
        
            

    def arestas_sobre_vertice(self, V):
        '''
        Provê uma lista que contém os rótulos das arestas que incidem sobre o vértice passado como parâmetro
        :param V: O vértice a ser analisado
        :return: Uma lista os rótulos das arestas que incidem sobre o vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        pass

    def eh_completo(self):
        '''
        Verifica se o grafo é completo.
        :return: Um valor booleano que indica se o grafo é completo
        '''
        pass
    

