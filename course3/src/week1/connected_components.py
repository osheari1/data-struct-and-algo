# python3
import sys

""" Constraints
2 <= n <= 10^3
1 <= m <= 10^3
"""


def number_of_components(adj):
    result = 0
    # write your code here
    return result


class Graph:

    def __init__(self, n, g):
        self.graph = g
        self.n = n
        self.cc_num = self.empty_arr()

    def empty_arr(self, x=None):
        return [-1] + [x] * self.n

    def print_graph(self):
        for i, g in enumerate(self.graph):
            print(i, "->", [x for x in g])

    def explore(self, v=1, cc=0):
        visited = self.empty_arr(False)

        def go(v, cc):
            visited[v] = True
            self.cc_num[v] = cc
            for w in self.graph[v]:
                if not visited[w]:
                    go(w, cc)

        go(v, cc)

    def connected(self, v, u):
        return 1 if self.cc_num[u] == self.cc_num[v] else 0

    def dfs(self):
        visited = self.empty_arr(False)
        cc = 0
        for v in range(len(self.graph))[1:]:
            if not visited[v]:
                self.explore(v, cc)
                cc += 1

    def n_comp(self):
        return len(set(self.cc_num[1:]))


def read_nodes_stdin(n, m):
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = list(map(lambda x: int(x), input().split(" ")))
        graph[u].append(v)
        graph[v].append(u)
    return graph


def read_nodes(n, g=None):
    graph = [[] for _ in range(n + 1)]
    for u, v in g:
        graph[u].append(v)
        graph[v].append(u)

    return graph


def str_2_g(str: str):
    l = str.split(" ")
    return [(int(l[i]), int(l[i + 1])) for i in range(len(l))[::2]]


if __name__ == '__main__':
    # n - number of vertices
    # m - number of edges
    n, m = list(map(int, input().split(" ")))
    g = read_nodes_stdin(n, m)
    graph = Graph(n, g)
    graph.dfs()
    print(graph.n_comp())

    # g1 = [(1, 2), (3, 2), (4, 3), (1, 4)]
    # n1 = 4
    # o1 = (1, 4)
    #
    # g2 = [(1, 2), (3, 2)]
    # n2 = 4
    # o2 = (1, 4)
    #
    # g3_str = "27 96 6 9 81 98 21 94 22 68 76 100 8 50 38 86 71 75 32 93 16 50 " \
    #          "71 84 6 72 22 58 7 19 19 76 44 75 24 76 31 35 11 89 42 98 63 92 " \
    #          "37 38 20 98 45 91 23 53 37 91 76 93 67 90 12 22 43 52 23 56 67 " \
    #          "68 1 21 17 83 63 72 30 32 7 91 50 69 38 44 55 89 15 23 11 72 28 " \
    #          "42 22 69 56 79 5 83 55 73 13 72 7 93 20 54 21 55 66 89 2 91 18 " \
    #          "88 26 64 11 61 28 59 12 86 42 95 17 82 50 66 66 99 40 71 20 40 " \
    #          "5 66 92 95 32 46 7 36 44 94 6 31 19 67 26 57 53 84 10 68 28 74 " \
    #          "34 94 25 61 71 88 10 89 28 52 72 79 39 73 11 80 44 79 13 77 30 " \
    #          "96 30 53 10 39 1 90 40 91 62 71 44 54 15 17 69 74 13 67 24 69 " \
    #          "34 96 21 50 20 91"
    # g3 = str_2_g(g3_str)
    # n3 = 100
    # o3 = (42, 46)
    #
    # for (g, n, o) in [(g1, n1, o1), (g2, n2, o2), (g3, n3, o3)]:
    #     # g = [(x[0] - 1, x[1] - 1) for x in g]
    #     # o = (o[0] - 1, o[1] - 1)
    #
    #     graph = Graph(n, read_nodes(n, g))
    #     graph.print_graph()
    #     graph.dfs()
    #
    #     print(graph.cc_num)
    #     print(graph.n_comp())
        # print(graph.connected(o[0], o[1]))

