def prime(num):
    c = 1
    for i in range(1, num // 2):
        if num % i == 0:
            c += 1
    if c == 2:
        print('Number is Prime')
    else:
        print('Not a Prime')

prime(2)
