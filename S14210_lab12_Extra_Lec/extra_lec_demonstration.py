import seaborn as sns
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd

class Network:

    def __init__(self, string_file):
        self.string_file = string_file
        self.p_network = self.create_net()
        self.no_prot = self.prot_counts()
        self.no_inter = self.prot_counts()
        self.network_diameter = self.net_d()

   # Create the network

    def create_net(self):

        p_network = nx.Graph()
        file = self.string_file
        with open(file, "r") as string:
            for line in string:
                if '#' not in line:
                    line = line.strip()
                    line = (line.split('\t'))
                    p_network.add_edge(line[0], line[1], weight=float(line[12]))

        self.p_network = p_network

        return p_network

    # Method to draw a network graph
    def network_graph(self):

        # Draw the graph
        nx.draw(self.p_network, with_labels=True,
                                node_size=200,
                                node_color='green',
                                font_size=9,
                                width=0.2,
                                label='PPI Network')

        plt.show()
        # Create a gml file for cytoscape
        nx.write_gml(self.p_network, 'dreb1a_interactions_Q3_IV.gml')-----