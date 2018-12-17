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
        self.dist = self.empty_arr(float('inf'))
        self.max = (self.n + 1) * 10 ** 5
        self.cc_num = self.empty_arr()
        self.prev = self.empty_arr(None)
        self.on_cycle = []
        self.bipartite = None
        self.cycle = None
        self.last = None

    def empty_arr(self, x=None):
        return [-1] + [x] * self.n

    def print_graph(self):
        for i, g in enumerate(self.graph):
            print(i, "->", [(x, self.w.get(i, {}).get(x, 0)) for x in g])

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
        done = {i: False for i in range(1, self.n + 1)}
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

    def bf_cycle(self, s=1):
        dist = self.empty_arr(float('inf'))
        prev = self.empty_arr(None)
        for i in range(1, self.n + 1):
            if len(self.graph[i]) > 0:
                s = i
                break

        dist[s] = 0
        cycle = None
        for i in range(1, self.n + 10):
            for u in range(1, self.n + 1):
                for v in self.graph[u]:
                    if dist[v] > dist[u] + self.w[u][v]:
                        dist[v] = dist[u] + self.w[u][v]
                        prev[v] = u
                        if i >= self.n:
                            cycle = 1
            if i >= self.n and cycle != 1:
                cycle = 0

        return cycle if cycle is not None else 0, dist

    def bf_find_cycle(self):
        ss = set(range(1, self.n + 1))
        cycle = 0
        while len(ss) > 0:
            s = ss.pop()
            if len(self.graph[s]) == 0:
                continue
            cycle, dist, _, _ = self.bf_(s)
            for i, d in enumerate(dist):
                if d != float("inf") and i != 0:
                    if i in ss:
                        ss.remove(i)

            if cycle == 1:
                self.cycle = cycle
                return
        self.cycle = cycle

    def bf_(self, s=1):
        dist = self.empty_arr(float('inf'))
        prev = self.empty_arr(None)

        dist[s] = 0
        cycle = None
        last = None
        for i in range(1, self.n + 1):
            for u in range(1, self.n + 1):
                for v in self.graph[u]:
                    if dist[v] > dist[u] + self.w[u][v]:
                        dist[v] = dist[u] + self.w[u][v]
                        prev[v] = u
                        if i >= self.n:
                            cycle = 1
                        last = v
            if i >= self.n and cycle != 1:
                cycle = 0

        return cycle if cycle is not None else 0, dist, prev, last

    def bf_shortest_path(self, s=1):
        cycle, dist, prev, last = self.bf_(s)
        self.cycle = cycle
        self.dist = dist
        self.prev = prev
        self.last = last
        if cycle == 1:
            self.detect_cycle()

        for i, d in enumerate(self.dist):
            if i == 0: continue
            if i in self.on_cycle:
                print("-")
            elif d == float('inf'):
                print('*')
            else:
                print(d)

    def detect_cycle(self):
        # Get node on cycle
        x = self.last
        for _ in range(1, self.n + 1):
            x = self.prev[x]
        orig = x
        self.on_cycle.append(orig)
        x = self.prev[x]
        while True:
            if x == orig:
                break
            self.on_cycle.append(x)
            x = self.prev[x]

        # Find all nodes reachable from cycle
        updated = False
        while True:
            if not updated:
                break
            updated = False
            for u in self.on_cycle:
                for v in self.graph[u]:
                    if v in self.on_cycle:
                        continue
                    else:
                        self.on_cycle.append(v)
                        updated = True



if __name__ == '__main__':
    # n - number of vertices
    # m - number of edges
    n, m = list(map(int, input().split(" ")))
    g, w = read_nodes_stdin_directed(n, m)
    s = int(input())
    graph = Graph(n, g, w)
    # print(graph.bf_())
    graph.bf_shortest_path(s)

    # g1 = [(1, 2, 10), (2, 3, 5), (1, 3, 100), (3, 5, 7), (5, 4, 10),
    #       (4, 3, -18), (6, 1, -1)]
    # n1 = 6
    # s1 = 1
    #
    # g2 = [(1, 2, -5), (4, 1, 2), (2, 3, 2), (3, 1, 1)]
    # n2 = 4
    # s2 = 4
    #
    # g3 = [(1, 2, 1), (4, 1, 2), (2, 3, 2), (3, 1, -5)]
    # n3 = 5
    # s3 = 4
    #
    # g4 = [(1, 2, 4), (1, 3, 2), (2, 3, 2), (3, 2, 1), (2, 4, 2), (3, 5, 4),
    #       (5, 4, 1), (2, 5, 3), (3, 4, 4)]
    # n4 = 5
    # s4 = 1
    #
    # g5 = [(1, 2, -1), (2, 3, 1)]
    # n5 = 3
    # s5 = 1
    #
    # g6 = [(1, 2, 4), (1, 3, 2), (2, 3, 2), (3, 2, 1), (2, 4, 2), (3, 5, 4),
    #       (5, 4, 1), (2, 5, 3), (3, 4, 4)]
    # n6 = 5
    # s6 = 1
    #
    # g7 = [(1, 2, 7), (1, 3, 5), (2, 3, 2)]
    # n7 = 3
    # s7 = 1
    #
    # g8 = [(1, 2, 1), (4, 1, 2), (2, 3, 2), (1, 3, 5)]
    # n8 = 4
    # s8 = 1
    #
    # g9 = [(1, 2, 4), (1, 5, 3), (3, 2, 4), (2, 5, -2), (3, 4, 2), (5, 3, -3),
    #       (5, 4, 1)]
    # n9 = 5
    # s9 = 1
    #
    # g10 = [(1, 2, 1), (1, 4, 2), (2, 3, 2), (3, 1, -5)]
    # n10 = 5
    # s10 = 1
    #
    # g11 = [(1, 2, 1), (4, 1, 2), (2, 3, 2), (3, 1, -5)]
    # n11 = 5
    # s11 = 1
    #
    # for (g, n, s) in [
    #     (g1, n1, s1),
    #     (g2, n2, s2),
    #     (g3, n3, s3),
    #     (g4, n4, s4),
    #     (g5, n5, s5),
    #     (g6, n6, s6),
    #     (g7, n7, s7),
    #     (g8, n8, s8),
    #     (g9, n9, s9),
    #     # (g10, n10, s10),
    #     # (g11, n11, s11),
    # ]:
    #     graph = Graph(n, *read_nodes_directed(n, g))
    #     graph.print_graph()
    #     graph.bf_shortest_path(s)
    #     print("dist: ", graph.dist)
    #     print("prev: ", graph.prev)
    #     print("cycle: ", graph.cycle)
    #     print("last: ", graph.last)
    #     print("start: ", s)
    #     print("on_cycle: ", graph.on_cycle)
    #
    #     print()
