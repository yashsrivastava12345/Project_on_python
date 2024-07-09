str1=input("Enter a string: ")
strng=None
def Palindrome(strng):
    strng2=""
    for i in strng:
        strng2=i+strng2
    print(strng==strng2)
    pass
Palindrome(str1)