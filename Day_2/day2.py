valid = 0
# listOfInputs = ["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]
listOfInputs = []
def validPassword(password, min, max, character):
    amount = 0
    i = 0
    while i <len(password):
        if password[i] == character:
            amount+=1
            i+=1
        else: 
            i+=1
    if (amount>= min) and (amount <=max):
        return 1
    else:
        return 0

def validPasswordPartTwo(password, min, max, character):
    amount = 0
    i = 0
    inMinMax = 0
    pos1 = min-1
    pos2 = max-1
    # print(pos1)
    while i <len(password):
        if ((password[i] == character)):
            if (i == pos1) or (i == pos2):
                inMinMax +=1
            i+=1
        else: 
            i+=1
    if (inMinMax == 1):
        return 1
    else:
        return 0    

def getPasswords(input):
    global valid
    parsedInput = input.split(":")
    parseSpaces = parsedInput[0].split()
    character = parseSpaces[1]
    minMax = parseSpaces[0].split('-')
    policy = parsedInput[0]
    password = parsedInput[1].strip()
    minimum = int(minMax[0])
    maximum = int(minMax[1])
    valid += validPasswordPartTwo(password, minimum, maximum, character)

with open('input_day_2.txt') as f:
    listOfInputs = [line.rstrip() for line in f]

for input in listOfInputs:
    getPasswords(input)

print(valid)