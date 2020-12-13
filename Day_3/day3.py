input = []
# input = ["..##.........##.........##.........##.........##.........##.......", 
#         "#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..",
#         ".#....#..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.",
#         "..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#",
#         ".#...##..#..#...##..#..#...##..#..#...##..#..#...##..#..#...##..#.",
#         "..#.##.......#.##.......#.##.......#.##.......#.##.......#.##.....",
#         ".#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#",
#         ".#........#.#........#.#........#.#........#.#........#.#........#",
#         "#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...",
#         "#...##....##...##....##...##....##...##....##...##....##...##....#",
#         ".#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#"]
PosDown = 0
PosRight = 0
trees = 0
with open('input.txt') as f:
    input = [line.rstrip() for line in f]

def checkCycle(row, moveX):
    global PosRight
    if ((PosRight + moveX) > (len(row)-1)):
        PosRight = 0 +((PosRight+moveX) - len(row))
    else:
        PosRight+= moveX

def checkIfTree(row):
    if row[PosRight] == '#':
        return True
    return False

def traverse(moveX, moveY):
    global PosDown
    global trees
    for row in input:
        if PosDown == (len(input)-1):
            if checkIfTree(input[PosDown]):
                trees+=1
            return trees
        else:
            if checkIfTree(input[PosDown]):
                trees+=1
            PosDown+=moveY
            checkCycle(input[PosDown], moveX)
one = traverse(1, 1)
PosDown = 0
PosRight = 0
trees = 0
two = traverse(3, 1)
PosDown = 0
PosRight = 0
trees = 0
three = traverse(5, 1)
PosDown = 0
PosRight = 0
trees = 0
four = traverse(7, 1)
PosDown = 0
PosRight = 0
trees = 0
five = traverse(1, 2)
print(one*two*three*four*five)

