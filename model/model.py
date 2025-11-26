from database.dao import DAO
import networkx as nx

class Model:
    def __init__(self):
        self._nodes = None
        self._edges = None
        self.G = nx.Graph()

    def costruisci_grafo(self, threshold):
        """
        Costruisce il grafo (self.G) inserendo tutti gli Hub (i nodi) presenti e filtrando le Tratte con
          """
        lista_hub = DAO.readAllHub()
        self._nodes = {}
        for hub in lista_hub:
            self._nodes[hub.id] = hub
        for hub in self._nodes:
            self.G.add_node(hub)


        self._edges = DAO.readAlldaotratte(threshold)
        for tratta in self._edges:
            self.G.add_edge(tratta.partenza, tratta.arrivo)
            # associo ai id dei hubs nome e stato
            tratta.partenza = f'{self._nodes[tratta.partenza].nome}({self._nodes[tratta.partenza].stato})'
            tratta.arrivo = f'{self._nodes[tratta.arrivo].nome}({self._nodes[tratta.arrivo].stato})'



    def get_num_edges(self):
        """
        Restituisce il numero di Tratte (edges) del grafo
        :return: numero di edges del grafo
        """
        return len(self.G.edges())

    def get_num_nodes(self):
        """
        Restituisce il numero di Hub (nodi) del grafo
        :return: numero di nodi del grafo
        """
        return len(self.G.nodes())

    def get_all_edges(self):
        """
        Restituisce tutte le Tratte (gli edges) con i corrispondenti pesi
        :return: gli edges del grafo con gli attributi (il weight)
        """



