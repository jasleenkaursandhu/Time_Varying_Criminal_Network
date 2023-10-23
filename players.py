import pandas as pd
import networkx as nx

# Step 1: Load the data
phases = {}
G = {}

for i in range(1, 12):
    var_name = "phase" + str(i)
    file_name = "https://raw.githubusercontent.com/ragini30/Networks-Homework/main/" + var_name + ".csv"
    phases[i] = pd.read_csv(file_name, index_col=["players"])
    phases[i].columns = "n" + phases[i].columns
    phases[i].index = phases[i].columns
    phases[i][phases[i] > 0] = 1
    G[i] = nx.from_pandas_adjacency(phases[i])
    G[i].name = var_name

# Step 2: Define actor roles
actor_roles = {
    'n1': 'Mastermind of the network',
    'n3': 'Principal lieutenant of Serero',
    'n83': 'Investor and transporter of money',
    'n86': 'Investor and transporter of money',
    # Add other actors and their roles here
}

# Step 3: Print names and roles of all actors
for actor_id, role in actor_roles.items():
    print(f"Actor {actor_id}: {role}")
