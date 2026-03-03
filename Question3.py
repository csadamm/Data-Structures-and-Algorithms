'''
A is an array of n distinct elements
An element A[i] is called extreme if:

    A[i] is not the first nor the last element of A
    i.e A[i] is not A[0] nor A[n]
    Hence, 0 < i < n-1 and either 
    A[i-1] < A[i] > A[i+1] or A[i-1] > A[i] < A[i+1]

For example, the extreme points of an array
[0,5,3,6,8,7,15,9] are 5,3,8,7,15

So what will we do?
We will go through a for loop to look through each
value in the array starting from 1 and ending at len(arr)-2
then for each of these we will check:

if(a[i-1] < a[i] and a[i] > a[i+1])
else if(a[i-1] > a[i] and a[i]  < a[i+1])

if either of those values are true, we will set a boolean flag to True
at the end we will check the boolean flag, if it is false then print 'Sorted'

Apart from this, if any of the values are true, we will print them

'''
import random 

arr = []
while len(arr) < 500:
    i = random.randint(0,1024)
    if(i not in arr):
        arr.append(i)

isSorted = False
print(arr)

#We do from 1 till len-1 since len-1 is excluded
for i in range(1,len(arr)-1):

    if(arr[i-1] < arr[i] and arr[i] > arr[i+1]):
        isSorted = True
        print(arr[i])
    elif(arr[i-1] > arr[i] and arr[i] < arr[i+1]):
        isSorted = True
        print(arr[i])

if(not isSorted):
    print("Sorted!")

