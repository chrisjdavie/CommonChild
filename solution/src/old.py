        #  find the candidates for the first position. This allows a tree-based approach, if I want
        
        domPairs = set()
        for (i, j) in smallCoords:
            
            newPair = True
            for pair in domPairs:
                if (i < pair[0]) and (j < pair[1]):
                    domPairs.discard((pair))
                    domPairs.add((i,j))
                    newPair = False
                    break
                if (i > pair[0]) and (j > pair[1]):
                    newPair = False 
                    break
             
            if newPair:
                domPairs.add( (i, j) )