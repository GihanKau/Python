'''
Author  : B.M.G.G.K. Ralapaksha
Date    : 19/11/21
Topic   : Majority voting algorithm to predict protein candidates on a protein network.
Input   : 1. A list of known proteins annotated to the particular function as a text file
          2. Protein interaction data for "DREB1A" as aTSV file
Output  : A list of unknown proteins with the predicted majority voting score
'''

# import libraries
import networkx as nx
from collections import OrderedDict

# take known proteins into a list
known_prot_list = []
with open("AT_stress_proteins.txt", "r") as known_file:
    for line in known_file:
        line = line.strip()
        line = line.split("\t")
        known_prot_list.append(line[1].upper())

p_network = nx.Graph()
# initiate the majority voting score counting dict.
m_vote_count_dict = {}
with open("string_interactions.tsv", "r") as str_file:
    unknown_p_count = 0
    for line in str_file:
        if "#" not in line:
            line = line.strip()
            line = line.split("\t")
            string_node1 = line[0].upper()
            string_node2 = line[1].upper()
            # Select unknown protein nodes which have connected to the known proteins
            if string_node1 not in known_prot_list and string_node2 in known_prot_list:

                if string_node1 in m_vote_count_dict:
                    m_vote_count_dict[string_node1] += 1
                else:
                    m_vote_count_dict[string_node1] = 1

            # Create a PPI network for DREB2A
            if string_node1 == "DREB2A":
                p_network.add_edge(string_node1, string_node2, weight=float(line[12]))
                # Count unknown proteins in the DREB2A PPI Network
                if string_node2 not in known_prot_list:
                    unknown_p_count += 1


print("Degree of the ATDREB2A protein in the network for stress tolerance : ", len(p_network.edges))
print("Number of unknown proteins in the network for stress tolerance : ", unknown_p_count)

# Sort the dictionary into descending order based on the value
sorted_dict = OrderedDict(sorted(m_vote_count_dict.items(), key=lambda x: x[1], reverse=True))

# Write the sorted dict into a new file
with open("Majority_voting.txt", "w") as file:
    file.write("Protein\t Majority voting score\n")
    for key, value in sorted_dict.items():
        file.write(key+"\t"+str(value)+"\n")

print("Unknown protein with highest majority voting score : ", sorted_dict.popitem(last=False))

# END
