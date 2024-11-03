import math
def is_perfect_square(x):
    s=int(math.sqrt(x))
    return s*s == x
def is_fibonacci(n):
    return is_perfect_square(5*n*n+4) or is_perfect_square(5*n*n-4)
num = int(input())
if is_fibonacci(num):
    print("True")
else:
    print("False")