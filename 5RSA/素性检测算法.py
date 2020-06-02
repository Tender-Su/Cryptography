import random
import time

def fast_power(base, power, n):
    """
    快速模幂运算
    """
    result = 1
    tmp = base
    while power > 0:
        if power&1 == 1:
            result = (result * tmp) % n
        tmp = (tmp * tmp) % n 
        power = power>>1
    return result

def Miller_Rabin(n, iter_num):
    # 2 is prime
    if n == 2:
        return True
    # if n is even or less than 2, then n is not a prime
    a=n&1
    if n&1 == 0 or n<2:
        return False
    # n-1 = (2^s)m
    m,s = n - 1,0
    while m&1==0:
        m = m>>1
        s += 1
    # M-R test
    for _ in range(iter_num):
        b = fast_power(random.randint(2,n-1), m, n)
        if b==1 or b== n-1:
            continue
        for __ in range(s-1):
            b = fast_power(b, 2, n)
            if b == n-1:
                break
        else:
            return False
    return True

if __name__ == "__main__":
    # example
    print(Miller_Rabin(145235345,10))