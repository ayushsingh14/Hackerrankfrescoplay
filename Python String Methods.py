#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'strmethod' function below.
#
# The function accepts following parameters:
#  1. STRING para
#  2. STRING spch1
#  3. STRING spch2
#  4. LIST li1
#  5. STRING strf
#

def stringmethod(para, special1, special2, list1, strfind):
    

    special1=list(special1)
    word1= ''.join(i for i in para if not i in special1) 


    rev=word1[:70]

    rword2=rev[::-1]
    print(str(rword2))


    rw1="".join(rword2.split())


    temp=special2.join(rw1)
    print(str(temp))   


    res = [ele for ele in list1 if(ele in para)] 
    if bool(res)==True:
        print(f"Every string in {list1} were present")   
    else:
        print(f"Every string in {list1} were not present") 
        
        
    wr1=word1.split() 
    wr1split=[wr1[a] for a in range(len(wr1)) if a<20]
    print(wr1split)       
    words=word1.split() 
    uniques = []
    for word in words:
        if word not in uniques:
            uniques.append(word)
    
    
    counts = []
    for unique in uniques:
        count = 0              # Initialize the count to zero.
        for word in words:     # Iterate over the words.
            if word == unique:   # Is this word equal to the current unique?
                 count += 1         # If so, increment the count
        counts.append((count, unique))

    counts=[x[1] for x in counts if x[0]<3]
    counts.reverse()
    #counts.sort()
    a=[counts[x] for x in range(len(counts)) if x<20]
    a.reverse()
    print(a)    


    sf = word1.rfind(strfind)
    print(sf) # Write your code here
if __name__ == '__main__':
