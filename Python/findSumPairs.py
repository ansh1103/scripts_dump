# program to list element which sum is equal to the target number

def findPair(elementList, targetNumber):
    neslist = []
    for i in range(len(elementList)):
        for j in range(i+1, len(elementList)):
            if elementList[i] + elementList[j] == targetNumber:
                neslist.append((elementList[i], elementList[j]))
    print(neslist)

if __name__ == '__main__':
    findPair([3,1,5,2,10,12], 15)