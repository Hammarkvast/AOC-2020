input = [979,675,366,299,1721]
def accounting(expenseReport):
    stationary = 0
    index = 1
    while (stationary <= (len(expenseReport)-1)) and (index <= len(expenseReport)):
        print("test")
        if index == len(expenseReport):
            print("testing")
            stationary+=1
            index = stationary + 1
        elif (expenseReport[stationary] + expenseReport[index]) == 2020:
            print("HELLO")
            return expenseReport[stationary]*expenseReport[index]
        else:
            print(index)
            index+=1



print(accounting(input))
