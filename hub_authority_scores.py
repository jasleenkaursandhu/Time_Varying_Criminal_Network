import pandas as pd
import networkx as nx

# Create a directed graph for each phase
G = {}
for i in range(1, 12):
    var_name = "phase" + str(i)
    file_name = "https://raw.githubusercontent.com/ragini30/Networks-Homework/main/" + var_name + ".csv"
    data = pd.read_csv(file_name, index_col=["players"])
    data.index = data.columns
    data[data > 0] = 1
    G[i] = nx.DiGraph(data)

# Calculate hub and authority scores for each phase
hub_scores = {}
authority_scores = {}

for phase in G:
    hub_scores[phase], authority_scores[phase] = nx.algorithms.link_analysis.hits(G[phase], max_iter=1000000)

# Create a text file for output
with open("hub_authority_scores.txt", "w") as output_file:
    # Redirect print statements to the file
    original_print = print
    print = lambda *args, **kwargs: original_print(*args, file=output_file, **kwargs)

    # Print hub and authority scores for each actor in each phase
    for phase, scores in hub_scores.items():
        print(f"Phase {phase} Hub Scores:")
        for actor, score in scores.items():
            print(f"{actor}: {score}")

    for phase, scores in authority_scores.items():
        print(f"Phase {phase} Authority Scores:")
        for actor, score in scores.items():
            print(f"{actor}: {score}")

# Close the file
output_file.close()

# Restore the original print function
print = original_print
