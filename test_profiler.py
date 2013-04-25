import time

@profile
def sum_in_memory(n):
    sum(range(n))

@profile
def sum_generator(n):
    sum(xrange(n))

if __name__ == "__main__":
    n = 1000000

    sum_in_memory(n)

    time.sleep(10)

    sum_generator(n)
