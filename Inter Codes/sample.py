def findIndex(arr, k):
    for i in range(len(arr)):
        if arr[i] == k:
            return i
        elif arr[i] > k:
            return i
    return len(arr)

def calculate():
    pass    
    
def minimumOperations(numbers):
    # Write your code here
    filler = []
    filler.append(numbers[0])
    filler.append(numbers[1])
    opsCounter = 0
    numbers = numbers[2:]
    for number in numbers:
        index = findIndex(filler, number)
        if index <= len(numbers)/2:
            numElements = len(numbers[0:index])
            opsCounter += (2*numElements + 1)
        else:
            numElements = len(numbers[index:])
            opsCounter += 2*numElements + 1
        filler.insert(index, number)
    
        return opsCounter

print(minimumOperations([2, 5, 6, 10]))
