def is_palindrome(s):
    s = s.lower().replace(" ","")
    return s ==s[::-1]
input_string = input()
if is_palindrome(input_string):
    print("Palindrome")
else:
    print("Not Palindrome")