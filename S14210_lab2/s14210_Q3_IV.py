'''
Program to count only the neighbours with more than 0.7 combined score for the
DREB1A protein.
Input : Protein interaction data in tabular format
Output : The count of the neighbours with more than 0.7 combined score for the
DREB1A protein.
'''

import networkx as nx
p_network = nx.Graph()
with open("string_interactions_short.tsv", "r") as string:
    for line in string:
        if '#' not in line:
            line = line.strip()
            line = (line.split('\t'))
            if (line[0]=="ERF24") | (line[1]=="ERF24") and float(line[12])>0.7:
                p_network.add_edge(line[0],line[1], weight=float(line[12]))


print("Neighbours with more than 0.7 combined score for the DREB1A protein : ",(len(p_network.nodes)-1))

nx.write_gml(p_network,'dreb1a_interactions_Q3_IV.gml')