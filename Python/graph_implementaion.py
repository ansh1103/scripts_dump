class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}
        for start, end in edges:
            if start in self.graph_dict.keys():
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]

    def get_paths(self, start, end, path = []):
        pass


if __name__ == '__main__':
    routes = [
        ('mumbai', 'paris'),
        ('mumbai', 'dubai'),
        ('paris', 'dubai'),
        ('paris', 'new york'),
        ('dubai', 'new york'),
        ('new york', 'toronto')
    ]