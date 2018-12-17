# python3
from queue import Queue
import heapq

""" Constraints
2 <= n <= 10^3
1 <= m <= 10^3
"""


def flip(x):
    if x is None:
        return 1
    elif x == 1:
        return 0
    else:
        return 1


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


def read_nodes_stdin_directed(n, m):
    graph = [[] for _ in range(n + 1)]
    weights = {i: {} for i in range(1, n + 1)}
    for _ in range(m):
        u, v, w = list(map(lambda x: int(x), input().split(" ")))
        graph[u].append(v)
        weights[u][v] = w
    return graph, weights


def read_nodes_directed(n, g):
    graph = [[] for _ in range(n + 1)]
    weights = {i: {} for i in range(1, n + 1)}
    for u, v, w in g:
        graph[u].append(v)
        weights[u][v] = w
    return graph, weights


def str_2_g(str: str):
    l = str.split(" ")
    return [(int(l[i]), int(l[i + 1])) for i in range(len(l))[::2]]


def number_of_components(adj):
    result = 0
    # write your code here
    return result


class Graph:

    def __init__(self, n, g, w: dict):
        self.graph = g
        self.w = w
        self.n = n
        self.cc_num = self.empty_arr()
        self.prev = self.empty_arr(None)
        self.bipartite = None

    def empty_arr(self, x=None):
        return [-1] + [x] * self.n

    def print_graph(self):
        for i, g in enumerate(self.graph):
            print(i, "->", [(x, self.w.get(i, 0).get(x)) for x in g])

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

    def bfs(self, s=1):
        dist = self.empty_arr(float('inf'))
        # prev = self.empty_arr(None)
        dist[s] = 0
        q = Queue()
        q.put_nowait(s)
        while not q.empty():
            u = q.get_nowait()
            for v in self.graph[u]:
                if dist[v] == float('inf'):
                    q.put_nowait(v)
                    dist[v] = dist[u] + 1
                    self.prev[v] = u
        return dist

    def reconstruct(self, u, s):
        path = []
        while u != s:
            path.append(u)
            u = self.prev[u]
        return reversed(path)

    def bfs_bipartite(self, s=1):
        dist = self.empty_arr(float('inf'))
        prev = self.empty_arr(None)
        bipartite = self.empty_arr(None)
        dist[s] = 0
        q = Queue()
        q.put_nowait(s)
        bipartite[s] = 0
        while not q.empty():
            u = q.get_nowait()
            for v in self.graph[u]:
                b_neigh = bipartite[v]
                if b_neigh is None:
                    bipartite[v] = flip(bipartite[u])
                if b_neigh == bipartite[u]:
                    self.bipartite = False

                if dist[v] == float('inf'):
                    q.put_nowait(v)
                    dist[v] = dist[u] + 1
                    prev[v] = u
        self.bipartite = 1 if self.bipartite is None else 0
        return dist

    def shortest_path(self, u, v):
        dists = self.bfs(u)
        return -1 if dists[v] == float('inf') else dists[v]

    def n_comp(self):
        return len(set(self.cc_num[1:]))

    def dijkstra(self, s=1, e=1):
        dist = self.empty_arr(float('inf'))
        prev = self.empty_arr(None)
        done = {i: False for i in range(1, self.n+1)}
        ndone = 0
        dist[s] = 0
        h = [(d, i) for d, i in zip(dist[1:], range(1, self.n + 1))]
        heapq.heapify(h)
        while ndone < self.n:
            d, u = heapq.heappop(h)
            if done[u]:
                continue
            done[u] = True
            ndone += 1
            for v in self.graph[u]:
                if dist[v] > dist[u] + self.w[u][v]:
                    dist[v] = dist[u] + self.w[u][v]
                    prev[v] = u
                    heapq.heappush(h, (dist[v], v))

        return dist[e] if dist[e] != float('inf') else -1


if __name__ == '__main__':
    # n - number of vertices
    # m - number of edges
    n, m = list(map(int, input().split(" ")))
    g, w = read_nodes_stdin_directed(n, m)
    s, e = list(map(int, input().split(" ")))
    graph = Graph(n, g, w)
    print(graph.dijkstra(s, e))

    # g1 = [(1, 2, 1), (4, 1, 2), (2, 3, 2), (1, 3, 5)]
    # n1 = 4
    # o1 = (1, 3)
    #
    # g2 = [(1, 2, 4), (1, 3, 2), (2, 3, 2), (3, 2, 1), (2, 4, 2), (3, 5, 4),
    #       (5, 4, 1), (2, 5, 3), (3, 4, 4)]
    # n2 = 5
    # o2 = (1, 5)
    #
    # g3 = [(1, 2, 7), (1, 3, 5), (2, 3, 2)]
    # n3 = 4
    # o3 = (3, 2)
    #
    # for (g, n, o) in [
    #     (g1, n1, o1),
    #     (g2, n2, o2),
    #     (g3, n3, o3),
    # ]:
    #     graph = Graph(n, *read_nodes_directed(n, g))
    #     graph.print_graph()
    #     print(graph.dijkstra(*o))
    #     print()
