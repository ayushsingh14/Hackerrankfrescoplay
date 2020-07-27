special1=list(special1)
    word1= ''.join(i for i in para if not i in special1) 


    rword2=word1[:70]

    rword2=rword2[::-1]
    print(str(rword2))


    rword2="".join(rword2.split())


    rword2=special2.join(rword2)
    print(str(rword2))   


    res = [ele for ele in list1 if(ele in para)] 
    if bool(res)==True:
        print(f"Every string in {list1} were present")   
    else:
        print(f"Every string in {list1} were not present") 
        
        
    word1=word1.split() 
    print(word1[:20]) 
          
    uniques = []
    for word in word1:
        if word not in uniques:
            uniques.append(word)

    counts = []
    for unique in uniques:
        count = 0              # Initialize the count to zero.
        for word in word1:     # Iterate over the words.
            if word == unique:   # Is this word equal to the current unique?
                 count += 1         # If so, increment the count
        counts.append((count, unique))

    counts=[x[1] for x in counts if x[0]<3]
    counts.reverse()
    a=counts[:20]
    a.reverse()
    print(a)  
    
    
    
    listToStr=' '.join([str(elem) for elem in word1]) 
    sf = listToStr.rfind(strfind)
    print(sf) 
