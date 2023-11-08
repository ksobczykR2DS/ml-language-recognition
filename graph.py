from typing import Dict, Any, List


class Graph:
    def __init__(self):
        self.graph: Dict[Any, Any] = {}

    @staticmethod
    def check_if_valid_key_type(key) -> bool:
        key_supported_types = (str, int, float, bool, tuple)
        return isinstance(key, key_supported_types)

    def add_vertex(self, vertex: Any) -> None:
        if not self.check_if_valid_key_type(vertex):
            raise ValueError(f"Wartość typu {type(vertex)} nie może być kluczem w słowniku.")
        elif vertex in self.graph:
            raise ValueError(f"Ta wartość '{vertex}' znajduję się już w grafie.")
        else:
            self.graph[vertex] = []

    def remove_vertex(self, vertex: Any) -> None:
        if not self.check_if_valid_key_type(vertex):
            raise ValueError(f"Wartość typu {type(vertex)} nie może być kluczem w słowniku.")
        elif vertex in self.graph:
            for vertex_edges in self.graph[vertex]:
                self.graph[vertex_edges].remove(vertex)
            del self.graph[vertex]
        else:
            raise ValueError(f"Wierzchołek '{vertex}' nie należy do grafu.")

    def add_edge(self, start_vertex: Any, end_vertex: Any) -> None:
        if not self.check_if_valid_key_type(start_vertex) and self.check_if_valid_key_type(end_vertex):
            raise ValueError(f"Jedna lub obie wartości sa typu, który nie może być kluczem w słowniku.")
        elif start_vertex in self.graph and end_vertex in self.graph:
            if end_vertex not in self.graph[start_vertex]:
                self.graph[start_vertex].append(end_vertex)
                self.graph[end_vertex].append(start_vertex)
            else:
                raise ValueError(f"Krawedz miedzy podanymi punktami ({start_vertex} i {end_vertex}) już istnieje.")
        else:
            raise ValueError("Jeden lub oba z podanych wierzchołków nie należą do grafu.")

    def remove_edge(self, start_vertex: Any, end_vertex: Any) -> None:
        if not self.check_if_valid_key_type(start_vertex) and self.check_if_valid_key_type(end_vertex):
            raise ValueError(f"Jedna lub obie wartości są typu, który nie może być kluczem w słowniku.")
        elif start_vertex in self.graph and end_vertex in self.graph:
            self.graph[start_vertex].remove(end_vertex)
            self.graph[end_vertex].remove(start_vertex)
        else:
            raise ValueError("Jeden lub oba z podanych wierzchołków nie należą do grafu.")

    def show_neighbours(self, vertex: Any) -> List[Any]:
        if not self.check_if_valid_key_type(vertex):
            raise ValueError(f"Podana wartość nie może byc kluczem grafu.")
        elif vertex in self.graph:
            neighbours = self.graph[vertex]
            print(f"Sąsiadami podanego wierzchołką {vertex} są {neighbours}.")
            return neighbours
        else:
            raise ValueError(f"Podany wierzchołek nie należy do grafu.")

    def print_graph(self) -> None:
        for vertex in self.graph:
            print(f"{vertex}: {self.graph[vertex]}")

    def dfs(self, start_vertex: Any):
        if not self.check_if_valid_key_type(start_vertex):
            raise ValueError(f"Podana wartość nie może byc kluczem grafu.")
        elif start_vertex not in self.graph:
            raise ValueError(f"Podany wierzchołek '{start_vertex}' nie istnieje w grafie.")

        def dfs_recursive(vertex, visited):
            visited.add(vertex)
            result.append(vertex)
            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    dfs_recursive(neighbor, visited)

        visited = set()
        result = []
        dfs_recursive(start_vertex, visited)
        return result

    def bfs(self, start_vertex: Any):
        if not self.check_if_valid_key_type(start_vertex):
            raise ValueError(f"Podana wartość nie może byc kluczem grafu.")
        elif start_vertex not in self.graph:
            raise ValueError(f"Podany wierzchołek '{start_vertex}' nie należy do grafu.")

        visited = set()
        result = []
        queue = [start_vertex]

        while queue:
            current_vertex = queue.pop(0)
            if current_vertex not in visited:
                visited.add(current_vertex)
                result.append(current_vertex)
                queue.extend(neighbor for neighbor in self.graph[current_vertex] if neighbor not in visited)

        return result

    def __iter__(self):
        return GraphIterator(self.graph)


class GraphIterator:
    def __init__(self, graph):
        self.graph = graph
        self.vertices = list(graph.keys())
        self.current_index = 0

    def __next__(self):
        if self.current_index < len(self.vertices):
            current_vertex = self.vertices[self.current_index]
            self.current_index += 1
            return current_vertex
        else:
            raise StopIteration


def main():
    # Przygotowanie grafu
    graph = Graph()

    graph.add_vertex('A')
    graph.add_vertex('B')
    graph.add_vertex('C')
    graph.add_vertex('D')
    graph.add_vertex('E')

    graph.add_edge('A', 'B')
    graph.add_edge('A', 'C')
    graph.add_edge('B', 'C')
    graph.add_edge('A', 'D')
    graph.add_edge('D', 'E')

    # test metod grafu
    print("Graf po dodaniu wierzchołków i krawędzi:")
    graph.print_graph()

    graph.show_neighbours('A')
    graph.remove_vertex('B')
    graph.remove_edge('A', 'C')
    print("Graf po usunięciu wierzchołka 'B' oraz krawędzi między 'A' a 'C':")
    graph.print_graph()

    # test końcówki zadania
    print("DFS:")
    for vertex in graph.dfs("A"):
        print(vertex)

    print("\nBFS:")
    for vertex in graph.bfs("A"):
        print(vertex)


if __name__ == "__main__":
    main()
