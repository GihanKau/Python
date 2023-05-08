

        # Method to count nodes and edges

    def prot_counts(self):

        p_network = self.p_network
        no_prot = p_network.number_of_nodes()
        no_inter = p_network.number_of_edges()

        self.no_prot = no_prot
        self.no_inter = no_inter
        return no_inter

    def prot_degree(self, prot_name):
        p_network = self.p_network
        return p_network.degree[prot_name]

    def plot_degree_dist(self):
        p_network = self.p_network

        degrees = [p_network.degree(n) for n in p_network.nodes()]

        sns.histplot(degrees, stat='count', binwidth=10)
        plt.xlabel('Degree')
        plt.title('Degree count vs Degree number')
        plt.show()

    def shortest_path(self, prot_1, prot_2):
        p_network = self.p_network
        return nx.shortest_path(p_network, source=prot_1, target=prot_2)

    def net_d(self): #error
        p_network = self.p_network

        ecc = nx.eccentricity(p_network)

        self.network_diameter = nx.diameter(p_network, ecc)

        return nx.diameter(p_network)

    def cluster_co(self, prot):
        p_network = self.p_network
        cluster_co = round(nx.clustering(p_network, prot), 4)
        return cluster_co

    def betw_cent(self,prot):
        p_network = self.p_network
        betw_cent = nx.betweenness_centrality(p_network)[prot]
        return betw_cent

    def betw_cent_hist(self):
        p_network = self.p_network
        betw_cents = nx.betweenness_centrality(p_network)
        #print(nx.betweenness_centrality(p_network))  # not sure

        cents = [betw_cents[n] for n in betw_cents.keys()]


        sns.histplot(cents, stat='count', bins=50)
        plt.xlabel('Betweenness Centralities')
        plt.title('The histogram of Betweenness Centralities')
        plt.xlim(0, 1)
        plt.show()

        return betw_cents

    @staticmethod
    def compare_2(file1, file2):

        pn1 = Network(file1)
        pn2 = Network(file2)

        # Average clustering bar chart
        net1_avg_clust = round(sum(nx.clustering(pn1.p_network).values()) / len(nx.clustering(pn1.p_network).values()), 3)
        net2_avg_clust = round(sum(nx.clustering(pn2.p_network).values()) / len(nx.clustering(pn2.p_network).values()), 3)

        net1_diam = pn1.network_diameter
        net2_diam = pn2.network_diameter

        data = {'Network': ['Network 1', 'Network 2'],
                'AVG Clust': [net1_avg_clust, net2_avg_clust],
                'Network d': [net1_diam, net2_diam]}

        df = pd.DataFrame(data, columns=['Network', 'AVG Clust', 'Network d'])

        fig, axis = plt.subplots(2, 2,)
        fig.suptitle('Comparison of the two PPI networks', fontsize=20)

        # Left hand plot
        axis[0][0].bar(df['Network'], df['AVG Clust'], color=['black', 'blue'], width=0.3)
        axis[0][0].set_ylabel('Average clustering coefficient')
        axis[0][0].set_title("Plot of Average clustering coefficient vs Network ")


        # Right hand plot
        axis[0][1].bar(df['Network'], df['Network d'], color=['black', 'blue'], width=0.3)
        axis[0][1].set_ylabel('Network diameter',)
        axis[0][1].set_title('Plot of Network diameter vs Network')

        #plt.show()


        # Histogram

        betw_cents1 = nx.betweenness_centrality(pn1.p_network)
        betw_cents2 = nx.betweenness_centrality(pn2.p_network)

        cents1 = [betw_cents1[n] for n in betw_cents1.keys()]
        cents2 = [betw_cents2[n] for n in betw_cents2.keys()]
        #fig, axes = plt.subplots(1, 2)

        # axes[0] = left, axes[1] = right
        sns.histplot(cents1, ax=axis[1][0], color='red', bins=80, binwidth=0.1)
        axis[1][0].set_xlabel('Betweenness centrality')
        axis[1][0].set_title('Betweenness centrality distribution for Network 1')

        sns.histplot(cents2, ax=axis[1][1], color='green')
        axis[1][1].set_xlabel('Betweenness centrality')
        axis[1][1].set_title('Betweenness centrality distribution for Network 2')



        plt.show()

        # betw_cents1 = nx.betweenness_centrality(pn1.p_network)
        # betw_cents2 = nx.betweenness_centrality(pn2.p_network)
        #
        #
        # cents1 = [betw_cents1[n] for n in betw_cents1.keys()]
        # cents2 = [betw_cents2[n] for n in betw_cents2.keys()]
        # fig, axes = plt.subplots(1, 2)
        #
        # # axes[0] = left, axes[1] = right
        # sns.histplot(cents1, ax=axes[0], color='red', bins=80)
        # axes[0].set_title('Network 1')
        #
        # sns.histplot(cents2, ax=axes[1], color='green')
        # axes[1].set_title('Network 2')
        #
        # plt.xlabel('Squamosal horn length')
        # plt.title('Histogram of betweenness centralities')
        # plt.show()





        return df


s1 = Network("string_interactions_short.tsv")
s2 = Network("string_interactions_short_2.tsv")
s3 = Network('string_interactions_short (newww).tsv')
s1.network_graph()
s2.network_graph()
s1.plot_degree_dist()

print('No. of proteins in the graph : ', s1.no_prot)
print('No of interactions in the graph : ', s1.no_inter)

print('No. of proteins in the graph : ', s2.no_prot)
print('No of interactions in the graph : ', s2.no_inter)

print('Degree of protein : ', s1.prot_degree('DREB1G'))
print('Degree of protein : ', s2.prot_degree('P1R1'))

print('Shortest path : ', s1.shortest_path('IRO2', 'PHR3'))

print('Network diameter : ', s1.network_diameter)
print('Network diameter : ', s2.network_diameter)
print('Network diameter : ', s3.network_diameter)

print('Cluster co : ', s1.cluster_co('IRO2'))
print('Cluster co : ', s2.cluster_co('BPM1'))

print('between cent : ', s1.betw_cent("IRO2"))
print('between cent : ', s2.betw_cent('P1R1'))

print(s1.betw_cent_hist())
print(s2.betw_cent_hist())

print(Network.compare_2("string_interactions_short.tsv", "string_interactions_short_2.tsv"))