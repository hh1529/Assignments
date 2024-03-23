def palindrome(n):
    if n==n[::-1]:
        return "the string is palindrome"
    else:
        return "the string is not palindrome"
        
n=input("enter the string : ")
print(palindrome(n))