import time
def countingSort(inputArray):
    maxEl = max(inputArray)

    countArrayLength = maxEl+1

    countArray = [0] * countArrayLength

    for el in inputArray: 
        countArray[el] += 1

    for i in range(1, countArrayLength):
        countArray[i] += countArray[i-1] 

    outputArray = [0] * len(inputArray)
    i = len(inputArray) - 1
    while i >= 0:
        currentEl = inputArray[i]
        countArray[currentEl] -= 1
        newPosition = countArray[currentEl]
        outputArray[newPosition] = currentEl
        i -= 1

    return outputArray
start_time = time.time()
file = open("list.txt","r")
f = file.readlines()
inputArray = []
for line in f:
    if line == "\n":
        inputArray.append(int(line[:-1]))
    else:
        inputArray.append(int(line))
print("Input array = ", inputArray)
sortedArray = countingSort(inputArray)
print("Counting sort result = ", sortedArray)
time_execution = time.time() - start_time
print(time_execution)