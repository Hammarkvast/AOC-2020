# input = ["BFFFBBFRRR", "FFFBBBFRRR", "BBFFBBFRLL"]
input = []
with open('input.txt') as f:
    input = [line.rstrip() for line in f]

rows = [i for i in range(128)]
columns = [i for i in range(8)]  
def getValidColumn(directions, startIndex, endIndex, listOfColumns):
    if len(listOfColumns) == 2:
        if directions[0] == 'L':
            return listOfColumns[0]
        else:
            return listOfColumns[1]
    middle = int((len(listOfColumns)/2))
    if directions[0] == 'L':
        directions = directions[1:]
        listOfColumns = listOfColumns[:middle]
        return getValidColumn(directions, startIndex, middle, listOfColumns)
    else:
        directions = directions[1:]
        listOfColumns = listOfColumns[middle:]
        return getValidColumn(directions, middle, endIndex, listOfColumns)

def getSetOfRows(directions, startIndex, endIndex, listOfRows):
    print(directions[0])
    middleIndex = int((len(listOfRows)/2))
    if(len(listOfRows) == 2):
        if directions[0] == 'F':
            return listOfRows[0]
        else:
            return listOfRows[1]
    elif directions[0] == 'F':
        directions = directions[1:]
        listOfRows= listOfRows[:middleIndex]
        print(listOfRows)
        return getSetOfRows(directions, startIndex, middleIndex, listOfRows)
    else:
        directions = directions[1:]
        listOfRows = listOfRows[middleIndex:]
        print(listOfRows)
        return getSetOfRows(directions, middleIndex, endIndex, listOfRows)

def getSeatID(partition, rowNumbers, columnNumbers):
    highestSeatID = 0
    for directions in partition:
        column = directions[7:]
        rowID = getSetOfRows(directions, 0, 127, rowNumbers)
        columnID = getValidColumn(column,0, 7, columnNumbers)
        SeatID = (rowID * 8) + columnID
        if SeatID > highestSeatID:
            highestSeatID = SeatID
    return highestSeatID

def getListOfSeatIDS(partitions, rowlist, columnlist):
   ids = []
   for  directions in partitions:
       column = directions[7:]
       rowID = getSetOfRows(directions, 0, 127, rowlist)
       columnID = getValidColumn(column,0, 7, columnlist)
       seatID = (rowID * 8) + columnID
       ids.append(seatID)
   ids.sort()
   return ids
    
def whatsMySeat():
    idList = getListOfSeatIDS(input, rows, columns)
    i = 0
    while ((i+1)<= (len(idList)-1)):
        if (idList[i+1]-idList[i]) == 2:
            return (idList[i]+1)
        else:
            i+=1


seat = whatsMySeat()

validRow = getSetOfRows(input[0], 0, 127, rows)
print(seat)



# 15m
# 13d
# 45d