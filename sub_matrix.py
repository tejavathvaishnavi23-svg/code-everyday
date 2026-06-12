#How many submatrices (1,2) is present
def sum_of_all_submatrices(mat):
    total = 0

    N = len(mat) #no.of rows
    M = len(mat[0]) #no.of columns

    for i in range(N):
        for j in range(M):
        #top-left choice
            TL = (i+1)*(j+1)

        #Bottoms-right choice
            BR = (N-i)*(M-j)

        #number of submatrices containing mat[i][j]
            occ = TL * BR

        #contribution of mat[i][j]
            total += mat[i][i] * occ
    return total
mat =[
    [1,2],
    [3,4]
]
print(sum_of_all_submatrices(mat))