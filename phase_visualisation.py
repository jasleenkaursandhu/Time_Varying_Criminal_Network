import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
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

# Create a folder to store the images
if not os.path.exists("phase_images"):
    os.mkdir("phase_images")

# Loop through each phase
for phase in range(1, 12):
    plt.figure(figsize=(10, 6))
    pos = nx.drawing.nx_agraph.graphviz_layout(G[phase])
    nx.draw(G[phase], pos, with_labels=True)
    plt.title(f"Phase {phase} Network Visualization")
    plt.grid(True)

    # Save the visualization as an image in the "phase_images" folder
    image_file = f"phase_images/phase{phase}_network_visualization.png"
    plt.savefig(image_file)

    # Close the plot to save memory
    plt.close()

print("Visualizations saved in the 'phase_images' folder.")
