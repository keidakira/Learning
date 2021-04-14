class Graph:
    def __init__(self, size):
        # To initialize a matrix with it's size
        self.data = [[0]*size for i in range(size)]
        self.size = size

    def add_edge(self, u, v):
        # To add an edge between two vertices
        self.data[u-1][v-1] = 1

    def remove_edge(self, u, v):
        # To remove an edge between two vertices
        self.data[u-1][v-1] = 0

    def print(self):
        print(self.data)


if __name__ == "__main__":
    graph = Graph(3)
    graph.add_edge(1, 2)
    graph.add_edge(0, 1)
    graph.print()
