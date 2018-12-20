def fibonacci(n):
    a = 0
    b = 1
    c = None

    for i in range(1, n):
        i += 1
        c = a + b
        a = b
        b = c
    return c
