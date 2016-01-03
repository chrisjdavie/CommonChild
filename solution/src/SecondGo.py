'''
Solving the hackerrank puzzle Common Child, 2nd try

---------------------

So find all the indicies for all the characters (O(N))
and the find the dominant characters (O(N)?) and do for
each subsequent character in the list. O(N^2) to O(N^3)?

This is a lot worse that that, perhaps. I've got another idea
which I think is N^2. I'll try that.

Created on 2 Jan 2016

@author: chris
'''
import copy
from collections import Counter

def testNewPairs():
    pass

def solver(inputStrings):
    output = []
    
    string0 = inputStrings[0]
    string1 = inputStrings[1]
    
    # making things easier - find letters in common with both
    
    inCommon = set(string0).intersection(set(string1))
    
    reduced0 = []
    reduced1 = []
    
    for char0, char1 in zip(string0, string1):
        if char0 in inCommon:
            reduced0.append(char0)
        if char1 in inCommon:
            reduced1.append(char1)
    reduced0 = "".join(reduced0)
    reduced1 = "".join(reduced1)
    
    
    # find the indicies of each character
    
    charInds = {}
    for char in inCommon:
        charInds[char] = { 'iInds': [],
                           'jInds': [],
                           'smallCoords' : [-1,-1]
                         }
    
    for i, char0 in enumerate(reduced0):
        charInds[char0]['iInds'].append(i)
    
    for j, char1 in enumerate(reduced1):
        charInds[char1]['jInds'].append(j)
    
    
    # initialise the smallest coordinates
    
    domPairs = set()
    domPairs.add( (-1,-1) )
    
    iOutput = -1
    iDomDyn = {}
    jDomDyn = {}
    
    kk = 0
    while len(domPairs) > 0:
        print kk
        kk += 1
        
        iOutput += 1
        smallCoords = set()
        
        iMin = 5001
        jMin = 5001
        for ( iDom, jDom ) in domPairs:
            
            try:
                iDomCharPos = iDomDyn[iDom]
            except(KeyError):
                iDomCharPos = {}
                for char in charInds:
                    for i in charInds[char]['iInds']:
                        if i > iDom:
                            break
                    else:
                        continue
                    iDomCharPos[char] = i                
                iDomDyn[iDom] = iDomCharPos
            
            try:
                jDomCharPos = jDomDyn[jDom]
            except(KeyError):
                jDomCharPos = {}
                for char in charInds:
                    for j in charInds[char]['jInds']:
                        if j > jDom:
                            break
                    else:
                        continue
                    jDomCharPos[char] = j
                jDomDyn[jDom] = jDomCharPos
                
                
            for char in charInds:            
                try:
                    i = iDomCharPos[char]
                    j = jDomCharPos[char]
                    smallCoords.add((i,j))
                    if i < iMin:
                        iMin = i
                    if j < jMin:
                        jMin = j
                except:
                    continue
                
            
        #  find the candidates for the first position. This allows a tree-based approach, if I want
        
        domPairsNew = set()
        for (i, j) in smallCoords:
            
            newPair = True
            for pair in domPairsNew:
                if (i < pair[0]) and (j < pair[1]):
                    domPairsNew.discard((pair))
                    domPairsNew.add((i,j))
                    newPair = False
                    break
                if (i > pair[0]) and (j > pair[1]):
                    newPair = False 
                    break
             
            if newPair:
                domPairsNew.add( (i, j) )
        
        domPairs = domPairsNew
        
    output.append(iOutput)
    
    return output
    

if __name__ == '__main__':
    inputStrings = []
    
    for _ in range(2):
        inputStrings.append(raw_input().strip())
     
    output = solver(inputStrings)
    
    for o in output:
        print o