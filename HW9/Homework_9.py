# 1. Fibonacci sequences using generator
def fib_gen(n):
    fibo_1, fibo_2 = 0, 1
    for _ in range(1, n + 1):
        fibo_1, fibo_2 = fibo_2, fibo_1 + fibo_2
        yield fibo_1


# 2. Fibonacci sequences using iterator
# option a
def fib_iter(n):
    d = []
    fib1, fib2 = 0, 1
    for _ in range(1, n + 1):
        fib1, fib2 = fib2, fib1 + fib2
        d.append(fib1)
    return iter(d)


# option b
class MyIterator:

    def __init__(self, num):
        self.num = num

    def __iter__(self):
        self.fib_1 = 0
        self.fib_2 = 1
        return self

    def __next__(self):
        fib = self.fib_1
        if fib > self.num:
            raise StopIteration
        self.fib_1, self.fib_2 = self.fib_2, self.fib_1 + self.fib_2
        return fib


# 3. Fibonacci sequences using recursion

def fib_rec(n):
    if n <= 1:
        return n
    return fib_rec(n - 1) + fib_rec(n - 2)


# 4. Factorial using recursion
def fact_rec(n):
    if n == 1:
        return 1
    return n * fact_rec(n - 1)
