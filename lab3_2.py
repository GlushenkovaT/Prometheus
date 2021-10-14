import sys
import math

fib1=1
fib2=1

n = input ("Введите число из ряда Фибоначчи : ")
n = int(n)

#Условие
i=2
while i < n:
	fib_sum = fib2+fib1
	fib1 = fib2
	fib2 = fib_sum
	i+=1

print (fib_sum)