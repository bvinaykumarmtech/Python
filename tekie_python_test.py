# Write a python program that finds the second largest number from a given list of numbers.
'''Examples:
Input : list_1 = [15, 23, 9]
Output: 15

Input : list_2 = [79, 13, 29, 7, 200]
Output: 79'''
list_1 = [15, 23, 9]
list_1.sort()
print(list_1[1])

# 2. Given a positive integer N, write a program in python that checks if the number is prime or not.

'''Definition: A prime number is a natural number greater than 1 that has no positive divisors other
than 1 and itself. The first few prime numbers are {2, 3, 5, 7, 11, ….}.

Examples :
Input:  n = 13
Output: true

Input:  n = 21
Output: false

Input:  n = 29
Output: true'''
N = int(input())
if N > 1:
        for i in range(2, N):
                if (N % i) == 0:
                        print("false")
                        break
        else:
                print("true")  
else:
        print("false")


