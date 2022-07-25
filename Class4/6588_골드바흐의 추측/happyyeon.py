import sys
input = sys.stdin.readline

# 소수 검증 함수 - 에라토스테네스의 체
def is_prime(n):
    sieve = [True]*(n+1)

    m = int(n**0.5)

    for i in range(2,m+1):
        if sieve[i] == True:
            for j in range(2*i,n+1,i):
                sieve[j] = False

    return sieve

sieve = is_prime(1000000)

while True:
    n = int(input())

    if n == 0:
        break
    
    for i in range(2,n-1):
        if sieve[i] == True and sieve[n-i] == True:
            print("{0} = {1} + {2}".format(n,i,n-i))
            break