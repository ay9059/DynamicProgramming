# abhishek
def canConstruct(word,li):
    return canConstructHelper(word,li,dict())

def canConstructHelper(word,li,memo):
    if word in memo:
        return memo[word]
    if word == '':
        return True
    for prefix in li:
        if check(word,prefix):
           new_word = canConstructHelper(word[len(prefix):],li,memo)
           memo[word[len(prefix):]] = new_word 
           if new_word == True:
               memo[word[len(prefix):]] = True
               return True
      
    memo[word] = False
    return False 

def check(word,prefix):

    if len(word)>=len(prefix):
       for x in range (len(prefix)):
          if prefix[x] not in word[x]:
             return False
       return True
    else:
       return False

test = 'ab'
word = 'abc'
print(word[len(test):])
print(word)
print(canConstruct('eeeeeeef',['e','eeeee','ee','eeeee']))

