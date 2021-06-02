
def candyStore(candies,N,K):
    diff = N-K
    candies.sort()
    mx = 0
    mn = 0
    for n in range(diff):
        mn += candies[n]
    candies.sort(reverse=True)
    for m in range(diff):
        mx += candies[m]
    return mn,mx
