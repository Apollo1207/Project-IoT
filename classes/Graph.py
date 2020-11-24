class Graph:

    def __init__(self):
        self.connections = {}

    def create_edges_from_vertexes(self, first_vertex_id: int, second_vertex_id: int, weight: int):

        if (type(first_vertex_id) is not int) or (type(second_vertex_id) is not int) or (type(weight) is not int):
            raise TypeError('All the params must be "Integer"')
        if weight < 0:
            raise ValueError('Weight can`t be negative')
        self.__create_edge(first_vertex_id, second_vertex_id, weight)
        self.__create_edge(second_vertex_id, first_vertex_id, weight)

    def __create_edge(self, vertex_from: int, vertex_to: int, weight: int):
        if vertex_from in self.connections.keys():
            if (vertex_to, weight) not in self.connections[vertex_from]:
                self.connections[vertex_from].append((vertex_to, weight))
        else:
            self.connections[vertex_from] = [(vertex_to, weight)]

    def print_graph(self):
        for el in self.connections:
            print(el, self.connections[el])
