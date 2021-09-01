""
def binarySearch1(searchFor, numbers = []):
    maxRange = len(numbers) - 1
    minRange = 0
    while True:
        midpoint = int((maxRange + minRange)/2)
        if numbers[midpoint] < searchFor and numbers[midpoint + 1] >= searchFor:
            return len(numbers) - midpoint - 1
        if numbers[midpoint] < searchFor:
            minRange = midpoint + 1
        else:
            maxRange = midpoint - 1
   
        
N = int(input())
A = list(map(int,input().split()))
#for i in range(0, len(inputArray)): 
#    inputArray[i] = int(inputArray[i]) 
A.sort()
testCases = int(input())
for x in range(testCases):
    q_ , x = map(int, input().split())
    if q_ is 0:
        if (A[0] >= x):
            print(len(A))
        elif (A[-1] < x):
            print(0)
        else:
            print(binarySearch1(x, A))
    else:
        if (A[0] > x):
            print(len(A))
        elif (A[-1] <= x):
            print(0)
        else:
            print(binarySearch1(x + 1, A))
        
