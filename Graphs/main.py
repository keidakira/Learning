class Graph:
    def __init__(self, size):
        # To initialize a matrix with it's size
        self.data = []
        for i in range(size):
            temp_data = []
            for j in range(size):
                if i == j:
                    temp_data.append(0)
                else:
                    temp_data.append(9999999)
            self.data.append(temp_data)
        self.size = size

    def add_edge(self, u, v):
        # To add an edge between two vertices
        self.data[u][v] = 1

    def remove_edge(self, u, v):
        # To remove an edge between two vertices
        self.data[u][v] = 0

    def print(self):
        print(self.data)

    def bfs(self, start):
        node = start
        visited = [False]*self.size

        from queue import Queue
        q = Queue()
        q.put(node)
        while not q.empty():
            curr_node = q.get()
            visited[curr_node] = True
            print(curr_node)
            # Add all its connected nodes to queue
            for i, e_node in enumerate(self.data[curr_node]):
                if visited[i] == False and e_node == 1:
                    q.put(i)


if __name__ == "__main__":
    graph = Graph(3)
    graph.add_edge(1, 2)
    # graph.add_edge(2, 1)
    graph.add_edge(0, 1)
    # graph.add_edge(1, 0)
    graph.bfs(1)
