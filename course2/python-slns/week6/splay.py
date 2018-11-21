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


class Tree:
    def __init__(self):
        self.k = []
        self.l = []
        self.r = []
        self.p = []
        self.root = 0

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

    def add(self, k):
        self.add_(k)
        self.find(k)

    def add_(self, k):
        if len(self.k) == 0:
            self.k = [k]
            self.l = [-1]
            self.r = [-1]
            self.p = [-1]
            return

        p = self.find_(k, self.root)

        if self.k[p] == k:
            return
        elif k < self.k[p]:
            self.k.append(k)
            self.l.append(-1)
            self.r.append(-1)
            self.p.append(p)
            self.l[p] = len(self.k) - 1

        elif k > self.k[p]:
            self.k.append(k)
            self.l.append(-1)
            self.r.append(-1)
            self.p.append(p)
            self.r[p] = len(self.k) - 1

    def find(self, k):
        node = self.find_(k, self.root)
        self.splay(node)
        return node

    def find_(self, k, i):
        if self.k[i] == -1:
            return 0

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

    def update_parent(self, i, p):
        self.p[i] = p

    def update_left(self, i, l):
        self.l[i] = l

    def update_right(self, i, r):
        self.r[i] = r

    def splay(self, i):
        if self.root == i:
            return
        if self.zig(i):
            pass
        elif self.zig_zag(i): # TODO: FIX ZIGZAG
            pass
        elif self.zig_zig(i):
            pass
        # else:
        #     raise RuntimeError("No conditions met in splay")
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
            self.update_left(gp, r_i)
            # self.l[gp] = self.r[i]  # Left of grandparent = right of i
            self.update_parent(r_i, gp)
            # self.p[self.r[i]] = gp  # Update subtree to new parent

            self.update_right(i, gp)
            # self.r[i] = gp  # Right of node = grandparent
            self.update_parent(i, p_gp)
            # self.p[i] = self.p[gp]  # Update parent of node
            self.update_left(p_gp, i)
            # self.l[self.p[gp]] = i  # Update left of parent of grandparent
            self.update_parent(p_gp, i)
            # self.p[gp] = i  # Parent of gradeparent is now node

            self.update_parent(gp, i)
            self.update_right(p, l_i)
            # self.r[p] = self.l[i]  # Update right of parent to left of node
            self.update_left(i, p)
            # self.l[i] = p  # Update left of node
            self.update_parent(p, i)
            # self.p[p] = i  # Update parent of parent to be node

            self._update_r_l_gp(l_p_gp, r_p_gp, p_gp, gp, i)

            return True

        elif l_p == i and r_gp == p:
            self.update_right(gp, l_i)
            # self.r[gp] = self.l[i]  # Left of grandparent = right of i
            self.update_parent(l_i, gp)
            # self.p[self.l[i]] = gp  # Update subtree to new parent
            self.update_left(i, gp)
            # self.l[i] = gp  # Right of node = grandparent
            self.update_parent(i, p_gp)
            # self.p[i] = self.p[gp]  # Update parent of node
            self.update_right(p_gp, i)
            # self.r[self.p[gp]] = i  # Update left of parent of grandparent
            self.update_parent(gp, i)
            # self.p[gp] = i  # Parent of gradeparent is now node

            self.update_parent(gp, i)
            self.update_left(p, r_i)
            # self.l[p] = self.r[i]  # Update right of parent to left of node
            self.update_right(i, p)
            # self.r[i] = p  # Update left of node
            self.update_parent(p, i)
            # self.p[p] = i  # Update parent of parent to be node

            self._update_r_l_gp(l_p_gp, r_p_gp, p_gp, gp, i)
            return True
        return False


def main():
    t = Tree()
    # for i in [5, 3, 6, 4]:
    for i in range(0, 10):
        t.add(i)
    t.print_by_level()
    t.find(4)
    t.print_by_level()
    t.find(6)
    t.print_by_level()
    t.find(8)
    t.print_by_level()


threading.Thread(target=main).start()
