def fib(n):
    Fn, Fn1 = 1, 0
    for i in range(2, n+1):
        Fn, Fn1 = Fn + Fn1, Fn
    if n == 0: Fn = 0
    return Fn    
    

def main():
    for n in range(85,86+2):
        print("F({}) = {}".format(n,fib(n)))


if __name__ == "__main__":
    main()