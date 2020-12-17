def allConstruct(word,li):
    return allConstructHelper(word,li,dict())


def allConstructHelper(word,li,memo):
    if word in memo:
        return memo[word]
    if word=='':
        return []
    for w in li:
        if check(word,w):
           result = allConstructHelper(word[len(w):],li,memo)
           memo[word] = result 
           
           if result != None:
               new_result = []
               new_result.append(w)

               for y in result:
                   new_result.append(y)

               memo[word] = new_result 

               return memo[word]


    return None


def check(word,pre):
    if len(word)<len(pre):
        return False
    for x in range (len(pre)):
        if word[x]!=pre[x]:
            return False
    return True 

print(allConstruct('abhishek',['a','dsfsdf','h','k','bcd','e','bhi','s']))