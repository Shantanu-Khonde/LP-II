graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['E'],
    'D': ['B'],
    'E': ['C']
}

def dfs(graph, start):
    visited = [start]
    stack = [start]
    while stack:
        node = stack.pop()
        print(node)
        for adj in graph[node]:
            if adj not in visited:
                visited.append(adj)
                stack.append(adj)
                
print(dfs(graph, input("Enter the starting vertex : ")))



#----------------------BFS--------------------------------
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['E'],
    'D': ['B'],
    'E': ['C']
}

def bfs(graph, start):
    visited = [start]
    queue = [start]
    while queue:
        node = queue.pop(0)
        print(node)
        for adj in graph[node]:
            if adj not in visited:
                visited.append(adj)
                queue.append(adj)
                
print(bfs(graph, input("Enter the starting vertex : ")))