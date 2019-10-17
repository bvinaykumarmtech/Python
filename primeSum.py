def primeSum():
    s = 0
    for x in range(10, 101):
        c = 1
        for y in range(1, x // 2):
            if (x % y == 0):
                c += 1
        if c == 2:
            s += x
    print(s)
primeSum()
