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

# 6) Write a program that takes array of numbers are input, 
# print the second duplicate number and and it’s occurrence

'''list=[64,1,2,7,79,7,7,1,22]

count=0
for i in list:
    if list.count(i)>1:
        count+=1
    if count==2:
        print(f" Secound duplicate number is {i} and it is occured {list.count(i)} times")
        break'''

#Output: Secound duplicate number is 7 and it is occured 3 times
#------------------------------------------------------------------------

# 7) Write a program that takes number of rows as input and print below respective pattern.

'''rows=int(input("Enter number of rows:"))

for i in range(1,rows+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print("\n")'''
    
# Output: 
''' 1
    1 2
    1 2 3
    1 2 3 4 '''

#-------------------------------------------------------------------------

# 8) Write a program that takes number of rows as input and print below respective pattern.

'''rows=int(input("Enter number of rows: "))

for i in range(1,rows+1):
    for j in range(rows,i-1,-1):
        print(j,end=" ")
    print("\n")'''

# Output: 
'''4 3 2 1 

   4 3 2 

   4 3 

   4 '''

#-------------------------------------------------------

# 9) Write a program that takes number of rows as input and print below respective pattern.

'''rows=4
for i in range(1,rows+1):
    sum=0
    for j in range(1,i+1):
        print(j,end=" ")
    for k in range(1,j+1):
        sum+=k
    print(sum,end=" ")
    print("\n")'''

# Output: 
'''1 1 

   1 2 3 

   1 2 3 6 

   1 2 3 4 10 '''
   
#-------------------------------------------------------
# 10) Write a program that takes number of rows as input and print below respective pattern.

'''rows=int(input("Enter number of rows: "))
for i in range(1,rows+1):
    for j in range(1,i+1):
        print(" "*(rows-i),j,end=" "*3)
    print("\n")'''
    
# Output:
'''    1
     1   2
   1   2   3 '''
   
#-------------------------------------------------------

# 11) Write a program that takes number of rows as input and print below respective pattern.


'''rows=4

for i in range(1,rows+1):
    for j in range(1,i+1):
        print(j,end="")
    print("+"*i)
    print("\n")
    '''
# Output:
'''1++++

   12+++

   123++

   1234+'''
#-------------------------------------------------------

# 12) Write a program that takes number of rows as input and print below respective pattern.

'''rows=int(input("Enter number of rows: "))

for i in range(1, rows+1):
    for j in range(1,i+1):
        print("+",end=" ")
    print(i)
    print("\n")'''

# Output:
'''+ 1

   + + 2

   + + + 3

   + + + + 4'''
#-------------------------------------------------------
# 13) Write a program that takes number of rows as input and print below respective pattern.

'''rows=int(input("Enter number of rows: "))

for i in range(1,rows+1):
    for j in range(1,i+1):
        print("+",end=" ")
    for k in range(1,j+1):
        print(k,end=" ")
    print("\n")'''
    
# Output:
'''+1
   ++12
   +++123
   ++++1234'''
   
#-------------------------------------------------------

# 14) Write a program that takes number of rows as input and print below respective pattern.

'''rows=int(input(" Enter number of rows: "))

for i in range(1,rows+1):
    for j in range(1,i+1):
        print(chr(64+j),end=" ")
    print("\n")'''

# Output:  
'''A 
   A B 
   A B C 
   A B C D '''

#--------------------------------------------------------

# 15) Write a program that takes number of rows as input and print below respective pattern.

'''rows=int(input("Enter number of roes: "))

for i in range(1,rows+1):
    for j in range(1,i+1):
        print(" "*(rows-i),chr(64+j),end=" ")
    print("\n")'''

#Output: 
''' A 

  A   B 

 A  B  C 
'''

#------------------------------------------------------

#16) Write a program that takes number of rows as input and print below respective pattern.

'''rows=4

for i in range(1,rows+1):
    for j in range(1,i+1):
        print(chr(64+j),end=" ")
    for k in range(1,j+1):
        print(k,end=" ")
    print("\n")'''

# Output: 
'''A 1 
   A B 1 2 
   A B C 1 2 3 
   A B C D 1 2 3 4 '''

#--------------------------------------------------------------

# 17) Write a program that takes number of rows as input and print below respective pattern.

'''rows=4

for i in range(1,rows+1):
    for j in range(1,i+1):
        if i%2!=0 :
            print(chr(64+j),end=" ")
        else:
            print(chr(96+j),end=" ")
    print("\n")'''

# Output: 
'''A 
   a b 
   A B C 
   a b c d '''
#----------------------------------------------------

# 18) Write a function that rotates an array to the right by a given number of steps.

'''list=[1,2,3,4,5]
no_of_rot=3
new_list=[]


for i in range(len(list)):
    
    new_list.append(list[-(no_of_rot)])
    no_of_rot-=1
print(new_list)'''

# Output: [3, 4, 5, 1, 2]

#------------------------------------------------------

# Write a function that returns the common elements between two arrays.

'''list=[1,2,3]
list2=[2,3,4]
comm_ele=[]

def common(list1,list2):
    for i in range(len(list1)):
        if list[i] in list2:
            comm_ele.append(list[i])
        
    return comm_ele
res=common(list,list2)
print(res)
'''
#Output: [2, 3]

#------------------------------------------------------

# 20) Given an array of consecutive numbers with one missing, find the missing number.

'''list=[1,2,4,5,6,8]
miss_num=[]
for i in range(1,list[-1]):
    if i not in list:
        miss_num.append(i)
print(miss_num)'''
    
#Output : [3, 7]
#------------------------------------------------------

# 21)  Write a function to find the maximum product of two elements in an array.

list=[3,5,-2,8,11]



'''def max_product(list):
    global max,secound_max
    max=list[0]
    secound_max=list[1]
    for i in range(len(list)):
        if list[i]>max and list[i]>secound_max:
            secound_max=max
            max=list[i]
        elif list[i]<max and list[i]>secound_max:
            secound_max=list[i]
    return max,secound_max
res=max_product(list)
print(f"{max} * {secound_max} ={max*secound_max}")'''


# Output: 11 * 8 =88

#------------------------------------------------------

# 22)Write a function that moves all zeros in an array to the end while maintaining the order of other elements.


'''list=[0,1,0,3,12]
list.sort()
def move_zero(list):
    for i in range(len(list)):
        if list[i]==0:
            list.append(list[i])
            list.remove(list[i])
            
    return list
move_zero(list) 
print(list)'''  

# Output: [1,3,12,0,0]
#--------------------------------------------------------

# 23) Write a function to find all pairs in an array whose sum is equal to a given target.


# list=[2,4,3,5,7,8,9]
# sum=7
# res_list=[]
# for i in range (len(list)):
#     loc_list=[]
#     for j in range(1,len(list)):
#         if sum==list[i]+list[j]:
#             loc_list.insert(list[i],list[j])
#     print(loc_list)
#     if loc_list!=[]:        
#         res_list.append(loc_list)
    
# print(res_list)

#-------------------------------------------------------------------------------------
# 24)  Write a function to find a peak element in an array. An element is a peak if it is not smaller than its neighbours.


'''lis=[1, 3, 20, 4, 1, 0]
def peak(lis):
    for i in range(len(lis)-3):
        first=lis[i]
        mid=lis[i+1]
        last=lis[i+2]
        if mid>=first and mid>=last:
            return mid
res=peak(lis)
print(res)'''

#Output: 20

#---------------------------------------------------------------------------------------------

# 25) Write a function to return the first duplicate value in an array.


lis=[2, 1, 3, 5, 3, 2]
# def dup(lis):
for i in range(len(lis)):
        for j in range(len(lis)):
            if lis[i]==lis[j]:
                print(lis[i])
            
            
            
        
    

            
