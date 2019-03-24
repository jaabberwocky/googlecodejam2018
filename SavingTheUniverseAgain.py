import sys

def readInput():
    '''
    Reads from StdIn and outputs (numCases, cases)
    cases is a dictionary containing an entry for each case number.
    '''
    numCases = 0
    cases = {}
    for ind, line in enumerate(sys.stdin):
        if ind == 0:
            numCases = int(line)
        else:
            testCaseInput = line.split(" ")
            cases[ind] = {
                'D': testCaseInput[0],
                'P': testCaseInput[1]
                }
            
    return (numCases, cases)
    
class Solution:
    '''
    Models the solution space.
    ind: case number for printing later
    D: shield 
    P: robot instructions
    '''
    
    def __init__(self, ind, D, P):
        self.ind = ind
        self.D = D
        self.P = P
        
    def needsHack():
        '''
        Determines if hacking is even needed.
        Returns true or false.
        '''
        currentStrength = 1
        damage = 0
        
        for ch in self.P:
            if damage > self.D:
                return True
            if ch == 'S':
                damage += currentStrength
            else:
                currentStrength *= 2
        return False

            