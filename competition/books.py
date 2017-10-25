def getSumOfBookChoices(listBooks):
    sumA = 0
    for x in range(len(listBooks)):
        sumA += books[listBooks[x]]
    return sumA

topics = []
bookNumber = -1
minTime = 100000
books = []

try:
    book = input()
    bookData = book.split(' ')
    time = bookData[0]
    bookNumber += 1
    books.append(time)
    for x in range(1, len(bookData)):
        topic = bookData[x]
        found = False
        for y in range(len(topics)):
            if topics[y] == topic:
                topics[y].append(bookNumber)
                found = True
        if found == False:
            topics.append({bookNumber})
except:
    #convert the topics to sets and find the intersections
    for x in range(len(topics)):
        
        
                
                
            
        

        
        
            
