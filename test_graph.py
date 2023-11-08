import unittest

from graph import Graph


class TestGraphMethods(unittest.TestCase):
    def test_add_vertex(self):
        graph = Graph()

        graph.add_vertex('A')
        graph.add_vertex('B')

        self.assertEqual(graph.graph, {'A': [], 'B': []})

        with self.assertRaises(ValueError):
            graph.add_vertex('A')

    def test_add_edge(self):
        graph = Graph()

        graph.add_vertex('A')
        graph.add_vertex('B')
        graph.add_vertex('C')

        graph.add_edge('A', 'B')
        graph.add_edge('A', 'C')

        self.assertEqual(graph.graph, {'A': ['B', 'C'], 'B': ['A'], 'C': ['A']})

        with self.assertRaises(ValueError):
            graph.add_edge('A', 'B')

        with self.assertRaises(ValueError):
            graph.add_edge('A', 'D')

    def test_remove_vertex(self):
        graph = Graph()

        graph.add_vertex('A')
        graph.add_vertex('B')

        graph.remove_vertex('A')

        self.assertEqual(graph.graph, {'B': []})

        with self.assertRaises(ValueError):
            graph.remove_vertex('A')

    def test_remove_edge(self):
        graph = Graph()

        graph.add_vertex('A')
        graph.add_vertex('B')
        graph.add_vertex('C')

        graph.add_edge('A', 'B')
        graph.add_edge('A', 'C')

        graph.remove_edge('A', 'B')

        self.assertEqual(graph.graph, {'A': ['C'], 'B': [], 'C': ['A']})

        with self.assertRaises(ValueError):
            graph.remove_edge('A', 'B')

        with self.assertRaises(ValueError):
            graph.remove_edge('A', 'D')

    def test_show_neighbours(self):
        graph = Graph()

        graph.add_vertex('A')
        graph.add_vertex('B')
        graph.add_vertex('C')

        graph.add_edge('A', 'B')
        graph.add_edge('A', 'C')

        neighbours = graph.show_neighbours('A')
        self.assertEqual(neighbours, ['B', 'C'])

        with self.assertRaises(ValueError):
            graph.show_neighbours('D')

    def test_dfs(self):
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

        dfs_result = graph.dfs('A')
        self.assertEqual(dfs_result, ['A', 'B', 'C', 'D', 'E'])

        with self.assertRaises(ValueError):
            graph.dfs('F')

    def test_bfs(self):
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

        bfs_result = graph.bfs('A')
        self.assertEqual(bfs_result, ['A', 'B', 'C', 'D', 'E'])

        with self.assertRaises(ValueError):
            graph.bfs('F')


if __name__ == '__main__':
    unittest.main()
