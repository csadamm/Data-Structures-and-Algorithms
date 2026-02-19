import random

def quickSort(arr, low, high):
    
    if low < high: #Check if we have atleast 2 elements
        pivot = arr[high] #Set pivot as rightmost value in array
        i = low-1 #Set i as one before the first value
        
        for j in range(low, high): 
            if (arr[j] <= pivot):
                i += 1 
                temp = arr[i] #Swap the value of i with value of j
                arr[i] = arr[j]
                arr[j] = temp
                              
        #When index j reaches pivot, we set the pivot to be the next increment of i
        #Thus we will have all values left of the pivot being smaller than or equal to the pivot
        #And all values right of the pivot being larger than or equal to the pivot
        temp = arr[i+1]
        arr[i+1] = arr[high]
        arr[high] = temp 
        pivot = i + 1 
    
        quickSort(arr, low, pivot-1) #Repeat process but with the values on the left of the original pivot
        quickSort(arr, pivot+1, high)#Repeat process but with the values on the right of the original pivot
        
        return arr

def shellSort(arr):
    
    n = len(arr)
    gap = n//2 
    
    #Reduce the gap until it becomes 0. When the gap is 0, the list is fully sorted
    while gap >= 1:
        
        #Start of gapoed insertion sort.
        for i in range(gap, n): 
            temp = arr[i]
            j = i
            
            #We keep swapping until we find a value which doesn't need to be swapped
            while j>=gap and arr[j-gap] >temp:
                arr[i] = arr[j-gap]
                j = j - gap
            arr[j] = temp
            
        #Divide the gap by 2
        gap = gap // 2
        
    return arr
        
arrA = [random.randint(0,1024) for _ in range(280)]
print("ShellSort Algorithm:")
print(shellSort(arrA))

arrB = [random.randint(0,1024) for _ in range(256)]
print("QuickSort Algorithm:")
print(quickSort(arrB, 0, len(arrB)-1)) 