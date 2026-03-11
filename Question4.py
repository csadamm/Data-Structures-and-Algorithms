'''
We will give a list of integers. The program will find all 2-pairs of integers that have the same product
2 pair -> 2 distinct pairs ((a,b), (c,d)) where a x b = c x d, a != b != c != d. 
range: 1-1024

For example: 10: 1 x 10 = 2 x 5
'''

#Generate array with values from 1 to 1024
arr = []
for i in range(1,1025):
    arr.append(i)
    
'''
Imagine the array A = [2,3,4,6]
The pairs will be:
(2,3), (2,4), (2,6),
(3,4), (3,6),
(4,6)

i.e 
We start from the first value and  pair with the rest of the values. then we restart this loop but increment the first value
'''
products = {}

for i in range(0, len(arr)):
    for j in range(i+1, len(arr)):
        pair = (arr[i], arr[j])
        product = arr[i] * arr[j]
        
        if product in products:
             products[product].append(pair)
        else:
            #products[product] means -> access this key inside the dictionary
            products[product] = [pair]
        
#now we have a dictionary with every key being a product and each value being the list of pairs of those products
#ex: {6 : [(1,6), (2,3)], 8 : [(1,8), (2,4)]} etc.

#therefore we will go through each key in the products dictionary and check the length of its values (its list of pairs) is greater than 1
#if so, we will print it
for product in products:
    if len(products[product]) > 1:
        print(f"Product {product}: {products[product]}")
