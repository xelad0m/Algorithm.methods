# последняя цифра в десятичной записи числа Фибоначчи

def fib_digit(n):
    Fn, Fn1 = 1, 0
    for i in range(2, n+1):
        Fn, Fn1 = (Fn + Fn1) % 10, Fn
    if n == 0: Fn = 0
    return Fn    
    

def main():
    for n in range(0,15+1):
        print("F({}) -> {}".format(n, fib_digit(n)))


if __name__ == "__main__":
    main()