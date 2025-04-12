#Problem-1 ==>Multiply all elements in a list

'''list=[2,3,4]
mul=1
for i in list:
    mul=mul*i
print(mul)'''

#Output: 24
#--------------------------------------------

#Problem-2 ==>Find minimum value in a list

'''list=[8,3,5]
print(min(list))'''

#Output:3
#---------------------------------------------

#Problem-3 ==>Find count of add numbers in a list

'''list=[2,5,7,8]
count=0
for i in list:
    if i%2==0:
        count+=1
print(count)'''

#Output:2
#----------------------------------------------

#Problem-4 ==> Find difference between max and min

'''list=[4,7,2,9]
max=max(list)
min=min(list)
print(f"Difference of {min} and {max} is {max-min}")
'''
#Output: Difference of 2 and 9 is 7
#--------------------------------------------------

#Problem-5 ==>Sum of only Positive numbers

'''list=[-1,3,5,-2]
sum=0
for i in list:
    if i>0:
        sum=sum+i
print(sum)'''

#Output: 8
#----------------------------------------------------

# Problem-6 ==>Get keys with even values from dict

'''dic={'a':2,'b':3,'c':4}
keys=[]
for i in dic:
    if dic[i]%2==0:
        keys.append(i)
print(keys)'''

# Output: 
#-----------------------------------------------------

# problem-7 ==>invert dictionary (keys become values)

'''dic1={'x':1,'y':2}
dic2={}

for i in dic1:
    dic2[dic1[i]]=i
print(dic2)'''

# Output: {1: 'x', 2: 'y'}
#------------------------------------------------------

#problem-8 ==>Check if two dictionaries are equal

'''dic1={'a':1}
dic2={'a':1}
print(dic1==dic2)'''

# Output: True
#-------------------------------------------------------
#problem=9  ==>Sum all values in dictionary

'''dic={'a':5,'b':10}
sum=0
for i in dic:
    sum=sum+dic[i]
print(sum)'''

# Output: 15
#--------------------------------------------------------

#problem-10  ==>List all values greater than 10

'''dic={'a':8,'b':12,'c':15}
res=[]
for i in dic:
    if dic[i]>10:
        res.append(dic[i])
print(res)'''

# Output: [12, 15]
#---------------------------------------------------------

#Problem-11 ==>Check if number is positive ,negative or zero

'''num=-4
if num==0:
    print("zero")
elif num>0:
    print("Postive")
else:
    print("Negative")'''
    
#Output: Negative
#----------------------------------------------------------

# Problem-12 ==>Generate first 5 even numbers

'''n=5
even_no=[]
i=1
count=0
while True:
    if i%2==0:
        even_no.append(i)
        count+=1
    i=i+1
    if count==n:
        break
print(even_no)'''

# Output: [2, 4, 6, 8, 10]
#-------------(or)-------------------------
'''n=5
lis=[]
for i in range(2,n*2,2):
    lis.append(i)
print(lis)'''
#Output: [2, 4, 6, 8, 10]
#---------------------------------------------

#Problem-13 ==>Find cube of a number 

'''n=3
print(n**3)'''

# Output: 27
#-----------(or)------------

'''n=3
cube=1
for i in range(1,4):
    cube=cube*n
print(cube)'''

#Output: 27
#-----------------------------

# Problem-14 ==>Check if number is multiple of 7

'''num=27
if num%7==0:
    print("Yes")
else:
    print(False)'''
    
# Output: False
#--------------------------------

# Problem-15 ==> Convert number to string and reverse it

'''n=123
res=str(n)
str=res[::-1]
print(f"'{str}'")'''

# Output: '321'
#------------------------------------





