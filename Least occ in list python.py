word1=word1.split() 
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
    #counts.sort()
    a=[counts[x] for x in range(len(counts)) if x<20]
    a.reverse()
    print(a)    
