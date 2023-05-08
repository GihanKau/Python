'''
Program to calculate the degree of the rice DREB1A protein
Input : Protein Interaction data in tabular format (.tcv file)
Output : Degree of the protein and protein network graph
'''
import networkx as nx
p_network = nx.Graph()
with open("string_interactions_short.tsv", "r") as string:
    for line in string:
        if '#' not in line:
            line = line.strip()
            line = (line.split('\t'))
            p_network.add_edge(line[0],line[1], weight=float(line[12]))


print("degree of DREB1A Protein : ",(len(p_network.nodes)-1))

nx.write_gml(p_network,'dreb1a_interactions_Q3_III.gml')

