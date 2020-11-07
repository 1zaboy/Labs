import math
import random
print("Lab 6. Performed by Vlad Kolosov.")
print()

def printArray(arr):
    print('\n')
    i = 0
    for item in arr:
        print("Item in array №", i, ":", item)
        i += 1
    print('\n')

def findMaxByAbs(arr):
    oldVal = -99999 
    for item in arr:
        valAbs = math.fabs(item)
        if valAbs > oldVal:
            oldVal = valAbs
    return oldVal

def sortZero(arr):
    newArray = []
    countZero = 0
    for item in arr:
        if item != 0:
            newArray.append(item)
        else:
            countZero += 1

    for item in range(0, countZero):
        newArray.append(0)
    return newArray

def getSumRange(arr):
    sum = 0
    isWrite = False
    for item in arr:
        if item > 0:
            if isWrite:
                return sum
            isWrite = True
            continue

        if isWrite:
            sum = sum + item
    return sum


#---------------------------------------------------------------
#---------------------------Array[n]----------------------------
#---------------------------------------------------------------
def task1():
    countItem = int(input("N: "))

    arr1 = []
    for i in range(0, countItem):
        arr1.append(random.randrange(-10, 2, 1))

    printArray(arr1)
    print("Max val by mod: ", findMaxByAbs(arr1))

    arr1 = sortZero(arr1)
    printArray(arr1)

    print("Sum range: ", getSumRange(arr1))

#---------------------------------------------------------------
#-------------------------Array[4][4]---------------------------
#---------------------------------------------------------------
def task2():
    arr2 = [[1, 2,  3,  40],
            [1, -2, 13, 4],
            [4, 4,  4,  4],
            [50, 5,  5,  5],]

    #write 
    #for i in range(0, 4):
    #    arrT = []
    #    for ii in range(0, 4):
    #        item = int(input("Enter value [{0}][{1}]: ".format(i,ii)))
    #        arrT.append(item)
    #    arr2.append(arrT)

    #print 
    for i in range(0, 4):
        for ii in range(0, 4):
            print(arr2[i][ii], end="\t")
        print();

    #sun
    sum1 = 0
    countTrueRow = 0
    for i in range(0, 4):
        isSum = True
        sumInRow = 0
        for ii in range(0, 4):
            if arr2[i][ii] > 0:
                sumInRow += arr2[i][ii]
            else:
                isSum = False

        if isSum:
            sum1 += sumInRow 
            countTrueRow = countTrueRow + 1
        if countTrueRow == 3:
            break 

    if countTrueRow == 3:
        print("Sum row: ", sum1)
    else:
        print("No 3 row")

    #diog
    sumDiog = []
    for i in range(1, 4):
        sumd = 0
        for ii in range(0, 4 - i):
            sumd += arr2[ii][i + ii]
        sumDiog.append(sumd)

    for i in range(1, 4):
        sumd = 0
        for ii in range(0, 4 - i):
            sumd += arr2[i + ii][ii]
        sumDiog.append(sumd)

    minValue = 99999
    for item in sumDiog:
        if item < minValue:
            minValue = item

    print("Минимальное значение диагоналей: ", minValue)

while True:
    ch = int(input("Select task: "))
    if ch == 1:
        task1()
    if ch == 2:
        task2()
    if ch != 1 and ch != 2:
        break


