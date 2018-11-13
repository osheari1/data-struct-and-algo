# python3
# import random

""" Constraints

1 <= N <= 10^5 -> number of queries
N / 5 <= m <= N -> number of buckets
len(input) <= 15


functions:
add string
del string
find string - 'yes' or 'no'
check i - output content of ith list in table



"""


class Query:
    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]


class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        # store all strings in one list
        self.elems = []

    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    def write_search_result(self, was_found):
        # print('yes' if was_found else 'no')
        return 'yes' if was_found else 'no'

    def write_chain(self, chain):
        # print(' '.join(chain))
        return ' '.join(chain)

    def read_query(self):
        return Query(input().split())

    def process_query(self, query):
        if query.type == "check":
            # use reverse order, because we append strings to the end
            return self.write_chain(cur for cur in reversed(self.elems)
                                    if self._hash_func(cur) == query.ind)
        else:
            try:
                ind = self.elems.index(query.s)
            except ValueError:
                ind = -1
            if query.type == 'find':
                return self.write_search_result(ind != -1)
            elif query.type == 'add':
                if ind == -1:
                    self.elems.append(query.s)
            else:
                if ind != -1:
                    self.elems.pop(ind)

    def process_queries_stdin(self):
        n = int(input())
        for i in range(n):
            self.process_query(self.read_query())

    def process_queries(self, queries):
        results = []
        for q in queries:
            q = Query(q)
            r = self.process_query(q)
            if r is not None:
                results.append(r)
        return results


class Set(object):
    def __init__(self, m):
        self.m = m
        self.h = self.hash_fnc()
        self.arr = [[] for _ in range(m)]

    def hash_fnc(self):
        p = 1000000007
        x = 263

        def h(s):
            ans = 0
            for s_i in reversed(s):
                ans = (x * ans + ord(s_i)) % p
            return ans % self.m

        return h

    def process(self, queries):
        result = []
        for q in queries:
            if q[0] == 'add':
                self.add(q[1])
            elif q[0] == 'find':
                result.append(self.find(q[1]))
            elif q[0] == 'del':
                self.delete(q[1])
            else:
                result.append(self.check(q[1]))
        return result

    def add(self, s):
        l = self.arr[self.h(s)]
        if s in l:
            return
        l.append(s)

    def find(self, s):
        l = self.arr[self.h(s)]
        if s in l:
            return 'yes'
        return 'no'

    def delete(self, s):
        if self.find(s) == 'no':
            return
        l = self.arr[self.h(s)]
        l.remove(s)

    def check(self, i):
        l = self.arr[int(i)]
        if len(l) == 0:
            return ""
        return ' '.join(l[::-1])


def read_queries_stdin():
    n = int(input())
    output = []
    for i in range(n):
        val = input().split()
        output.append(val)
    return output


if __name__ == '__main__':
    bucket_count = int(input())
    hs = Set(bucket_count)
    queries = read_queries_stdin()
    for r in hs.process(queries):
        print(r)

    # import numpy as np
    # import string

    # m = 3
    # n = 12
    # queries = [
    #     ("check", '0'),
    #     ("find", 'help'),
    #     ("add", 'help'),
    #     ("add", 'del'),
    #     ("add", 'add'),
    #     ("find", 'add'),
    #     ("find", 'del'),
    #     ("del", 'del'),
    #     ("find", 'del'),
    #     ("check", '0'),
    #     ("check", '1'),
    #     ("check", '2'),
    # ]

    # m = 4
    # n = 8
    # queries = [
    #     ("add", 'test'),
    #     ("add", 'test'),
    #     ("find", 'test'),
    #     ("del", 'test'),
    #     ("find", 'test'),
    #     ("find", 'Test'),
    #     ("add", 'Test'),
    #     ("find", 'Test'),
    # ]

    # m = 5
    # n = 12
    # queries = [
    #     ("add", 'world'),
    #     ("add", 'HellO'),
    #     ("check", '4'),
    #     ("find", 'World'),
    #     ("find", 'world'),
    #     ("del", 'world'),
    #     ("check", '4'),
    #     ("del", 'HellO'),
    #     ("add", 'luck'),
    #     ("add", 'GooD'),
    #     ("check", '2'),
    #     ("del", 'good'),
    # ]

    # for _ in range(100):
    #     q = 1000
    #     m = q // 2 + q // 4
    #     queries = []
    #     types = ['add', 'find', 'del', 'check']
    #     for i in range(q):
    #         t = random.choice(types)
    #         if t == 'check':
    #             v = str(random.choice(range(m)))
    #         else:
    #             v = ''.join(random.choices(string.ascii_letters, k=4))
    #         queries.append((t, v))
    #
    #     hs = Set(m)
    #     hs_naive = QueryProcessor(m)
    #     # print(hs.h('test'))
    #     # print(hs.arr)
    #     results = hs.process(queries)
    #     results_naive = hs_naive.process_queries(queries)
    #     print(_)
    #     if results != results_naive:
    #         print("FAIL")
    #         print(results)
    #         print(results_naive)
    #         break
