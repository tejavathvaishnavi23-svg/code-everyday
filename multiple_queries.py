def zero_queries(n, query):
    arr = [0] * n
    q = len(query)
    for i in range(q):
        s = query[i][0]
        v = query[i][1]
        arr[s] = arr[s] + v
    psum = [0] * n
    total = 0
    for i in range(n):
        total += arr[i]
        psum[i] = total
    return psum
n = 7
queries = [
    (2, 6),
    (0, -1),
    (3, 2),
    (5, 4),
    (3, 3)
]
print(zero_queries(n, queries))