#TEST
def gridTraveller(m,n):
   memo = [[0 for i in range(n+1)] for x in range (m+1)]
   return gridTravellerHelper(m,n,memo)

def gridTravellerHelper(m,n,memo):
    if memo[m][n]!=0: 
        return memo[m][n]
    if m == 1 and n == 1:
        return 1
    if m == 0 or n == 0:
        return 0
    memo[m][n] = gridTravellerHelper(m-1,n,memo) + gridTravellerHelper(m,n-1,memo)
    return memo[m][n]
print(gridTraveller(18,18))