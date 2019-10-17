#Read the input from user until DONE
while True:
    ip = input('Enter a Number:  ')
    if ip == 'DONE':
        break;
    if(ip.isdigit()):
        print(ip)
