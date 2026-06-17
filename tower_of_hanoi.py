def TOH(n,start,end):
    if (n == 1):
        print(start,end)
    else:
        temp = 6-(start+end)
        TOH(n-1,start,temp)
        print(start,end)
        TOH(n-1,temp,end)
print(TOH(3,1,3))


