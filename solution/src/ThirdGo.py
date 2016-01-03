'''
The image of this is a grid, which letters down each side. I'm 
exploring the grid, looking for pairs of numbers. I stop when I 
find one.

Very similar to the cannonical solution - I hold less data, but
the wiki solution has more sensible data access patterns, which
probably makes it a winner.

Created on 3 Jan 2016

@author: chris
'''
from copy import copy
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
    
#     grid = []
#     
#     row = [-1]*len(reduced0)
#     for _ in range(len(reduced1)):
#         grid.append(copy(row))
#     
#     for row in grid:
#         print row
#     print reduced0
#     print reduced1
    
    iStart, jStart = -1, -1
    coordPairs = [(iStart, jStart)]
    moves = -1
    
    while len(coordPairs) > 0:
        moves += 1
        iLimit = len(reduced0)
        newCoordPairs = []
        for k, (iStart, jStart) in enumerate(coordPairs):
            if len(coordPairs) > k + 1:
                jLimit = coordPairs[k+1][1] + 1
                kUp = k + 1
                while jLimit == jStart + 1 and len(coordPairs) > kUp + 1:
                    jLimit = coordPairs[kUp+1][1] + 1
                    kUp += 1
                if len(coordPairs) == kUp + 1:
                    jLimit = len(reduced1)
            else:
                jLimit = len(reduced1)
            for j in range(jStart+1,jLimit):
                charJ = reduced1[j] 
                for i in range(iStart+1,iLimit):
                    charI = reduced0[i]
#                     grid[j][i] = moves                   
                    if charI == charJ:
#                         grid[j][i] = 'x'
                        newCoordPairs.append((i, j))
                        if i + 1 < iLimit:
                            iLimit = i + 1

        
        coordPairs = newCoordPairs
     
     
#         for pairs in newCoordPairs:
#             print pairs
# #      
#         for row in grid:
#             print row    
    
    
    output.append(moves)
    return output
    
if __name__ == '__main__':
    inputStrings = []
    
    for _ in range(2):
        inputStrings.append(raw_input().strip())
     
    output = solver(inputStrings)
    
    for o in output:
        print o