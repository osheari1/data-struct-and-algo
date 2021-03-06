# python3
import sys, threading

sys.setrecursionlimit(10 ** 7)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size

""" Constraints
2 <= n <= 10^3
1 <= m <= 10^3
"""


class DGraph:

    def __init__(self, n, g, g_r):
        self.graph = g
        self.graph_r = g_r
        self.n = n
        self.cc_num = self.empty_arr()
        self.pre = self.empty_arr()
        self.post = self.empty_arr()
        self.visited = self.empty_arr(False)
        self.cyclic = None

    def print_n_connected(self):
        print(len(set(self.cc_num[1:])))

    def empty_arr(self, x=None):
        return [-1] + [x] * self.n

    def print_graph(self):
        for i, g in enumerate(self.graph):
            print(i, "->", [x for x in g])

    def print_pre_post_order(self):
        for i, (pr, po) in enumerate(zip(self.pre, self.post)):
            print(i, "->", "(%d, %d)" % (pr, po))

    def print_order(self):
        sorted_post = sorted(range(1, len(self.graph)),
                             key=lambda x: self.post[x])
        print(" ".join(map(str, reversed(sorted_post))))

    def explore(self, v=1, cc=0, clock=0, reverse=False):
        graph = self.graph_r if reverse else self.graph

        def go(v, cc, clock, path):
            self.visited[v] = True
            self.cc_num[v] = cc
            clock = self.previsit(v, clock)
            path.append(v)
            for w in graph[v]:
                if w in path:
                    self.cyclic = True
                if not self.visited[w]:
                    clock = go(w, cc, clock, path)
            clock = self.postvisit(v, clock)
            path.pop()
            return clock

        return go(v, cc, clock, [])

    def connected(self, v, u):
        return 1 if self.cc_num[u] == self.cc_num[v] else 0

    def dfs(self, reverse=False):
        graph = self.graph_r if reverse else self.graph
        cc = 0
        clock = 0
        for v in range(len(graph))[1:]:
            if not self.visited[v]:
                clock = self.explore(v, cc, clock, reverse=reverse)
                cc += 1
        if self.cyclic is None:
            self.cyclic = False

    def connect_components(self):
        self.dfs(reverse=True)
        order = list(reversed(sorted(
                range(1, len(self.graph)),
                key=lambda x: self.post[x])))

        self.visited = self.empty_arr(False)
        cc = 0
        for v in order:
            if not self.visited[v]:
                self.explore(v, cc)
                cc += 1

    def previsit(self, v, clock):
        self.pre[v] = clock
        return clock + 1

    def postvisit(self, v, clock):
        self.post[v] = clock
        return clock + 1

    def n_comp(self):
        return len(set(self.cc_num[1:]))

    def is_cyclic(self):
        return 1 if self.cyclic else 0


def read_nodes_stdin(n, m):
    graph = [[] for _ in range(n + 1)]
    graph_r = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = list(map(lambda x: int(x), input().split(" ")))
        graph[u].append(v)
        graph_r[v].append(u)
    return graph, graph_r


def read_nodes(n, g=None):
    graph = [[] for _ in range(n + 1)]
    graph_r = [[] for _ in range(n + 1)]
    for u, v in g:
        graph[u].append(v)
        graph_r[v].append(u)

    return graph, graph_r


def str_2_g(str: str):
    l = str.split(" ")
    return [(int(l[i]), int(l[i + 1])) for i in range(len(l))[::2]]


def main():
    # n - number of vertices
    # m - number of edges
    n, m = list(map(int, input().split(" ")))
    g, g_r = read_nodes_stdin(n, m)
    graph = DGraph(n, g, g_r)
    graph.connect_components()
    # graph.print_order()
    graph.print_n_connected()

    # g1 = [(1, 2), (3, 2), (4, 3), (1, 4)]
    # n1 = 4
    # # o1 = (1, 4)
    # #
    # g2 = [(1, 2), (3, 2)]
    # n2 = 4
    # # o2 = (1, 4)
    # #
    # g3_str = '5 3 4 10 3 2 1 3 4 9 2 6 8 3 8 2 6 1 6 10 10 6 1 4 3 8 1 5 8 9 ' \
    #          '5 ' \
    #        '1 8 5 7 8 3 4 8 4'
    # g3 = str_2_g(g3_str)
    # n3 = 10
    #
    # # g3 = [(1, 2), (4, 1), (2, 3), (3, 1)]
    # # n3 = 4
    #
    # g4 = [(1, 2), (2, 3), (1, 3), (3, 4), (1, 4), (2, 5), (3, 5)]
    # n4 = 5
    #
    # g5 = [(1, 2), (4, 1), (3, 1)]
    # n5 = 4
    #
    # g6 = [(3, 1)]
    # n6 = 4
    #
    # g7 = [(2, 1), (3, 2), (3, 1), (4, 3), (4, 1), (5, 2), (5, 3)]
    # n7 = 5
    #
    # g8 = [(1, 2), (4, 1), (2, 3), (3, 1)]
    # n8 = 4
    #
    # g9 = [(1, 2), (3, 2), (4, 3)]
    # n9 = 4
    #
    # for (g, n) in [
    #     # (g1, n1),
    #     # (g2, n2),
    #     (g3, n3),
    #     # (g4, n4),
    #     # (g5, n5),
    #     # (g6, n6),
    #     (g7, n7),
    #     (g8, n8),
    #     (g9, n9),
    # ]:
    #     # g = [(x[0] - 1, x[1] - 1) for x in g]
    #     # o = (o[0] - 1, o[1] - 1)
    #
    #     g, g_r = read_nodes(n, g)
    #     graph = DGraph(n, g, g_r)
    #     graph.print_graph()
    #     graph.connect_components()
    #     graph.print_pre_post_order()
    #     graph.print_n_connected()
    #     print(graph.cc_num)
    #     print()



threading.Thread(target=main).start()
