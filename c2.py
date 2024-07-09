#"""a="13"
#print(type(a))
#this is the way of taking the input integer
"""string=input("Enter a string")
for i in string:
    print(i)"""
#wap to enter alpha-numeric string and count total number of digits
"""sting,c=input("Enter a String" ),0
for i in sting:
    if(i.isdigit()):
        c+=1
        pass
    pass
print(c)"""
#wap to enter alpha-numeric string and count total number of digits and characters
"""sting,c,a1=input("Enter a String: " ),0,0
for i in sting:
    if(i.isdigit()):
        c+=1
        pass
    if(i.isalpha()):
        a1+=1
        pass
    pass
print("number of digits: ",c,"","Number of alphabets",a1)"""
#Swaping of numbers without using third variable
"""a,b=12,13
print(a,b)
a,b=b,a
print(a,b)"""
#Find the sum of the digits
a,sum=input("Enter a number: "),0
for i in a:
    sum=sum+(int(i))
    pass
print(sum)