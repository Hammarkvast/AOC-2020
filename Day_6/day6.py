import sys

sys.setrecursionlimit(2300)

input = []
# input = ["b", "", "a", "b", "c", "", "ba", "ca", "", "a", "a", "a", "a", "", "abc"]
# input = ["nuixfj", "ixozbutyj", "isxlpkqhwrmvj", "jincxga", "jenidx"]
# nuixfj
# ixozbutyj
# isxlpkqhwrmvj
# jincxga
# jenidx

sumOfAnsweredQuestions = 0
questionsAnswered = []

with open('input.txt') as f:
    input = [line.rstrip() for line in f]

def answeredQuestions(questions, answered):
    for question in questions:
        if question not in answered:
            answered.append(question)
            
def groupQuestionaire(questionaire, sum):
    global sumOfAnsweredQuestions
    global questionsAnswered
    if len(questionaire) == 1:
        answeredQuestions(questionaire[0], questionsAnswered)
        sum += len(questionsAnswered)
        return sum
    elif questionaire[0] == "":
        del questionaire[0]
        sum+=len(questionsAnswered)
        questionsAnswered = []
        return groupQuestionaire(questionaire, sum)
    else:
        answeredQuestions(questionaire[0], questionsAnswered)
        del questionaire[0]
        return groupQuestionaire(questionaire, sum)
    
def checkCommonYeses(answers):
    if len(answers) == 1:
        common = len(answers[0])
        return common
    firstAnswer = answers[0]
    common = 0
    del answers[0]
    for yes in firstAnswer:
        amount = 0
        for answer in answers:
            if yes in answer:
                amount+=1
        if amount == len(answers):
            common+=1
    return common

def getAllValidYeses(questionaire, sum):
    global questionsAnswered
    if len(questionaire) == 1:
        questionsAnswered.append(questionaire[0])
        yeses = checkCommonYeses(questionsAnswered)
        print(yeses)
        sum +=yeses
        return sum
    elif questionaire[0] == "":
        del questionaire[0]
        yeses = checkCommonYeses(questionsAnswered)
        sum+=yeses
        questionsAnswered = []
        return getAllValidYeses(questionaire, sum)
    else:
        questionsAnswered.append(questionaire[0])
        del questionaire[0]
        return getAllValidYeses(questionaire, sum)


amount = getAllValidYeses(input, 0)
print(amount)
