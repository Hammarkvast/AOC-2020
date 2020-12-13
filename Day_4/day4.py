from os import pipe2
import sys
# input = ["hcl:#cfa07d eyr:2025 pid:166559648", "iyr:2011 ecl:brn hgt:59in", "", 
#         "iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884", "hcl:#cfa07d byr:1929", "", 
#         "hcl:#ae17e1 iyr:2013", "eyr:2024", "ecl:brn pid:760753108 byr:1931", "hgt:179cm", "", 
#         "ecl:gry pid:860033327 eyr:2020 hcl:#fffffd", "byr:1937 iyr:2017 cid:147 hgt:183cm"]
#"ecl:gry pid:860033327 eyr:2020 hcl:#fffffd", "byr:1937 iyr:2017 cid:147 hgt:183cm"

input =  []

required = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]

eyeColors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

passport = []

passportDict = {}

sys.setrecursionlimit(1500)

#PART 1!

def checkValidity(passportFields):
    for field in required:
        if (field not in passport) and (field != "cid"):
            return 0
    return 1

def getPassPortFields(partOfPassport):
    for field in partOfPassport:
        getField = field.split(":")
        passport.append(getField[0])

def grabPassports(batch):
    global passport
    if len(batch) == 1:
        fields = batch[0].split(" ")
        getPassPortFields(fields)
        return checkValidity(passport)
    elif batch[0] == "":
        isPassportValid = checkValidity(passport)
        passport = []
        del batch[0]
        return isPassportValid + grabPassports(batch)
    else:
        fields = batch[0].split(" ")
        getPassPortFields(fields)
        del batch[0]
        return 0 + grabPassports(batch)

# PART 2!

def checkDigit(colorCode):
    for c in colorCode:
        if c.isdigit():
            return True
    return False

def checkChar(colorCode, char):
    for c in colorCode:
        if c == char:
            return True
    return False

def checkEyeColor(code):
    for color in eyeColors:
        if color == code:
            return True
    return False

def checkPID(id):
    if len(id) == 9:
        for c in id:
            if not c.isdigit():
                return False
        return True
    return False

def checkValidityPart2(passportFields):
    for field in required:
        if (field not in passportFields) and (field != "cid"):
            return 0
        else:
            if field == "byr":
                year = passportDict.get(field)
                if (int(year) >= 1920) and (int(year) <= 2002) and (len(year)<= 4):
                    continue
                else:
                    return 0
            elif field == "iyr":
                year = passportDict.get(field)
                if (int(year) >= 2010) and (int(year) <= 2020) and (len(year)<= 4):
                    continue
                else:
                    return 0
            elif field == "eyr":
                year = passportDict.get(field)
                if (int(year) >= 2020) and (int(year) <= 2030) and (len(year)<= 4):
                    continue
                else:
                    return 0
            elif field == "hgt":
                height = passportDict.get(field)
                if "cm" in height:
                    height= height.replace("cm",'')
                    if (int(height) >= 150) and (int(height) <= 193):
                        continue
                    else:
                        return 0
                elif "in" in height:
                    height = height.replace("in","")
                    if (int(height) >= 59) and (int(height) <= 76):
                        continue
                    else:
                        return 0
                else:
                    return 0
            elif field == "hcl":
                hairColor = passportDict.get(field)
                if (hairColor[0] == "#"):
                    code = hairColor[1:]
                    containsNumber = checkDigit(code)
                    if containsNumber or ((checkChar(code, 'a')) or (checkChar(code, 'b')) or (checkChar(code, 'c')) or (checkChar(code, 'd')) or (checkChar(code, 'e')) or (checkChar(code, 'f'))):
                        continue
                    else:
                        return 0
                else:
                    return 0
            elif field == "ecl":
                eyeColor = passportDict.get(field)
                if checkEyeColor(eyeColor):
                    continue
                else:
                    return 0
            elif field == "pid":
                passID = passportDict.get(field)
                if checkPID(passID):
                    continue
                return 0
            elif field == "cid":
                continue
    return 1

def getPassPortFieldsPart2(partOfPassport):
    for field in partOfPassport:
        getField = field.split(":")
        passportDict[getField[0]] = getField[1]

def grabPassportsPart2(batch):
    global passportDict
    if len(batch) == 1:
        fields = batch[0].split(" ")
        getPassPortFieldsPart2(fields)
        return checkValidityPart2(passportDict)
    elif batch[0] == "":
        isPassportValid = checkValidityPart2(passportDict)
        passportDict = {}
        del batch[0]
        return isPassportValid + grabPassportsPart2(batch)
    else:
        fields = batch[0].split(" ")
        getPassPortFieldsPart2(fields)
        del batch[0]
        return 0 + grabPassportsPart2(batch)

with open('input.txt') as f:
    input = [line.rstrip() for line in f]

valid = grabPassportsPart2(input)

print(valid)