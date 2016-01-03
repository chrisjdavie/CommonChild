'''
Solving the hackerrank puzzle Common Child

https://www.hackerrank.com/challenges/common-child

---------------------

Problem Statement

Given two strings a and b of equal length, what's the longest string (S) that can be constructed such that it is a child of both? 

A string x is said to be a child of a string y if x can be formed by deleting 0 or more characters from y. 

For example, ABCD and ABDC has two children with maximum length 3, ABC and ABD. Note that we will not consider ABCD as a common child because C doesn't occur before D in the second string.

Input format

Two strings, a and b, with a newline separating them.

Constraints

All characters are upper cased and lie between ASCII values 65-90. The maximum length of the strings is 5000.

Output format

Length of string S.

---------------------

This is a sort-of O(N!) solution. It's not really, it's at most O(26!), but in most cases a
lot less (added quite a lot of dynamic programming features). Unfortunately, that's still a 
really long solution, doesn't pass the test cases. 

Thinking about it, I might have a better solution that's around O(N) to O(N^2), so that's 
second go.  

Created on 2 Jan 2016

@author: chris
'''
import copy

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
    
    N = len(reduced0) - 1
    
    def genInds(skip, inds = [0]):
        if skip:
            inds[-1] += 1
        
        if inds[-1] >= N:
            inds.pop()
            try:
                inds[-1] += 1
            except(IndexError):
                pass
        elif not skip:
            inds.append(inds[-1]+1)
            
        return inds
    
    inds = [0]
    if len(reduced0) == 0:
        inds = []
    
    alreadyTested = set()
    alreadyCalced = {}
    maxOp = 0
    i = 0
    skip = False
    while len(inds) != 0:
        i += 1
        
        skip = False
        
        testList = []
        for j in inds:
            testList.append(reduced0[j])
        testString = "".join(testList)
        if (len(reduced0) - inds[-1]) < (maxOp - len(inds)):
            alreadyTested.add(testString)
        
        if testString not in alreadyTested:
            alreadyTested.add(testString)
            
            if len(testString) == 1:
                opAttempt = 0
                indexN = 0
                j = 0
            else:
                opAttempt = alreadyCalced[testString[:-1]]['opAttempt']
                indexN = alreadyCalced[testString[:-1]]['indexN']
            j = len(testString) - 1
            
            nextSubstring1 = copy.copy(reduced1[indexN:len(reduced1)-maxOp+j])
            char0 = testString[-1]
            try:
                indexN += nextSubstring1.index(char0) + 1
                opAttempt += 1
            except(ValueError):
                skip = True
            
#             print
#             opAttemptOld = 0
#             indexNOld = 0
#             nextSubstring1 = copy.copy(reduced1[indexNOld:len(reduced1)-maxOp])
#             for j, char0Old in enumerate(testString):
#                 try:
#                     indexNOld += nextSubstring1.index(char0Old) + 1
#                     opAttemptOld += 1
#                     nextSubstring1 = reduced1[indexNOld:len(reduced1)-maxOp+j+1]
#                 except(ValueError):
#                     skip = True
#                     break
#             
#             print opAttempt, opAttemptOld
#             print indexN, indexNOld
#             print testString, i, char0
#             
#             if i == 2:
#                 exit()
            
            if opAttempt > maxOp:
                maxOp = opAttempt 
            
            alreadyCalced[testString] = { 'opAttempt': opAttempt,
                                          'indexN': indexN
                                         }
            
        else:
            skip = True
            
        inds = genInds(skip)
    
    output.append(maxOp)
    
    return output
    

if __name__ == '__main__':
    inputStrings = []
    
    for _ in range(2):
        inputStrings.append(raw_input().strip())
     
    output = solver(inputStrings)
    
    for o in output:
        print o