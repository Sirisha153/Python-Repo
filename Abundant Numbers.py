def sum_of_divisors(n):
    total = 0
    for i in range(1,n//2+1):
        if n % i ==0:
            total +=i
    return total
def is_abundant(n):
    return sum_of_divisors(n)>n
num = int(input())
if is_abundant(num):
    print("True")
else:
    print("False")