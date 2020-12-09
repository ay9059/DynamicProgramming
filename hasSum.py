def hasSum(n,li):
    return hasSumHelper(n,li,dict())

def hasSumHelper(n,li,memo):
    if n in memo:
        return memo[n]
    if n<0:
       return None
    if n==0:
        return []
    for x in range(len(li)):
        result = hasSumHelper(n-li[x],li,memo)
        if result!=None:
            resulting_list = []
            for y in result:
                resulting_list.append(y)
            resulting_list.append(li[x])
            memo[n]=resulting_list
            return resulting_list
    memo[n]=None
    return None

print(hasSum(19,[17,18,2]))
                