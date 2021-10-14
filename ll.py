import sys
x == 1
fib_prev = 0
fib_curr = 1
if x == 0:
    print (fib_prev)
else:
    if x == 1:
        print (fib_curr)
    else:
        for i in range(x-1):
            fib_new = fib_prev + fib_curr
            fib_prev = fib_curr
            fib_curr = fib_new
        print (fib_curr)