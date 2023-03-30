def knapSack(W, wt, val, n):
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]
    # Build tаble K[][] in bоttоm uр mаnner
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0  or  w == 0:
                K[i][w] = 0
            elif wt[i-1] <= w:
                K[i][w] = max(val[i-1]
                           + K[i-1][w-wt[i-1]],
                               K[i-1][w])
            else:
                K[i][w] = K[i-1][w]
    return K[n][W]

    

if __name__ == '__main__':
    W = 11
    wt = [1, 2, 5, 6, 7]
    pr = [1, 6, 18, 22, 28]
    N = len(pr)

    #Define DP array
    
    maxProfit = knapSack(W, wt, pr, N)
    print(f"Max profit is {maxProfit}")
