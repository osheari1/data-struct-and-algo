# python3
import sys, threading

sys.setrecursionlimit(10 ** 6)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size

""" Constraints

1 <= n <= 10^5
0 <= key_i <= 10^9
-1 <= left_i, right_i <= n - 1
if left_i != -1 and right_i != -1 --> left_i != right_i
"""


class TreeOrders:
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
        self.key = key
        self.left = left
        self.right = right

    def inOrder(self):
        result = []

        def go(i: int):
            if self.left[i] != -1:
                go(self.left[i])
            result.append(self.key[i])
            if self.right[i] != -1:
                go(self.right[i])
        go(0)
        return result

    def preOrder(self):
        result = []

        def go(i: int):
            result.append(self.key[i])
            if self.left[i] != -1:
                go(self.left[i])
            if self.right[i] != -1:
                go(self.right[i])

        go(0)
        return result

    def postOrder(self):
        result = []

        def go(i: int):
            if self.left[i] != -1:
                go(self.left[i])
            if self.right[i] != -1:
                go(self.right[i])
            result.append(self.key[i])
        go(0)
        return result


def main():
    # key = [4, 2, 5, 1, 3]
    # left = [1, 3, -1, -1, -1]
    # right = [2, 4, -1, -1, -1]
    #
    # key = list(filter(lambda x: x % 10 == 0, range(100)))
    # left = [7, -1, -1, 8, 3, -1, 1, 5, -1, -1]
    # right = [2, -1, 6, 9, -1, -1, -1, 4, -1, -1]

    tree = TreeOrders()
    # tree.read(key, left, right)
    tree.read_stdin()
    print(" ".join(str(x) for x in tree.inOrder()))
    print(" ".join(str(x) for x in tree.preOrder()))
    print(" ".join(str(x) for x in tree.postOrder()))


threading.Thread(target=main).start()
