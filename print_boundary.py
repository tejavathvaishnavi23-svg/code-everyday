#Given matrix[N][N] print boundary in clockwise direction.
def print_boundary(mat):
    n = len(mat)
    if n == 1:
        print(mat[0][0])
        return
    #Top row
    for j in range(n):
        print(mat[0][j], end=" ")
    #Right Column
    for i in range(1,n):
        print(mat[i][n-1], end=" ")
    #Bottom row
    for j in range(n-2,-1,-1):
        print(mat[n-1][j], end=" ")
    #Left Column
    for i in range(n-2,0,-1):
        print(mat[i][0], end=" ")

N = int(input())

mat = []
for i in range(N):
    row = list(map(int, input().split()))
    mat.append(row)

print_boundary(mat)


