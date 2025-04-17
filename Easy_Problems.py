# 1) Write a program to print the sum of the digits in the number. 

'''num=567
sum=0
while num!=0:
    quo=num%10
    sum+=quo
    num=num//10
print("Sum of the digits in the number is:",sum)
'''
# Output= 18

#-----------------------------------------------------------

# 2)Write a program to print reverse of the given number.

'''num=721
temp=num
rev=0
while num!=0:
    quo=num%10
    rev=rev*10+quo
    num=num//10
print(f"Reverse of the number {temp} is {rev}")'''
# Output= 127

#-----------------------------------------------------------

# 3)Write a program to print factorial of the number.

'''num=5
fact=1
for i in range(5,0,-1):
    fact=fact*i
print(f"factorial of the number {num} is {fact}")
'''
# Output= 120

#-----------------------------------------------------------

# Write a program to print middle character(s) in the given string or number. 

'''str="Wonder"
if len(str)%2==0:
    mid=len(str)//2
    print(str[mid-1:mid+1])
else:
    mid=len(str)//2
    print(str[mid])'''
    
# Output= nd

#-----------------------------------------------------------

#Write a program to check whether the sum of digits in the number except  
#first digit and digit is equal to the sum of first digit and last digit 
# of that  number. If both the sums are equal then print equal otherwise print not  equal  

'''num=75547
lastdigit=num%10
num=num//10
firstdigit=0
sum=0
while num!=0:
    quo=num%10
    if num//10!=0:
        sum=sum+quo
    else:
        firstdigit=quo
    num=num//10

res=sum==(firstdigit+lastdigit)
if res==True:
    print("Equal")
else:
    print("Not Equal")'''
    
# Output= Equal
        
#-----------------------------------------------------------

# Write a program to check whether the digits in-between the first and last  
#digit are less than first and last digit, if yes then print true, otherwise print  false.  

num=1672



