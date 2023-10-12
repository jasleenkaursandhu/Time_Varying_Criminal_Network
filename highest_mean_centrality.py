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

# Define the players of interest
players_of_interest = ["n1", "n3", "n12", "n83"]

# Initialize dictionaries to store centrality values
betweenness_centrality_values = {}
eigenvector_centrality_values = {}

# Calculate centrality for each player at each phase
for phase in range(1, 12):
    centrality_betweenness = nx.betweenness_centrality(G[phase], normalized=True)
    centrality_eigenvector = nx.eigenvector_centrality(G[phase])
    for player in players_of_interest:
        if player not in betweenness_centrality_values:
            betweenness_centrality_values[player] = []
            eigenvector_centrality_values[player] = []
        if player in centrality_betweenness:
            betweenness_centrality_values[player].append(centrality_betweenness[player])
        else:
            betweenness_centrality_values[player].append(0)
        if player in centrality_eigenvector:
            eigenvector_centrality_values[player].append(centrality_eigenvector[player])
        else:
            eigenvector_centrality_values[player].append(0)

# Calculate the mean centrality for each player
mean_betweenness_centrality = {player: sum(values) / 11 for player, values in betweenness_centrality_values.items()}
mean_eigenvector_centrality = {player: sum(values) / 11 for player, values in eigenvector_centrality_values.items()}

# Find the top three players with the highest mean centrality for betweenness and eigenvector centrality
top_three_betweenness = sorted(mean_betweenness_centrality, key=mean_betweenness_centrality.get, reverse=True)[:3]
top_three_eigenvector = sorted(mean_eigenvector_centrality, key=mean_eigenvector_centrality.get, reverse=True)[:3]

# Print the results
print("Players with the highest mean betweenness centrality:")
for i, player in enumerate(top_three_betweenness, 1):
    print(f"{i}. {player}: {mean_betweenness_centrality[player]:.3f}")

print("\nPlayers with the highest mean eigenvector centrality:")
for i, player in enumerate(top_three_eigenvector, 1):
    print(f"{i}. {player}: {mean_eigenvector_centrality[player]:.3f}")
