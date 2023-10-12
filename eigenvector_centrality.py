import pandas as pd
import networkx as nx
import os

# Initialize dictionaries to store data
phases = {}
G = {}

# Load data and create NetworkX graphs
for i in range(1, 12):
    var_name = "phase" + str(i)
    file_name = "https://raw.githubusercontent.com/ragini30/Networks-Homework/main/" + var_name + ".csv"
    phases[i] = pd.read_csv(file_name, index_col=["players"])
    phases[i].columns = "n" + phases[i].columns
    phases[i].index = phases[i].columns
    phases[i][phases[i] > 0] = 1
    G[i] = nx.from_pandas_adjacency(phases[i])
    G[i].name = var_name

# List of players under investigation
players = ["n1", "n3", "n12", "n83"]

# Compute and list eigenvector centrality for each player at the specified phases
for player in players:
    print(f"Player {player}:")
    for phase in [3, 9]:
        centrality = nx.eigenvector_centrality(G[phase])
        normalized_centrality = centrality[player]
        # Normalize eigenvector centrality
        norm_factor = (sum(v ** 2 for v in centrality.values())) ** 0.5
        normalized_centrality /= norm_factor
        print(f"Phase {phase}, Eigenvector Centrality = {normalized_centrality:.3f}")
