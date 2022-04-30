import random, sys

def pivot(A, low, high):
    mid = (low + high) // 2
    if A[mid] < A[low]:
        A[low], A[mid] = A[mid], A[low]
    if A[high] < A[low]:
        A[low], A[high] = A[high], A[low]
    if A[mid] < A[high]:
        A[high], A[mid] = A[mid], A[high]
    return A[high]


def partLow(A, l, r):
    # базовый учебный вариант (берем первый эл-т)
    q = A[l]
    j = l
    for i in range(l+1, r+1):
        if A[i] <= q:
            j += 1
            A[j], A[i] = A[i], A[j]
            # print("p={} (ij)=(A[{}]= {} A[{}]= {}) A = {} + {} = {}".format(q, i, A[i], j, A[j], A[l:j+1], A[j+1:r+1], A[l:r+1]))
    A[l], A[j] = A[j], A[l]
    return j if j<r else j-1

def partHigh(A, l, r):
    # разбиение Ломуто (берем последний эл-т)
    q = A[r]
    j = l
    for i in range(l, r):
        if A[i] <= q:
            A[j], A[i] = A[i], A[j]
            j += 1
    A[r], A[j] = A[j], A[r]
    return j if j<r else j-1

def partHoar(A, l, r):
    # разбиение Хоара, справа >=, слева <=
    q = pivot(A, l, r)
    i = l - 1
    j = r + 1
    while (True):
        i += 1
        while (A[i] < q):
            i += 1
        j -= 1
        while (A[j] > q):
            j -= 1
        if (i >= j):
            return j
        A[i], A[j] = A[j], A[i]

def quickSort(A, partition=partLow):
    
    def _qSort2(A, l, r):
        if l >= r:
            return
        m = partition(A, l, r)
        # print('in:',l,r,A[l:r+1])
        _qSort2(A, l, m)
        _qSort2(A, m+1, r)
        
    def _qSort(A, l, r):
        while l < r:
            m = partition(A, l, r)
            _qSort(A, l, m)
            l = m + 1 

    _qSort2(A, 0, len(A)-1)

testPartFuncs = [partLow, partHigh, partHoar]

def test(l=100, N=10):
    for func in testPartFuncs:
        passed = True
        for i in range(l):
            L = [random.randint(1, N) for _ in range(N)]
            L1 = L.copy()
            try:
                quickSort(L, partition=func)
            except Exception as E:
                print(E)
                passed = False
                break
            if L != sorted(L1): passed = False
        print(func.__name__, "OK" if passed else "Failed!")

test()
# L = [random.randint(1,5) for _ in range(10)]
# print(L)
# quickSort(L, partition=partLow)
# print(L)