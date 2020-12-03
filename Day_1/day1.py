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


with open('input.txt') as f:
    input = [line.rstrip() for line in f]

for i in range(0, len(input)): 
    input[i] = int(input[i]) 
# print(len(input))

print(accounting(input))
