#Problem-1 ==>Sum of elements in a list

'''list=[1,2,3,4,5]
sum=0
for i in list:
    sum+=i
print(sum)'''

# Output: 15
#------------------------------

#Problem-2 ==>Find the largest number in a list

'''list=[4,6,8,9,3,2]
print(max(list))'''

# Output: 9
#-------------------------------

#Problem-3 ==>Count even numbers in a list

'''list=[1,2,3,4,5,6,7,8,9]
count=0
for i in list:
    if i%2==0:
        count+=1
print(count)'''

# Output: 4
#---------------------------------

#Problem-4  ==>Remove duplicates from a list

'''list=[1,2,3,4,1,2,3,4]
uniq=[]
for i in list:
    if i not in uniq:
        uniq.append(i)
print(uniq)'''

# Output: [1, 2, 3, 4]
#-----------------------------------

#Problem-5 ==>Find the secound largest number

'''list=[5,1,9,6]
max=max(list)

for i in range(max-1,0,-1):
    if i in list:
        print(i)
        break'''

# Output: 6
#-------------------------------------

#Problem-6 ==>Count word occurence in a sentence

'''str="apple banana apple"
list=str.split(" ")
dict={}
for i in list:
    var=list.count(i)
    dict[i]=var
print(dict)'''

# Output: {'apple': 2, 'banana': 1}
#---------------------------------------

#Problem-7 ==>Update values of a key in a dictionary
'''dict={'a':1,'b':2}

dict['a']=10
print(dict)'''
#----------------------------------------

#Problem-8 ==>Check if a key exists in a dictionary

'''dict={'x':5,'y':6}
key='x'
for i in dict:
    if i==key:
        print("True")
        break
    else:
        print("False")
        break'''
        
# Output: True
#-------------------------------------

#Problem-9 ==>Print only dictionary keys

'''dict={'name':'avr','age':21}
print(dict.values())'''

# Output: (['avr', 21])
#-------------------------------------

#Problem-10 ==>Add new key-value if key doesn't exist

'''dict={'x':1}
key_val={'y':2}

for i in dict:
    for j in key_val:
        if i==j:
            flag=False
        else:
            flag=True
if flag==True:
    dict[j]=key_val[j]
print(dict)'''

# Output: {'x': 1, 'y': 2}
#-------------------------------------

#Problem-11 ==>Check if a number is even or odd

'''num=9
if num%2==0:
    print("Even")
else:
    print("Odd")'''
    
# Output: Odd

#--------------------------------------

#Problem-12 ==>Find factorial of a number

'''num=5
fact=1
for i in range(1,num+1):
    fact=fact*i
print(fact)'''

# Output: 120
#---------------------------------------

#Problem-13 ==>Check if a number is prime

'''num=13
count=0
for i in range(2,num,1):
    if num%i==0:
        count+=1
if count>0:
    print("Not a Prime")
else:
    print("Prime")'''

# Output: Prime
#--------------------------------------

#Problem-14 ==>Reverse the digit of a number

'''num=1234
temp=0
while num!=0:
    quo=num%10
    temp=(temp*10)+quo
    num=num//10
print(temp)'''

# Output: 4321
#-----------------------------------

#Problem-15 ==>Count the Digits of a number

'''num=789
count=0
while num!=0:
    num=num//10
    count+=1
print(count)'''

# Output: 3
#-----------------------------------

