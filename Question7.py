import csv

finalList = []

for i in range(2, 513):
    currentSequence = [i]

    j = i 
    while j != 1:
        if j % 2 != 0: 
            #value is odd. therefore, multiply by 3 and add 1
            j = (j*3)+1
            currentSequence.append(j)
        else:
            #value is even. therefore divide by 2
            # // will automatically make it an integer
            j = j // 2
            currentSequence.append(j)
    
    #Once j is 1, we have reached the 4-2-1 loop.
    #therefore, add this currentSequence to the finalList and repeat process
    finalList.append(currentSequence)

filename = "collatzSequence.csv"
with open(filename, 'w', newline='') as csvfile: #Opens the file in write mode
    csvwriter = csv.writer(csvfile) #Create writer object
    csvwriter.writerows(finalList) 
            
