# python3
import random

""" Constraints

1 <= N <= 10^5
size of number <= 7
size of name <= 15
name 'not found' doesn't exist



"""


class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]


def read_queries_naive_stdin():
    n = int(input())
    return [Query(input().split()) for i in range(n)]


def read_queries_stdin():
    n = int(input())
    output = []
    for i in range(n):
        val = input().split()
        val[1] = int(val[1])
        output.append(val)
    return output


def read_queries(queries):
    return [Query(q) for q in queries]


def write_responses(result):
    print('\n'.join(result))


def process_queries_naive(queries):
    result = []
    # Keep list of all existing (i.e. not deleted yet) contacts.
    contacts = []
    for cur_query in queries:
        if cur_query.type == 'add':
            # if we already have contact with such number,
            # we should rewrite contact's name
            for contact in contacts:
                if contact.number == cur_query.number:
                    contact.name = cur_query.name
                    break
            else:  # otherwise, just add it
                contacts.append(cur_query)
        elif cur_query.type == 'del':
            for j in range(len(contacts)):
                if contacts[j].number == cur_query.number:
                    contacts.pop(j)
                    break
        else:
            response = 'not found'
            for contact in contacts:
                if contact.number == cur_query.number:
                    response = contact.name
                    break
            result.append(response)
    return result


class HashTable(object):
    def __init__(self, size=10 ** 5):
        self.arr = [None] * size
        # self.arr = [[]] * size
        self.p = 10000019
        self.h = self.hash_fnc_int(
                random.randint(1, self.p - 1),
                random.randint(0, self.p - 1),
                size,
                self.p)

    def process(self, queries):
        result = []
        for q in queries:
            if q[0] == 'add':
                self.add(q[1], q[2])
            elif q[0] == 'find':
                result.append(self.find(q[1]))
            elif q[0] == 'del':
                self.delete(q[1])
            else:
                raise RuntimeError("Query op does not exist %s" % q[0])
        return result

    def add(self, num, name):
        # l = self.arr[self.h(num)]
        self.arr[num - 1] = name

    def delete(self, num):
        self.arr[num - 1] = None

    def find(self, num):
        out = self.arr[num - 1]
        if out is not None:
            return out
        else:
            return "not found"

    def hash_fnc_int(self, a, b, m, p=10000019):
        """
        :param a: random int between 1 and p -1
        :param b: random int between 0 and p-1
        :param m: size of hash table
        :param p: prime number
        :return:
        """
        return lambda x: ((a * x + b) % p) % m


if __name__ == '__main__':
    # queries = [
    #     ('add', 911, 'police'),
    #     ('add', 911, 'police'),
    #     ('add', 76213, 'Mom'),
    #     ('add', 17239, 'Bob'),
    #     ('find', 76213),
    #     ('find', 910),
    #     ('find', 911),
    #     ('del', 910),
    #     ('del', 911),
    #     ('find', 911),
    #     ('find', 76213),
    #     ('add', 76213, 'daddy'),
    #     ('find', 76213)
    # ]
    # output = ["Mom", "not found", "police", "not found", "Mom", "daddy"]
    # queries = [
    #     ('find', 3839442),
    #     ('add', 123456, 'me'),
    #     ('add', 0, 'granny'),
    #     ('find', 0),
    #     ('find', 123456),
    #     ('del', 0),
    #     ('del', 0),
    #     ('find', 0),
    # ]
    # output = ["not found", "granny", "me", "not found"]

    # import numpy as np
    # import string
    # q = 100000
    # queries = []
    # types = ['add', 'find', 'del']
    # for i in range(q):
    #     queries.append(
    #             (
    #                 random.choice(types),
    #                 random.randint(1, 10 ** 7),
    #                 ''.join(random.choices(string.ascii_letters, k=15))
    #             )
    #     )

    queries = read_queries_stdin()
    ht = HashTable(10 ** 7)
    results = ht.process(queries)
    for r in results:
        print(r)
    # results_naive = process_queries_naive(read_queries(queries))

    # for a, b in zip(results, results_naive):
    #     print(a)
    #     print(b)
    #     if a != b:
    #         print('FAIL')
