
raw="1"

for _ in range(30):
    newRow=""
    iter=None
    for i in raw:
        if(iter==None):
            iter=i

        
        else:
            if(iter[-1]==i):
                iter+=i
            else:
                strLen=len(iter)
                tempStr=str(strLen)+iter[-1]
                newRow+=tempStr
                iter=i
        #print(iter)
                
    
    strLen=len(iter)
    tempStr=str(strLen)+iter[-1]
    newRow+=tempStr
    

    raw=newRow

    # print("space")
    # print(raw)
    # print("space")

print(len(raw))