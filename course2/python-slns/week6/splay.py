# python3

import queue

import sys, threading
from copy import deepcopy

sys.setrecursionlimit(10 ** 7)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size

""" Constraints
0 <= n <= 10^5
-2^31 < key <2^31 - 1
-1 <= left_i, right_i <= n-1

"""


class Tree2:
    def __init__(self):
        self.m = 1000000001
        self.last_sum = 0
        self.k = []
        self.l = []
        self.r = []
        self.p = []
        self.d = []
        self.root = 0

    def to_mod(self, x):
        return (x + self.last_sum) % self.m

    def read(self, inp):
        results = []
        for _, s in enumerate(inp):
            c = s[0]
            v = s[1:]
            print(c, v, end=" ")
            if c == "+":
                self.add_mod(v[0])
                print()
            elif c == "-":
                self.delete_mod(v[0])
                print()
            elif c == "?":
                if len(self.k) == 0:
                    results.append("Not found")
                    print(results[-1])
                    continue
                f = self.find_mod(v[0])
                if f == -1 or self.deleted(f) or self.k[f] != self.to_mod(v[0]):
                    results.append("Not found")
                else:
                    results.append("Found")
                print(results[-1])
            elif c == "s":
                results.append(self.sum_mod(v[0], v[1]))
                print(results[-1])

        for r in results:
            print(r)

    def read_stdin(self):
        n = int(input())
        results = []
        for _ in range(n):
            i = input().split(" ")
            c = i[0]
            v = list(map(int, i[1:]))
            if c == "+":
                self.add_mod(v[0])
            elif c == "-":
                self.delete_mod(v[0])
            elif c == "?":
                if len(self.k) == 0:
                    results.append("Not found")
                    continue
                f = self.find_mod(v[0])
                if f == -1 or self.deleted(f) or self.k[f] != self.to_mod(v[0]):
                    results.append("Not found")
                else:
                    results.append("Found")
            elif c == "s":
                results.append(self.sum_mod(v[0], v[1]))

        for r in results:
            print(r)

    def deleted(self, i):
        return self.d[i]

    def has_left(self, i):
        return self.l[i] != -1

    def has_right(self, i):
        return self.r[i] != -1

    def print_by_level(self):
        def go(i):
            q = queue.Queue()
            q.put_nowait((i, 0))
            while not q.empty():
                node, ind = q.get_nowait()
                print("".join(["\t"] * ind) + str(self.k[node]))
                if self.has_right(node):
                    q.put_nowait((self.r[node], ind + 1))
                if self.has_left(node):
                    q.put_nowait((self.l[node], ind + 1))

        go(self.root)

    def print_in_order(self):
        def go(i):
            if self.has_left(i):
                go(self.l[i])
            print(self.k[i])
            if self.has_right(i):
                go(self.r[i])

        go(self.root)

    def sum_mod(self, l, r):
        return self.sum((l + self.last_sum) % self.m,
                        (r + self.last_sum) % self.m)

    def sum(self, l, r):
        i = self.find(l)
        if i == -1:
            return 0
        s = self.k[i]
        while self.k[i] <= r:
            i = self.next(i)
            if i == -1:
                break
            if self.k[i] >= l:
                s += self.k[i]
            if self.k[i] >= r:
                break
        self.last_sum = s
        return s

    def add_mod(self, k):
        self.add((k + self.last_sum) % self.m)

    def delete_mod(self, k):
        self.delete((k + self.last_sum) % self.m)

    def find_mod(self, k):
        return self.find((k + self.last_sum) % self.m)

    def add(self, k):
        self.add_(k)
        self.find(k)

    def add_(self, k):
        if len(self.k) == 0:
            self.k = [k]
            self.l = [-1]
            self.r = [-1]
            self.p = [-1]
            self.d = [False]
            return

        p = self.find_(k, self.root)

        if p == -1:  # Previously nodes existed but don't anymore
            self.k.append(k)
            self.l.append(-1)
            self.r.append(-1)
            self.p.append(-1)
            self.d.append(False)
            self.root = len(self.k) - 1

        elif self.k[p] == k:
            return
        elif k < self.k[p]:
            self.k.append(k)
            self.l.append(-1)
            self.r.append(-1)
            self.p.append(p)
            self.d.append(False)
            self.l[p] = len(self.k) - 1

        elif k > self.k[p]:
            self.k.append(k)
            self.l.append(-1)
            self.r.append(-1)
            self.p.append(p)
            self.d.append(False)
            self.r[p] = len(self.k) - 1

    def find(self, k):
        node = self.find_(k, self.root)
        self.splay(node)
        return node

    def find_(self, k, i):
        if len(self.k) == 0 or self.deleted(i):
            return -1

        if self.k[i] == k:
            return i

        if k < self.k[i]:
            if self.has_left(i):
                return self.find_(k, self.l[i])
            else:
                return i

        if k > self.k[i]:
            if self.has_right(i):
                return self.find_(k, self.r[i])
            else:
                return i

    def delete(self, k):
        # Don't try to delete if already deleted
        # Find without splaying
        i = self.find_(k, self.root)
        self.delete_(i)

    def delete_(self, i):
        if i == -1:
            return
        # IF does not have right, remove node and promote left subtree to
        # original location
        if not self.has_right(i):
            l_i = self.l[i]
            p_i = self.p[i]
            # Promote left subtree
            self.update_parent(l_i, p_i)
            # If i was in the right of its parent, update right else update left
            self.update_left_or_right(i, l_i, p_i)
            # Fill in p, l, r with -1
            self._remove_node(i)

            if self.root == i:
                self.root = l_i
        else:
            # self.l[x] == -1 by definition
            x = self.next(i)
            r_x = self.r[x]
            p_x = self.p[x]

            r_i = self.r[i]
            l_i = self.l[i]
            p_i = self.p[i]

            # Replace x by n
            self.update_left(x, l_i)
            self.update_right(x, r_i)
            self.update_parent(x, p_i)
            self.update_parent(l_i, x)
            self.update_parent(r_i, x)

            if p_i == -1:
                self.root = x

            # Promote right subtree
            self.update_parent(r_x, p_x)
            self.update_left_or_right(x, r_x, p_x)
            self._remove_node(i)

    def _remove_node(self, i):
        self.d[i] = True
        self.update_left(i, -1)
        self.update_right(i, -1)
        self.update_parent(i, -1)

    def next(self, i):
        if self.has_right(i):
            return self.left_desc(self.r[i])
        elif self.has_left(i):
            return self.right_ans(i)
        else:
            return -1

    def left_desc(self, i):
        if not self.has_left(i):
            return i
        return self.left_desc(self.l[i])

    def right_ans(self, i):
        if self.k[i] < self.k[self.p[i]]:
            return self.p[i]
        return self.right_ans(self.p[i])

    def update_parent(self, i, p):
        if i == -1:
            return
        self.p[i] = p

    def update_left(self, i, l):
        if i == -1:
            return
        self.l[i] = l

    def update_right(self, i, r):
        if i == -1:
            return
        self.r[i] = r

    def update_left_or_right(self, x, i, p):
        if x == self.r[p]:
            self.update_right(p, i)
        elif x == self.l[p]:
            self.update_left(p, i)

    def splay(self, i):
        if self.root == i or i == -1 or len(self.k) == 0:
            return
        if self.zig(i):
            pass
        elif self.zig_zag(i):
            pass
        elif self.zig_zig(i):
            pass
        else:
            raise RuntimeError("No conditions met in splay")
        self.splay(i)

    def zig(self, i):
        # Parent must be root node
        p = self.p[i]
        l_i = self.l[i]
        r_i = self.r[i]
        # l_p = self.l[p]
        # r_p = self.r[p]
        # p_p = self.p[p]

        if p != self.root:
            return False
        # When node is in right subtree
        if self.r[p] == i:
            self.update_parent(l_i, p)
            self.update_right(p, l_i)

            self.update_parent(i, -1)
            self.update_left(i, p)
            self.update_parent(p, i)

            self.root = i

        elif self.l[p] == i:
            self.update_parent(r_i, p)
            self.update_left(p, r_i)

            self.update_parent(i, -1)
            self.update_right(i, p)
            self.update_parent(p, i)
            self.root = i

        return True

    def _update_r_l_gp(self, l_p_gp, r_p_gp, p_gp, gp, i):
        if gp == self.root:
            self.root = i
            self.update_parent(i, -1)
            return
        if l_p_gp == gp:
            self.update_left(p_gp, i)
        elif r_p_gp == gp:
            self.update_right(p_gp, i)

    def zig_zig(self, i):
        p = self.p[i]
        gp = self.p[p]
        p_gp = self.p[gp]
        r_p_gp = self.r[p_gp]
        l_p_gp = self.l[p_gp]
        l_i = self.l[i]
        r_i = self.r[i]
        l_p = self.l[p]
        r_p = self.r[p]
        l_gp = self.l[gp]
        r_gp = self.r[gp]

        if l_p == i and l_gp == p:
            self.update_parent(r_i, p)
            self.update_right(i, p)
            self.update_left(p, r_i)
            self.update_parent(p, i)

            self.update_parent(r_p, gp)
            self.update_right(p, gp)
            self.update_left(gp, r_p)
            self.update_parent(gp, p)

            self.update_parent(i, p_gp)
            # update parent of grandparent
            self._update_r_l_gp(l_p_gp, r_p_gp, p_gp, gp, i)
            return True

        elif r_p == i and r_gp == p:
            self.update_parent(l_i, p)
            self.update_left(i, p)
            self.update_right(p, l_i)
            self.update_parent(p, i)

            self.update_parent(l_p, gp)
            self.update_left(p, gp)
            self.update_right(gp, l_p)
            self.update_parent(gp, p)

            self.update_parent(i, p_gp)
            # update parent of grandparent
            self._update_r_l_gp(l_p_gp, r_p_gp, p_gp, gp, i)
            return True
        return False

    def zig_zag(self, i):
        p = self.p[i]
        gp = self.p[p]
        p_gp = self.p[gp]
        r_p_gp = self.r[p_gp]
        l_p_gp = self.l[p_gp]
        l_i = self.l[i]
        r_i = self.r[i]
        l_p = self.l[p]
        r_p = self.r[p]
        l_gp = self.l[gp]
        r_gp = self.r[gp]

        if r_p == i and l_gp == p:

            self.update_left(i, p)
            self.update_left(gp, r_i)

            self.update_right(p, l_i)
            self.update_right(i, gp)

            self.update_parent(l_i, p)
            self.update_parent(r_i, gp)
            self.update_parent(i, p_gp)
            self.update_parent(p, i)
            self.update_parent(gp, i)

            self._update_r_l_gp(l_p_gp, r_p_gp, p_gp, gp, i)

            return True

        elif l_p == i and r_gp == p:
            self.update_right(i, p)
            self.update_right(gp, l_i)

            self.update_left(p, r_i)
            self.update_left(i, gp)

            self.update_parent(r_i, p)
            self.update_parent(l_i, gp)
            self.update_parent(i, p_gp)
            self.update_parent(p, i)
            self.update_parent(gp, i)

            self._update_r_l_gp(l_p_gp, r_p_gp, p_gp, gp, i)
            return True
        return False


def main():
    t = Tree()
    # e = [["+", 491572259], ["?", 491572259], ["?", 899375874],
    #      ["s", 310971296, 877523306], ["+", 352411209]]
    # e = [["?", 0], ["+", 0], ["?", 0], ["-", 0], ["?", 0]]
    # e = [["?", 1], ["+", 1], ["?", 1], ["+", 2], ["s", 1, 2],
    #      ["+", 10 ** 9], ["?", 10 ** 9], ["-", 10 ** 9], ["?", 10 ** 9],
    #      ["s", 10 ** 9 - 1, 10 ** 9], ["-", 2], ["?", 2], ["-", 0], ["+", 9],
    #      ["s", 0, 9]]
    # t.read(e)
    # t.read_stdin()
    for i in range(0, 100):
        t.add_mod(i)
    for i in range(0, 100):
        for j in range(i, 100):
            print(sum(range(t.to_mod(i), t.to_mod(j+1))))
            print(t.sum_mod(i, j))



    # for j in range(0, 100):
    #     t.add(j)
    #     print("t", t.sum_mod(0, j))
    #     print("s", sum(range(0, j+1)))








threading.Thread(target=main).start()
