# 1. Fibonacci sequences using generator
def fib_gen(n):
    fibo_1, fibo_2 = 0, 1
    for _ in range(1, n + 1):
        fibo_1, fibo_2 = fibo_2, fibo_1 + fibo_2
    return fibo_1


print(fib_gen(int(input())))


# 2. Fibonacci sequences using iterator
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


print(fib_rec(int(input())))


# 4. Factorial using recursion
def fact_rec(n):
    if n == 1:
        return 1
    return n * fact_rec(n - 1)


print(fact_rec(int(input())))
