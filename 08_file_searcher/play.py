# 5! = 120:
#
# 5 * 4 * 3 * 2 * 1

# Example of a Recursive Algorithm

def factorial(n):
    if n == 1:
        return 1

    return n * factorial(n - 1)  # a recursive technique where a function calls itself


print("5! = {:,}, 3! = {:,}, 11! = {:,}".format(
    factorial(5),  # = 120
    factorial(3),  # = 6
    factorial(11)  # some HUGE number
))


# Fibonacci sequence
# 1, 1, 2, 3, 5, 8, 13, ...

def fibonacci(limit):
    nums = []

    current = 0
    next = 1

    while current < limit:
        current, next = next, next + current
        nums.append(current)

    return nums


# print(fibonacci(100))
for n in fibonacci(100):
    print(n, end=', ')
