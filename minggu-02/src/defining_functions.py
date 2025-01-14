# Praktik 1
def fib(n):  # write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()


# Now call the funtion we just defined:
fib(2000)

# Praktik 2
fib
f = fib
f(100)

# Praktik 3
fib(0)
print(fib(0))

# Praktik 4


def fib2(n):  # return Fibonacci series up to n
    """Return a list containing the Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)    # see below
        a, b = b, a+b
    return result


f100 = fib2(100)    # call it
f100                # write the result
