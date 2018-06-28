import re
file = open("condition.py", "r")

global conditionStatement
global ifCount, forCount, whileCount, elifCount, elseCount, newCondition
conditionStatements = {}
ifCount = 0
forCount = 0
whileCount = 0
elifCount = 0
elseCount = 0
newCondition = []
def numberOfIndentation(words):
    indentation = 0
    for i in range(len(words)):
        if(words[i] == ''):
            indentation += 1
        else:
            break
    return indentation

for line in file:
    words = re.split("; |, |\"|\(|\)|\n|\:| ", line)
    #print(words)
    #print(numberOfIndentation(words))
    
    if("if" in words):
        conditionStatements["if_" + str(ifCount)] = numberOfIndentation(words)
        ifCount += 1
    if("elif" in words):
        conditionStatements["elif_" + str(elifCount)] = numberOfIndentation(words)
        elifCount += 1
    if("else" in words):
        conditionStatements["else_" + str(elseCount)] = numberOfIndentation(words)
        elseCount += 1
    elif("for" in words):
        conditionStatements["for_" + str(forCount)] = numberOfIndentation(words)
        forCount += 1
    elif("while" in words):
        conditionStatements["while_" + str(whileCount)] = numberOfIndentation(words)
        whileCount += 1

'''for key in conditionStatements:
        print(key + " : " + str(conditionStatements[key]))
'''       

def newConditionKey():
    pathCount = 0
    for key in conditionStatements:
        if(conditionStatements[key] == 0):
            newCondition.append(key)
            print("path: " + str(pathCount))
            pathCount += 1


def computeCondition():
    #firstIndentation = newCondition[newCondition[0]]
    indentationNumber = 0
    pathCount = 0
    zeroInd = []
    fourInd = []
    eightInd = []
    twelveInd = []
    for key in conditionStatements:
        if(conditionStatements[key] == 0):
            zeroInd.append(key)
        elif(conditionStatements[key] == 4):
            fourInd.append(key)
        elif(conditionStatements[key] == 8):
            eightInd.append(key)
        elif(conditionStatements[key] == 12):
            twelveInd.append(key)
    for i in range(len(fourInd)):    
         print("path: " + str(pathCount))
         print(zeroInd[0] + " , " + fourInd[i])
         pathCount += 1
    for i in range(len(eightInd)):
        print("path: " + str(pathCount))
        print(zeroInd[0] + " , " + fourInd[0] + " , " + eightInd[i])
        pathCount += 1
        

        
computeCondition()


    
    
