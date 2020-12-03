# input = [979,675,299,366,1721]
input = []
def accounting(expenseReport):
    stationary = 0
    index = 1
    while (stationary <= (len(expenseReport)-1)) and (index <= len(expenseReport)):
        if index == len(expenseReport):
            stationary+=1
            index = stationary + 1
        elif (expenseReport[stationary] + expenseReport[index]) == 2020:
            return expenseReport[stationary]*expenseReport[index]
        else:
            index+=1

def moreAccounting(expenseReport):
    stationary = 0
    index = 1
    nextIndex = 2
    while (stationary <= (len(expenseReport)-2) and (index <= (len(expenseReport)-1)) and (nextIndex <= len(expenseReport))):
        if (nextIndex == len(expenseReport)) and (index == (len(expenseReport) - 1)):
            stationary+=1
            index = stationary + 1
            nextIndex = index + 1
        elif (expenseReport[stationary] + expenseReport[index] + expenseReport[nextIndex]) == 2020:
            return expenseReport[stationary] * expenseReport[index] * expenseReport[nextIndex]
        else:
            if(index < (len(expenseReport)-1) and (nextIndex  == (len(expenseReport)-1))):
                nextIndex = index + 1
                index+=1
            else:
                nextIndex+=1


with open('input.txt') as f:
    input = [line.rstrip() for line in f]

for i in range(0, len(input)): 
    input[i] = int(input[i]) 

print(moreAccounting(input))
