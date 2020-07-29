def primegenerator(num, val):
    p=[]
    
    for n in range(2,num + 1):  
        if n > 1:  
            for i in range(2,n):  
                if (n % i) == 0:  
                    break  
            else:
                p.append(n)
    if val==1:
        for i in range(0, len(p)):
            if i % 2 == 0:
                yield p[i]
    else:
        for i in range(0, len(p)):
             if i % 2 != 0:
                yield p[i]
if __name__ == '__main__':

    num = int(input().strip())

    val = int(input().strip())

    for i in primegenerator(num, val):
        print(i,end=" ")
