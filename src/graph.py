from linked_list import LinkedList


# Edges in this graph are explicitly bidirectional
# Implementation uses linked list to hold edges related to a vertex
# - this may not be optimum and a set-based collection may be better
class Graph:
    def __init__(self):
        self.__graph = {}

    def add_vertex(self, vertex):
        if vertex in self.__graph:
            print("Vertex [{}]: already exists".format(vertex))
            return False
        else:
            self.__graph[vertex] = LinkedList()
            return True

    def remove_vertex(self, vertex):
        if vertex not in self.__graph:
            print("Vertex [{}]: does not exist".format(vertex))
            return False
        else:
            # Remove any edge references to the vertex being removed
            for idx in range(self.__graph[vertex].length):
                ref = self.__graph[vertex].get_value(idx)
                self.remove_edge(ref, vertex)

            # Remove the vertex itself
            del self.__graph[vertex]
            return True

    def add_edge(self, v_from, v_to):
        if v_from not in self.__graph:
            print("Vertex [{}]: does not exist".format(v_from))
            return False

        if v_to not in self.__graph:
            print("Vertex [{}]: does not exist".format(v_to))
            return False

        if not self.__graph[v_from].contains(v_to):
            self.__graph[v_from].append(v_to)

        if not self.__graph[v_to].contains(v_from):
            self.__graph[v_to].append(v_from)

        return True

    def remove_edge(self, v_from, v_to):
        if v_from not in self.__graph:
            print("Vertex [{}]: does not exist".format(v_from))
            return False

        if v_to not in self.__graph:
            print("Vertex [{}]: does not exist".format(v_to))
            return False

        for idx in range(self.__graph[v_from].length):
            if self.__graph[v_from].get_value(idx) == v_to:
                self.__graph[v_from].remove(idx)
                break

        for idx in range(self.__graph[v_to].length):
            if self.__graph[v_to].get_value(idx) == v_from:
                self.__graph[v_to].remove(idx)
                break

        return True

    def print(self):
        print("Graph: {}".format("is empty" if len(self.__graph) == 0 else ""))
        for vertex in self.__graph:
            edges = "<No Edges>" if self.__graph[vertex].length == 0 \
                    else str(self.__graph[vertex].as_string())
            print("\tVertex [{}]: -->> {}".format(vertex, edges))


if __name__ == '__main__':
    graph = Graph()
    graph.print()
    graph.add_vertex("Bob")
    graph.print()
    graph.add_vertex("Jim")
    graph.add_vertex("Jim")
    graph.add_edge("Bob", "Fred")
    graph.add_edge("Bob", "Jim")
    graph.add_edge("Bob", "Jim")
    graph.print()
    graph.add_vertex("Fred")
    graph.add_vertex("Nigel")
    graph.add_edge("Fred", "Bob")
    graph.add_edge("Nigel", "Bob")
    graph.print()
    graph.remove_vertex("Jim")
    graph.print()
    graph.remove_edge("Fred", "Bob")
    graph.print()
    graph.remove_vertex("Bob")
    graph.print()

