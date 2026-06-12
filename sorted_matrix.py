#2D array
#Given rowwise and columnwise sorted matrix[N][N], find K.
def sorted_matrix(mat,key):
    rows = len(mat)
    cols = len(mat[0])
    r = 0
    c = cols - 1
    while r < rows and c >= 0:
        if mat[r][c] == key:
            return True
        elif mat[r][c] < key:
            r+=1
        else:
            c-=1
    return False
mat = [
    [10, 20, 30, 40],
    [15, 25, 35, 45],
    [27, 29, 37, 48],
    [32, 33, 39, 50]
]
key = 29
print(sorted_matrix(mat, key))