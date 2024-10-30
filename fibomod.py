def fibo(n):                        # function start
    a = 0                           
    b = 1
    if n < 0:
        print("incorrect input")
    elif n==0:
        return 0
    elif n == 1 or n == 2:
        return b
    else:
        for i in range(1, n):
            c = a + b               
            a = b
            b = c
        return b



