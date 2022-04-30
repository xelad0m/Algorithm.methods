def naiveBisect(L, d, less_or_equal=True):
    count = 0
    if less_or_equal:
        for l in L:
            if l <= d: 
                count += 1
            else:
                break
        return count
    else:
        for r in reversed(L):
            if r >= d:
                count += 1
            else:
                break
        return count
    
def binaryBisect(a, k, less_or_equal=True):
    # сколько элементов <= (>=) заданного в УПОРЯДОЧЕННОМ массиве
    length = len(a)
    l, r = 0, length
    while l < r:
        m = l + (r - l) // 2
        
        cond1 = (a[m] <= k) if less_or_equal else (a[m] >= k)
        cond2 = ((a[m+1] > k) if (m + 1 < length) else True) if less_or_equal else \
                ((a[m-1] < k) if (m - 1 >= 0) else True)
        cond3 = a[m] > k if less_or_equal else a[m] >= k

        if cond1 and cond2:
            return m + 1 if less_or_equal else length - m
        elif cond3:
            r = m
        else:
            l = m + 1
    return 0

def bisectHoara(A, l, r, k, left=False):
    # разбиение Хоара (максимум слева <= минимум справа) неупорядоченного массива
    # left=True: эл-ты >= опорного сдвигаются вправо (т.е. включая k)
    right = not left
    
    i = l - 1
    j = r + 1 
    while True:
        i += 1
        j -= 1
        while (A[i] < k) if right else (A[i] <= k):
            i += 1
            if i == r + 1:  # если секущая больше максимума
                return j
        while (A[j] > k) if left else (A[j] >= k):
            j -= 1
            if j == l - 1:  # если секущая меньше минимума
                return i
        if i >= j:
            return j   # индексы встретились в массиве
        A[i], A[j] = A[j], A[i]
        

def bisectBentley(A, k, left=False): 
    m = bisectHoara(A, 0, len(A)-1, k)
    if left:
        m1 = bisectHoara(A, 0, m, k)
    else:
        m2 = bisectHoara(A, m+1, len(A)-1, k)
    return m1 if not left else m2


import bisect, random

def test(width=3, n=10):
    L = [random.randint(1, width) for _ in range(n)]
    Ls = sorted(L)
    test_range = range(min(Ls) - 1, max(Ls) + 2)
    
    print('list:', L)
    print('sorted list:', Ls)
    print('k:', list(test_range))
    
    print('hoara  (<= k):', [bisectHoara(L, 0, len(L)-1, i) for i in test_range])
    print('naive  (<= k):', [naiveBisect(Ls, i) for i in test_range])
    print('binary (<= k):', [binaryBisect(Ls, i) for i in test_range])
    print('builtin(<= k):', [bisect.bisect(Ls, i) for i in test_range])
    
    print('hoara  (> k):', [bisectHoara(L, 0, len(L)-1, i, left=True) for i in test_range])
    print('naive  (> k):', [naiveBisect(Ls, i, less_or_equal=False) for i in test_range])
    print('binary (> k):', [binaryBisect(Ls, i, less_or_equal=False) for i in test_range])
    print('builtin(> k):', [bisect.bisect_left(Ls, i) for i in test_range])

    print('naiveBisect is OK:', [bisect.bisect(Ls, i) == naiveBisect(Ls, i) for i in test_range] == [True]*(width+2))
    print('bianryBisect is OK:', [bisect.bisect(Ls, i) == binaryBisect(Ls, i) for i in test_range] == [True]*(width+2))
    print('hoaraBisect is OK:', [bisect.bisect(Ls, i) == bisectHoara(L, 0, len(L)-1, i) for i in test_range] == [True]*(width+2))
    
    
test()
L = [random.randint(1, 5) for _ in range(20)]
Ls = sorted(L)
print('list:', L)
print('sorted list:', Ls)

k = max(L)
print(k)

m = bisectHoara(L, 0, len(A)-1, k=k, left=True)  # включая k
print(m, L)

# random.shuffle(L)
m = bisectHoara(L, 0, len(A)-1, k=k)             # не включая k
print(m, L)