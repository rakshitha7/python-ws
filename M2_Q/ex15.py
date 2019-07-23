def isprime(num):
    if num < 2:
        return False
    else:
        for i in range(2,num//2+1):
            if num % i == 0:
                return False
    return True


num = [i for i in range(1,201)]
lst=list(filter(isprime,num)) 
print(lst)