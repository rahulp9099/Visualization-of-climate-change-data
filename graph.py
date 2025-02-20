class Node:
    def __init__(self,vertex) -> None:
        self.vertex = vertex
        self.next = None
    
class Graph:
    def __init__(self) -> None:
        self.graph = {}
    
    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = None
        else:
            print(f"Vertex {vertex} already exists")
    
    def add_edge(self,src,dest):
        if src in self.graph and dest in self.graph:
            new_node = Node(dest)
            new_node.next = self.graph[src]
            self.graph[src] = new_node
            
            new_node = Node(src)
            new_node.next = self.graph[dest]
            self.graph[dest] = new_node
            