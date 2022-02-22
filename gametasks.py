import os

def printInstructions(instruction):
    print(instruction)

    
def getUserScore(userName):
    f = open ('userScores.txt', 'r')
    for line in f:
        content = line.split(', ')
        if content[0] == userName:
            
            return content[1]

    return "-1"

def updateUserScore(newUser, userName, score):
    if newUser == True:
        f = open('userScores.txt', 'a')
        f.write('\n%s, %s'%(userName, score))
        f.close()
        print(newUser)

    else:
        tmp = open ('userScores.tmp', 'w')
        f = open ('userScores.txt', 'r')
        for line in f:
            content = line.split(', ')
            if content[0] == userName:
                tmp.write('%s, %s\n'%(userName, score))
            else:
                tmp.write('%s, %s'%(content[0], content[1]))

        os.remove('userScores.txt')
        os.rename('userScores.tmp','userScores.txt')
    

updateUserScore(False, 'Ann', 10)
                
result = getUserScore('50cent')

print(result)

