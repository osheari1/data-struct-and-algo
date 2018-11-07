# python3

"""Constraints

1 <= n, m <= 100 000
0 <= ri <= 10000
1 <= destination_i , source_i <= n
"""

import sys
from copy import deepcopy
import random


# noinspection PyAttributeOutsideInit,SpellCheckingInspection
class TableMerge(object):
    def read_std(self):
        self.n, self.m = map(int, sys.stdin.readline().split())
        self.rank = list(map(int, sys.stdin.readline().split()))
        self.heights = deepcopy(self.rank)
        self.d_s = []
        for _ in range(self.m):
            d_s = list(map(int, sys.stdin.readline().split()))
            self.d_s.append((d_s[0] - 1, d_s[1] - 1))

    def read(self, n, m, lines, d_s):
        self.n, self.m = n, m
        self.rank = lines
        self.heights = deepcopy(self.rank)
        self.d_s = d_s

    def find(self, i):
        if i != self.parent[i]:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        i_id = self.find(i)
        j_id = self.find(j)
        if i_id == j_id:
            return i_id
        if self.rank[i_id] > self.rank[j_id]:
            self.parent[j_id] = i_id
            self.heights[i_id] += self.heights[j_id]
            return i_id
        else:
            self.parent[i_id] = j_id
            self.heights[j_id] += self.heights[i_id]
            if self.rank[j_id] == self.rank[i_id]:
                self.rank[j_id] += 1
            return j_id

    def solve(self, p=False):
        self.parent = list(range(self.n))
        # self.rank = [1] * self.n
        self.ans = max(self.rank)

        # print(self.parent)
        # print(self.ans)
        for d, s in self.d_s:
            self.merge(d, s)
            # print(self.parent)
            # print(self.rank)
            if p:
                print(self.ans)

    def merge(self, dest, source):
        # p_dest = self.find(dest)
        # p_source = self.find(source)
        p_dest = dest
        p_source = source
        if p_dest == p_source:
            return
        p_new = self.union(p_source, p_dest)
        if self.ans < self.heights[p_new]:
            self.ans = self.heights[p_new]
        pass

        # print(self.parent)
        # print(self.rank)
        # print()

        # self.rank[p_dest] += self.rank[p_source]
        # self.parent[source] = p_dest
        # if self.rank[p_dest] > self.ans:
        #     self.ans = self.rank[p_dest]

        # for n in self.parent:
        #     self.compress_path(n)

        # print(self.parent)
        # print(self.rank)

    # def compress_path(self, node):
    #     if self.parent[node] == node:
    #         return
    #     nodes = []
    #     p = node
    #     while True:
    #         # p = self.parent[p]
    #         if p == self.parent[p]:
    #             root = p
    #             break
    #         nodes.append(p)
    #         p = self.parent[p]
    #     self.parent = list(map(lambda x:
    #                            root if x in nodes else x, self.parent))


if __name__ == "__main__":

    # n, m = 5, 5  # n tables m merges
    # lines = [1, 1, 1, 1, 1]
    # d_s = [(x[0] - 1, x[1] - 1) for x in
    #        [(3, 5), (2, 4), (1, 4), (5, 4), (5, 3)]]

    # n, m = 6, 4  # n tables m merges
    # lines = [10, 0, 5, 0, 3, 3]
    # d_s = [(x[0] - 1, x[1] - 1) for x in [(6, 6), (6, 5), (5, 4), (4, 3)]]

    # n, m = 100000, 100000
    # r = 10000
    # lines = [random.randint(0, r) for _ in range(n)]
    # d_s = [(random.randint(0, n - 1), random.randint(0, n - 1)) for _ in
    #        range(m)]
    # merge = TableMerge()
    # merge.read(n, m, lines, d_s)
    # merge.solve(True)

    merge = TableMerge()
    merge.read_std()
    merge.solve(True)
