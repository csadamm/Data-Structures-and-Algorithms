import random

arrA = [random.randint(0,1024) for _ in range(280)] 
arrB = [random.randint(0,1024) for _ in range(256)]
arrC = arrA + arrB

def merge(leftArr, rightArr, arrC):
    leftSize = len(arrC) // 2
    rightSize = len(arrC) - leftSize
    i = 0
    l = 0
    r = 0
    
    while(l < leftSize and r < rightSize):
        #If left value < right value, then store the left value in the Total Array
        if(leftArr[l] < rightArr[r]):
            arrC[i] = leftArr[l]
            i += 1
            l += 1
        #Else store the right value
        else:
            arrC[i] = rightArr[r]
            i += 1
            r += 1
            
    #Eventually there will be a value which cannot be compared to anything else, store this as the last value
    while(l < leftSize):
        arrC[i] = leftArr[l]
        i += 1
        l += 1
        
        
    while(r < rightSize):
        arrC[i] = rightArr[r]
        i += 1
        r += 1
        
    return arrC

def mergeSort(arrC):
    length = len(arrC)
    if length <= 1: #Base case
        return
    middle = length // 2 
    
    #Creating two arrays to split array in half
    leftArr = [0] * middle 
    rightArr = [0] * (length - middle)
    
    i = 0 #for left array
    j = 0 #for right array
    
    for i in range(i, length):
        #Values from leftmost to middle will be stored in leftArray
        if i < middle:
            leftArr[i] = arrC[i]
        #Values from middle to rightmost will be stored in leftArray
        else:
            rightArr[j] = arrC[i]
            j = j + 1
    #Repeat recursively to split the array up further until its 1 value
    mergeSort(leftArr)
    mergeSort(rightArr)
    #Recursively merge them back together and sort
    merge(leftArr, rightArr, arrC)
    
    return arrC

mergeSort(arrC)
print(arrC)
