# challenge 1

def sum_to(n):
    total = 0
    i = 0
    while i <= n:
        total = total + i
        print(total)
        i += 1
    return total


sum_to(10)
sum_to(6)

# challenge 2


def largest(lis):
    print(f'largest number:', max(lis))
    return max(lis)


largest([1, 2, 3, 5, 6, 4])

# challenge 3


def occurances(inp1, inp2):
    print(f'occurance count: ', inp1.count(inp2))
    return inp1.count(inp2)


occurances('fleep floop', 'p')
occurances('fleep floop', 'ee')

# challenge 4


def product(*args):
    total = 1
    for arg in args:
        total = total * arg

    print("product", total)


product(2, 5, 5)  # returns 50
product(4, 0.5, 5)  # returns 10.0
