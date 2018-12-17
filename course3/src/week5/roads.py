# python3
import math
import heapq


class Edge:
    def __init__(self, g1, g2):
        self.w = dist(g1[0], g2[0], g1[1], g2[1])
        self.g1 = g1
        self.g2 = g2

    def __str__(self):
        return "(%s -> %s : %.2f)" % (self.g1, self.g2, self.w)

    def __repr__(self):
        return "(%s -> %s : %.2f)" % (self.g1, self.g2, self.w)


def dist(x1, x2, y1, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def empty_arr(n, x):
    return [x]


def print_graph(g):
    for g_ in g:
        print(g_)


def read_nodes_stdin(n, m):
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = list(map(lambda x: int(x), input().split(" ")))
        graph[u].append(v)
        graph[v].append(u)
    return graph


def kruskal(edges):
    sets = [set(i) for i in range(len(g))]
    x = set()

    edges = sorted(edges, key=lambda x: x.w)

    cost = empty_arr(len(g), float('inf'))
    parent = empty_arr(None)
    cost[0] = 0
    # pq =


def create_edges(g):
    edges = []
    for u in range(len(g)):
        for v in range(len(g)):
            if u == v:
                continue
            edges.append(Edge(g[u], g[v]))
    return edges


# def read_nodes(g):
#     graph = [[] for _ in range(len(g))]
#     weights = {i: {} for i in range(0, len(g))}
#     for u in range(len(g)):
#         for v in range(len(g)):
#             if u == v:
#                 continue
#             graph[u].append(v)
#             weights[u][v] = dist(g[u][0], g[v][0], g[u][1], g[v][1])
#     return graph, weights


if __name__ == '__main__':
    # n - number of vertices
    # m - number of edges
    # n, m = list(map(int, input().split(" ")))
    # g = read_nodes_stdin(n, m)
    # u, v = list(map(lambda x: int(x), input().split(" ")))

    g1 = [(0, 0), (0, 1), (1, 0), (1, 1)]

    for g in [
        g1,
        # (g2, n2),
        # (g3, n3),
        # (g4, n4),
        # (g5, n5),
    ]:
        g = create_edges(g)
        print_graph(g)
        print(sorted(g, key=lambda x: x.w))

# g = [(x[0] - 1, x[1] - 1) for x in g]
# o = (o[0] - 1, o[1] - 1)
