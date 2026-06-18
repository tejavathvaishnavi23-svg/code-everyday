def printvalidpar(N, open, close, string):

    if open == N and close == N:
        print(string)
        return

    if open < N:
        printvalidpar(N, open+1, close, string+'(')

    if close < open:
        printvalidpar(N, open, close+1, string+')')
N = 2
printvalidpar(N, 0, 0, "")