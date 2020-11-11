#calculate barrel volumes
#code challange https://codeforces.com/problemset/problem/1430/B
def barrelCal(testData):
    #testData[0][0] = nr of barrels
    #testData[0][1] = nr actions
    nrB=int(testData[0][0])
    nrA=int(testData[0][1])
    amountL = testData[1]
    amountL =[int(x) for x in amountL]
    for i in range(0, nrA):
        maxAi = max(range(len(amountL)), key=amountL.__getitem__) #get index with max value       
        bAmount = amountL[maxAi]  #save the max value        
        amountL[maxAi]=0 #set selected index to 0       
        maxAi = max(range(len(amountL)), key=amountL.__getitem__) #select next max        
        amountL[maxAi]+=bAmount #add max value
    return (max(amountL)-min(amountL))

#set initial values
lineCount = 0
tests = 0
barrelData = []
#read data file
with open("test.txt", "r") as reader:
    for line in reader:
        testCount = 0
        if lineCount == 0 :
            tests = int(line)
            lineCount += 1
        else :
            if lineCount % 2 > 0 :
                nkList = line.split()
                #print(nkList)
            else :
                amountList = line.split()
                barrelData.append((nkList, amountList))
                #print(amountList)
            lineCount +=1
        
#print(lineCount)
#print(tests)
#print(barrelData)
#loop test cases
for test in barrelData :
    print(barrelCal(test))
    
   