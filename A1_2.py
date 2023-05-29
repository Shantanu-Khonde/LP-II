#DFS
graph = {

   'A': {'B', 'C'},
   'B': {'A', 'D', 'E'},
   'C': {'A', 'F'},
   'D': {'B'},
   'E': {'B', 'F'},
   'F': {'C', 'E'}
}

visited = set()

def dfs(visited, graph, node):
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbor in graph[node]:
            
            dfs(visited, graph, neighbor)


#Driver Code
print("Following is the Depth-First Search")
dfs(visited, graph, 'A')

graph = {

   'A': {'B', 'C'},
   'B': {'A', 'D', 'E'},
   'C': {'A', 'F'},
   'D': {'B'},
   'E': {'B', 'F'},
   'F': {'C', 'E'}
}

visited = [] # List for visited nodes. 
queue = [] #Initialize a queue



#BFS
def bfs(visited, graph, node): #function for BFS 
    visited.append(node)
    queue.append(node)

    while queue: # Creating loop to visit each node .
      m = queue.pop(0)
      print (m, end = " ")

      for neighbour in graph[m]:
        if neighbour not in visited: 
            visited.append(neighbour) 
            queue.append(neighbour)

# Driver Code
print("Following is the Breadth-First Search") 
bfs(visited, graph, 'A') # function calling

