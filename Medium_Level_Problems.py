# 1) Write a program that takes a string, string should be of even length.
# Divide the string into two equals parts, check the number of vowels 
# in both the parts of the string. If both parts of string have same 
# number of vowels then return true otherwise return false.

'''str="rebels"
vowels="aeiou"
count1=0
count2=0

if len(str)%2==0:
    str1=str[:len(str)//2]
    str2=str[len(str)//2:]
    for i in str1:
        if i in vowels:
            count1+=1
    for j in str2:
        if j in vowels:
            count2+=1
            
if count1==count2: 
    print("True")
else:
    print("False")
'''
#Output: True

#-------------------------------------------------

# 2)Write a program that takes array of numbers as input,
# among the numbers in array, check how many numbers starts 
# with the same digit and ends with the same digits. Print 
# the count of such kind of numbers in the given array.

'''num=[34,88,423,121,2382,10]
count=0
for i in num:
    if str(i)[0]==str(i)[-1]:
        count+=1
print(count)'''

#Output: 3
#-------------------------------------------------
 
# 3)Write a program that takes array of numbers as input,
# among the numbers in array, print the numbers which forms
# a prime number by adding one to it. Print such numbers in
# the given array separated b spaces. 

'''num=[7, 4, 7, 23, 10]

for i in num:
    num=i+1
    count=0
    for i in range(2,num):
        if num%i==0:
            count+=1
    if count==0:
        print(i,end=" ")'''
        
#Output: 4 10
#-------------------------------------------------
 # 4)Write a program that takes array of numbers as input and
 # a number as second input. Check the position of the factorial
 # of the second input number in the given array. Print the position
 # of it. If the factorial of given second input number is not presented
 # in the array then print factorial of  the number is not presented.
 
'''list=[61,4,6,7,120,10]
num=int(input("Enter a number: "))
fact=1
for i in range(1,num+1):
    if i==1:
        fact=1
    else:
        fact=fact*i
if fact in list:
    print(list.index(fact))
else: 
    print(f"facorial of num {num} is not present")'''

#Output: 4
#-------------------------------------------------

# 5) Write a program that takes a number as input,
# print the sum of duplicate numbers in the given number.

'''num=7473183
lis=[]
while num!=0:
    quotient=num%10
    lis.append(quotient)
    num=num//10
sum=0
new_list=list(set(lis))
for i in new_list:
    if lis.count(i)>1:
        sum+=i
print(sum)'''

#Output: 10
#-------------------------------------------------

# 6)Write a program that takes array of numbers are input, 
# print the second duplicate number and 












 



