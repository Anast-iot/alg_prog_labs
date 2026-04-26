import csv

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x]) 
    return parent[x]

def union(parent, rank, x, y):
    rx = find(parent, x)
    ry = find(parent, y)
    if rx == ry:
        return False  
    if rank[rx] < rank[ry]:
        parent[rx] = ry
    elif rank[rx] > rank[ry]:
        parent[ry] = rx
    else:
        parent[ry] = rx
        rank[rx] = rank[rx] + 1
    return True

def read_csv(filename):
    edges = {}   
    nodes = {}  
    edge_count = 0

    with open(filename, newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            u = row[0].strip()
            v = row[1].strip()
            w = int(row[2].strip())

            edges[edge_count] = (u, v, w)
            edge_count = edge_count + 1

            nodes[u] = True
            nodes[v] = True

    return edges, nodes, edge_count

def sort_edges(edges, edge_count):
    arr = {}
    for i in range(edge_count):
        arr[i] = edges[i]

    for i in range(edge_count):
        for j in range(edge_count - i - 1):
            if arr[j][2] > arr[j + 1][2]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

def kruskal(filename):
    edges, nodes, edge_count = read_csv(filename)

    node_count = 0
    for _ in nodes:
        node_count = node_count + 1

    parent = {}
    rank = {}
    for node in nodes:
        parent[node] = node
        rank[node] = 0

    sorted_edges = sort_edges(edges, edge_count)

    total = 0
    used_edges = 0

    for i in range(edge_count):
        u, v, w = sorted_edges[i]
        if union(parent, rank, u, v):
            total = total + w
            used_edges = used_edges + 1

    if used_edges != node_count - 1:
        return -1

    return total

result = kruskal("communication_wells.csv")
print(result)