def fibonacci(n):
    ''' takes in one num and retruns the fibonacci formula of that number'''
    if n<=0:
        return 0
    elif n==1:
        return 1
    elif n==2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

def lucas(n):
    '''takes in one num and returns the lucas formula of that number'''
    if n < 0:
        print('nahhhh')
    elif n==0:
        return 2
    elif n==1:
        return 1
    else:
        return lucas(n-1)+lucas(n-2)

def sum_series(n, x = 0, y = 1):
    '''takes in one necessary parameter and two optional params'''
    if n<0:
        print('NAHHHH')
    elif n == 0:
        return 2
    elif n == 1:
        return 1
    elif n == 2:
        return 3
    elif n == 3:
        return 4
    else:
        return sum_series(n - 1, x, y) + sum_series(n - 2, x, y)
