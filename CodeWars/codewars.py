def maxSequence(arr):
    largestSum = 0
    currentSum = 0
    for ii in arr:
        currentSum = currentSum + ii
        if currentSum < 0: currentSum = 0
        if largestSum < currentSum: largestSum = currentSum
    
    return largestSum

maxSequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
