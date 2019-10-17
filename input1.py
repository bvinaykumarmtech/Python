#Read the input from user until DONE
ip = input('Enter a Number:  ')
while str(ip) != 'DONE':
    if(ip.isdigit()):
        print(ip)
    ip = input('Enter a Number:  ')
