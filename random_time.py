import random 
import time
def getRandomDate(startDate, endDate ):
    print("Printing random date between", starDate, "and" , endDate)
    randomGenerator = random.random()
    dateFormat = '%m/%d/%Y'
    startTime = time.mktime(time.strptime(startDate , dateFormat))
    endTime = time.mktime(time.strptime(startDate , dateFormat))
    randomTime = startTime + RandomGenerator * (endTime - startTime)
    randomDate = time.strftime(dateformat,time.localtime(randomTime))
    return randomDate
    print("Random Date = ", getRandomDate("1/1/2025" , "12/12/2027"))
    
