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

# Define the players and phases of interest
players_of_interest = ["n1", "n3", "n12", "n83"]
phases_of_interest = [3, 9]

# Initialize a dictionary to store betweenness centrality values
betweenness_centrality_values = {}

# Calculate normalized betweenness centrality for each player at each phase
for phase in phases_of_interest:
    for player in players_of_interest:
        centrality = nx.betweenness_centrality(G[phase], normalized=True)[player]
        betweenness_centrality_values[(phase, player)] = centrality

# Display the betweenness centrality values
for phase, player in betweenness_centrality_values:
    centrality = betweenness_centrality_values[(phase, player)]
    print(f"Phase {phase}, Player {player}: Normalized Betweenness Centrality = {centrality:.3f}")
