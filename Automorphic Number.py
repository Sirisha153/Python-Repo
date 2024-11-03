def is_automorphic(n):
    square = n*n
    return str(square).endswith(str(n))
num = int(input())
if is_automorphic(num):
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")