def zero_queries(n, query):
    arr = [0] * n # initialized to 0

    for i in range(len(query)):
        s = query[i][0]
        e = query[i][1]
        v = query[i][2]

        arr[s] += v
        if e + 1 < n:
            arr[e+1] -= v

    total = 0
    psum = [0] * n

    for i in range(n):
        total += arr[i]
        psum[i] = total

    return psum
n = 7
queries = [
    (2, 5, 7),
    (1, 3, 2),
    (2, 4, 1),
    (3, 6, 2)
]
print(zero_queries(n, queries))
