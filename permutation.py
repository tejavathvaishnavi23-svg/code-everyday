def permutations(arr, ans, indx,visited):
    if indx == len(arr):
        print(ans)
        return

    for i in range(len(arr)):
        if not visited[i]:
            visited[i] = True
            ans[indx] = arr[i]

            permutations(arr,ans, indx+1, visited)
            visited[i] = False
arr = [1, 2, 3]
ans = [0] * len(arr)
visited = [False] * len(arr)
permutations(arr, ans, 0, visited)
