# python3

import sys, threading

sys.setrecursionlimit(10 ** 7)  # max depth of recursion
sys.setrecursionlimit(10 ** 7)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size

""" Constraints
0 <= n <= 10^5
-2^31 < key <2^31 - 1
-1 <= left_i, right_i <= n-1
"""


def Node(k):
    n = Node_(k)
    n.p = Node_(None)
    n.r = Node_(None)
    n.l = Node_(None)
    return n


class Node_:

    def __init__(self, k):
        self.k = k

    def __eq__(self, other):
        return self.k == other.k

    def __lt__(self, other):
        return self.k < other.k

    def __gt__(self, other):
        return self.k > other.k

    def __repr__(self):
        s = str(self.k)
        # if self.has_r():
        #     s += "--"
        #     if self.has_p():
        #         s = "\n\t" + s
        # if self.has_l():
        #     s += "   /\\n    /\\"
        return s

    def has_l(self):
        return not self.l.is_empty()

    def has_r(self):
        return not self.r.is_empty()

    def has_p(self):
        return not self.p.is_empty()

    def add_l(self, k):
        n = Node(k)
        n.p = self
        self.l = n

    def add_r(self, k):
        n = Node(k)
        n.p = self
        self.r = n

    def is_empty(self):
        return self.k is None


def r_of_p(n):
    if n.p.has_r():
        return n == n.p.r
    return False


def l_of_p(n):
    if n.p.has_l():
        return n == n.p.l
    return False


class Tree:
    m = 1000000001
    last_sum = 0

    def __init__(self):
        self.root = Node(None)
        # self.n = Node(None)

    def find_mod(self, k):
        self.find((k + self.last_sum) % self.m, self.root)

    def find(self, k, n: Node_):
        if n.is_empty():
            return n

        if n.k == k:
            return n
        elif n.k > k:
            if n.has_l():
                return self.find(k, n.l)
            return n
        elif n.k < k:
            if n.has_r():
                return self.find(k, n.r)
            return n

    def add_mod(self, k):
        self.add((k + self.last_sum) % self.m, self.root)

    def add(self, k, n: Node_):
        p = self.find(k, n)

        # If p is empty replace node with current
        if p.is_empty():
            self.root = Node(k)
        elif p.k > k:
            p.add_l(k)
        else:
            p.add_r(k)

    def delete(self, k):
        # First find node
        n = self.find(k, self.root)

        if self.root == n:
            self.root = Node(None)

        if n.is_empty():
            return
        if not n.has_r():
            if l_of_p(n):
                n.p.l = n.l
                n.l.p = n.p
            elif r_of_p(n):
                n.p.r = n.l
                n.l.p = n.p

    def next(self, n: Node_):
        if n.has_r():
            return self.left_descendant(n.r)
        return self.right_ancestor(n)

    def left_descendant(self, n: Node_):
        if not n.has_l():
            return n
        return self.left_descendant(n.l)

    def right_ancestor(self, n):
        if n < n.p:
            return n.p
        return self.right_ancestor(n.p)


def main():
    t = Tree()
    print(t.root)
    # print(t.find(10, t.root))
    for i in range(5, 10):
        t.add(i, t.root)
    # t.find(9, t.root)
    for i in range(5, 10):
        print(t.find(i, t.root))
    for i in range(5, 10)[::-1]:
        t.delete(i)
        print(t.find(i, t.root))

    # t = Tree()
    # e = [["+", 491572259], ["?", 491572259], ["?", 899375874],
    #      ["s", 310971296, 877523306], ["+", 352411209]]
    # e = [["?", 0], ["+", 0], ["?", 0], ["-", 0], ["?", 0]]
    # e = [["?", 1], ["+", 1], ["?", 1], ["+", 2], ["s", 1, 2],
    #      ["+", 10 ** 9], ["?", 10 ** 9], ["-", 10 ** 9], ["?", 10 ** 9],
    #      ["s", 10 ** 9 - 1, 10 ** 9], ["-", 2], ["?", 2], ["-", 0], ["+", 9],
    #      ["s", 0, 9]]
    # t.read(e)
    # t.read_stdin()
    # for i in range(0, 100):
    #     t.add_mod(i)
    # for i in range(0, 100):
    #     for j in range(i, 100):
    #         print(sum(range(t.to_mod(i), t.to_mod(j + 1))))
    #         print(t.sum_mod(i, j))

    # for j in range(0, 100):
    #     t.add(j)
    #     print("t", t.sum_mod(0, j))
    #     print("s", sum(range(0, j+1)))


threading.Thread(target=main).start()
