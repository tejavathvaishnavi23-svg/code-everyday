def spiral_print(mat):
    n = len(mat)
    i,j = 0,0
    while n>1:
    #step-1:Top row(left to right)
          for d in range(n-1):
              print(mat[i][j],end=" ")
              j+=1
    #step-2:Right column(top to bottom)
          for d in range(n-1):
              print(mat[i][j],end=" ")
              i+=1
    #step-3:Bottom row(right to left)
          for d in range(n-1):
              print(mat[i][j],end=" ")
              j-=1
    #step-4:Left column(bottom-top)
          for d in range(n - 1):
              print(mat[i][j], end=" ")
              i-= 1
    #move to inner submatrix
          i += 1
          j += 1
          n -= 2
    #EdgeCase:center element
    if n == 1:
        print(mat[i][j],end=" ")

#input
N=int(input("Enter size of square matrix"))
mat = []
print("Enter matrix elements")
for _ in range(N):
    row = list(map(int,input().split()))
    mat.append(row)

print("Spiral Order")
spiral_print(mat)
