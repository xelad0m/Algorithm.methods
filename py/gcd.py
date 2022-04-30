def gcd(a, b):
    # if a == 0:
    #     return b
    # elif b == 0:
    #     return a
    # elif a >= b:
    #     return gcd(a % b, b)
    # else:
    #     return gcd(a, b % a)

    while a != 0 and b != 0:
        if a >= b:
            a = a % b
        else:
            b = b % a
    return max(a, b)

def main():
    a, b = 18, 35
    print(gcd(a, b))

    a, b = 14159572, 63967072
    print(gcd(a, b))


if __name__ == "__main__":
    main()