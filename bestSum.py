def bestSum(n,li):
    return bestSumHelper(n,li,dict())

def bestSumHelper(n,li,memo):
    if n in memo:
        return memo[n]
    if n < 0:
        return None
    if n == 0:
        return [] 
    best = None
    for x in range(len(li)):
        result = bestSumHelper(n-li[x],li,memo)
        if result != None:
            result_list = [] 
            for y in result:
                result_list.append(y)
            result_list.append(li[x])

            if best == None or len(result_list) < len(best):
                best = result_list
                memo[n] = result_list
    
    memo[n] = best
    return best
        

print(bestSum(100,[25,2,3,1]))