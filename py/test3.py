D = {}

def calcTD(n, reminder=0):
    # очень долго
    global D
    if reminder == 0:
        if n == 1:
            return 0
        else:
            n3 = calcTD(n // 3, n % 3)
            n2 = calcTD(n // 2, n % 2)
            n1 = calcTD(n - 1, 0)
            
            return D.setdefault(n, 1 + min(n3, n2, n1))
    else:
        return float('inf')


def calcBU(n):
    K = list(range(n+1))
    P = [0] * (n + 1)
    
    found = False
    
    k = 0
    P[1] = 0
    K[1] = 0
    while not found:
        i = 1

        # print(K, P)
        while i < n:
            
            if K[i] == k:
                print('inner', i, k, K[i])
                if i+1 < n:
                    if k < K[i+1]:
                        K[i+1] = k + 1
                        P[i+1] = i
                if 2*i < n:
                    if k < K[2*i]:
                        K[2*i] = k + 1
                        P[2*i] = i
                if 3*i < n:
                    if k < K[3*i]:
                        print('3i', 3*i)
                        K[3*i] = k + 1 
                        P[3*i] = i
                print(K, P)    
            i = i + 1
            
        
        
        k = k + 1
        print(i, k, K[i])
        if k > 2: found = True

             

     
calcTD(10)
calcBU(10)