'''
A is an array of n distinct elements
An element A[i] is called extreme if:

    A[i] is not the first nor the last element of A
    i.e A[i] is not A[0] nor A[n-1]
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

i.e if the value is either a local maximum or a local minimum
i.e if the value is either bigger than both neighbours OR smaller than both neighbours

if either of those values are true, we will set a boolean flag to True
at the end we will check the boolean flag, if it is false then print 'Sorted'

Apart from this, if any of the values are true, we will print them

'''
import random 

arr = []
extremes = []
#An alternative method is to use pythons built in random generator:
#arr = random.sample(range(1025), 500)
#this will randomly generate distinct elements from 0-1024, 500 times

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
        extremes.append(arr[i])
    elif(arr[i-1] > arr[i] and arr[i] < arr[i+1]):
        isSorted = True
        extremes.append(arr[i])

if(not isSorted):
    print("Sorted!")
else:
    print("\nList of extreme values: ")
    print(extremes)
    
#Q. Do you agree that an array has no extreme points if and only if it is sorted? Explain your answer.
'''
It depends on how sorted is defined. If it is defined traditionally, i.e sorted in an ascending order, then this is incorrect.
This is because for an array to have no extreme points, it would need to be either sorted in ascending order OR sorted in descending order. 
i.e there is no change of direction

This is because an extreme point occurs when (graphically) there is a local minimum or a local maximum (there is a change of direction),
therefore we would need a list of values which graphically are a diagonal line either going up or down.
'''
