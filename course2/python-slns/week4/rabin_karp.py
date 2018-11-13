# python3
# import random

""" Constraints


1 <= |P| <= |T| <= 5 * 10 ^ 5


"""


def read_input():
    return (input().rstrip(), input().rstrip())


def print_occurrences(output):
    print(' '.join(map(str, output)))


def get_occurrences(pattern, text):
    return [
        i
        for i in range(len(text) - len(pattern) + 1)
        if text[i:i + len(pattern)] == pattern
    ]


class RabinKarp(object):
    _x = 263
    _p = 1000000007

    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._x + ord(c)) % self._p
        return ans

    def precompute_hashes(self, t, p):
        l_p = len(p)
        l_t = len(t)
        h = [None] * (l_t - l_p + 1)
        s = t[l_t - l_p: l_t]
        h[l_t - l_p] = self._hash_func(s)
        y = 1
        for i in range(0, l_p):
            tmp = y * self._x
            y = ((tmp % self._p) + self._p) % self._p
        for i in range(0, l_t - l_p)[::-1]:
            h[i] = (self._x * h[i+1] + ord(t[i]) - y * ord(t[i + l_p])) % \
                   self._p
        return h

    def compute(self, t, p):
        results = []
        phash = self._hash_func(p)
        h = self.precompute_hashes(t, p)
        l_t = len(t)
        l_p = len(p)
        for i in range(0, l_t-l_p+1):
            if phash != h[i]:
                continue
            if t[i: i + l_p] == p:
                results.append(i)
        return results


if __name__ == '__main__':
    p, t = read_input()
    rk = RabinKarp()
    results = rk.compute(t, p)
    for r in results:
        print(r, end=' ')
    # p = 'aba'
    # t = 'abacaba'

    # p = 'Test'
    # t = 'testTesttesT'

    # p = 'aaaaa'
    # t = 'baaaaaaa'

    # import string
    # import random
    # for _ in range(100):
    #     t = ''.join(random.choices(string.ascii_lowercase, k=100000))
    #     p = ''.join(random.choices(string.ascii_lowercase, k=2))
    #
    #     rk = RabinKarp()
    #     results = rk.compute(t, p)
    #     results_naive = get_occurrences(p, t)
    #     # print(results == results_naive)
    #     print(t)
    #     print(p)
    #     print(results)
    #     print(results_naive)
    #     print()
    #     if results != results_naive:
    #         print('FAIL')
    #         print(results)
    #         print(results_naive)
    #
    #

