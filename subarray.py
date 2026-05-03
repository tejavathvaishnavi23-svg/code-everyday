#Generate all subarrays
arr = [1,2,3]
n = len(arr)
total = n*(n+1)//2
print(total)

#print only size 2 subarrays
arr = [4,5,6,7]
for i in range (len(arr)):
    for j in range (i,len(arr)):
        if j-i+1 == 2:
            print(arr[i:j+1])

#find sum of each subarray
arr = [1,2]
for i in range(len(arr)):
    for j in range (i,len(arr)):
        sub = arr[i:j+1]
        print(sub,"sum=",sum(sub))