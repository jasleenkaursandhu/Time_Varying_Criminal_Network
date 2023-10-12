import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
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

# Initialize lists to store node and edge counts
node_counts = []
edge_counts = []

# Calculate and store node and edge counts for each phase
for i in range(1, 12):
    node_counts.append(G[i].number_of_nodes())
    edge_counts.append(G[i].number_of_edges())

# Create a list of phases (from 1 to 11)
phases_list = list(range(1, 12))

# Display the number of nodes and edges for the specified phases
phases_to_display = [2, 6, 10]

for phase in phases_to_display:
    idx = phases_list.index(phase)
    print(f"Phase {phase}:")
    print("Number of nodes:", node_counts[idx])
    print("Number of edges:", edge_counts[idx])
    print()

# Create the "images" folder if it doesn't exist
if not os.path.exists("images"):
    os.mkdir("images")

# Plot the evolution of the number of nodes and edges over time
plt.figure(figsize=(10, 6))
plt.plot(phases_list, node_counts, label="Number of Nodes", marker='o')
plt.plot(phases_list, edge_counts, label="Number of Edges", marker='x')
plt.xlabel("Phase")
plt.ylabel("Count")
plt.title("Evolution of Network Size (Nodes and Edges) Over Time")
plt.legend()
plt.grid(True)

# Save the plot to the "images" folder
plt.savefig("images/network_evolution_plot.png")

# Show the plot
plt.show()

# Visualize the graph for Phase 3
plt.figure(figsize=(10, 6))
nx.draw(G[3], pos=nx.drawing.nx_agraph.graphviz_layout(G[3]), with_labels=True)
plt.title("Phase 3 Network Visualization")
plt.grid(True)

# Save the visualization as an image in the "images" folder
plt.savefig("images/phase3_network_visualization.png")

# Show the plot
plt.show()
