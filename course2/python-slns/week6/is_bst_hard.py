# python3

import sys, threading
from queue import LifoQueue

sys.setrecursionlimit(10 ** 7)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size

""" Constraints
duplicate keys are always to the right
0 <= n <= 10^5
-2^31 < key <2^31 - 1
-1 <= left_i, right_i <= n-1

"""


class Tree:
    def read_stdin(self):
        self.n = int(sys.stdin.readline())
        self.key = [0 for i in range(self.n)]
        self.left = [0 for i in range(self.n)]
        self.right = [0 for i in range(self.n)]
        for i in range(self.n):
            [a, b, c] = map(int, sys.stdin.readline().split())
            self.key[i] = a
            self.left[i] = b
            self.right[i] = c

    def read(self, key, left, right):
        self.n = len(key)
        self.key = key
        self.left = left
        self.right = right

    def is_correct(self):
        mr = [float("-inf")]
        correct = ['CORRECT']

        if self.n == 0:
            return 'CORRECT'

        def go(i):
            if self.left[i] != -1:
                # print(self.key[self.left[i]], self.key[i])
                if self.key[self.left[i]] >= self.key[i]:
                    correct[0] = "INCORRECT"
                    return
                go(self.left[i])

            if self.key[i] < mr[0]:
                correct[0] = 'INCORRECT'
                return
            mr[0] = max(self.key[i], mr[0])

            if self.right[i] != -1:
                if self.key[self.right[i]] < self.key[i]:
                    correct[0] = 'INCORRECT'
                    return
                go(self.right[i])

        go(0)
        return correct[0]


def main():
    tree = Tree()
    tree.read_stdin()
    print(tree.is_correct())

    # # CORRECT
    # key = [2, 1, 3]
    # left = [1, -1, -1]
    # right = [2, -1, -1]
    #
    # # INCORRECT
    # key1 = [1, 2, 3]
    # left1 = [1, -1, -1]
    # right1 = [2, -1, -1]
    #
    # # CORRECT
    # key2 = [2, 1, 2]
    # left2 = [1, -1, -1]
    # right2 = [2, -1, -1]
    #
    # # INCORRECT
    # key3 = [2, 2, 3]
    # left3 = [1, -1, -1]
    # right3 = [2, -1, -1]
    #
    # # CORRECT
    # key4 = [1, 2, 3, 4, 5]
    # left4 = [-1, -1, -1, -1, -1]
    # right4 = [1, 2, 3, 4, -1]
    #
    # # CORRECT
    # key5 = [4, 2, 6, 1, 3, 5, 7]
    # left5 = [1, 3, 5, -1, -1, -1, -1]
    # right5 = [2, 4, 6, -1, -1, -1, -1]
    #
    # for (k, l, r) in [
    #     [key, left, right],
    #     [key1, left1, right1],
    #     [key2, left2, right2],
    #     [key3, left3, right3],
    #     [key4, left4, right4],
    #     [key5, left5, right5],
    # ]:
    #     tree = Tree()
    #     tree.read(k, l, r)
    #     # tree.read_stdin()
    #     print(tree.is_correct())


threading.Thread(target=main).start()
