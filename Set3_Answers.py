#Problem-1 ==>Find the avg of no in a list

'''list=[4,6,8]
sum=0
len=len(list)
for i in list:
    sum+=i
print(f"Avg:{sum/len}")'''

#Output: Avg:6.0
#---------------------------------
# Problem-2 ==> Count how many times a number appears in a list

'''list=[1,2,2,3,2]
n=2
count=0
for i in list:
    if n==i:
        count+=1
print(count)'''

#Output: 3
#-----------------------------------------------------
# Problem-3 ==>print no grater than 5 from a list

'''list=[2,5,7,8]
temp=[]
for i in list:
    if i>5:
        temp.append(i)
print(temp)'''

# Output: [7, 8]
#-----------------------------------------------
# Problem-4 ==>Replace all 0's with 1's in a list

'''list=[0,1,0,2]
for i in range(len(list)):
    if list[i]==0:
        list[i]=1
print(list)'''

#Output: [1, 1, 1, 2]
#------------------------------------------------
#Problem-5 ==>Print a list in reverse order
'''
list=[1,2,3,4]
print(list[::-1])
'''
#Output:  [4, 3, 2, 1]
#----------------(or)---------

'''list=[1,2,3,4]
temp=[]
for i in range(len(list)-1,-1,-1):
    temp.append(list[i])
print(temp)'''

# Output: [4, 3, 2, 1]
#----------------(or)----------

'''list=[1,2,3,4]
list.sort(reverse=True)
print(list)'''

#Output: [4, 3, 2, 1]
#-------------------------------
# Problem-6 ==>Merge two dictionaries

'''dic1={'a':1}
dic2={'b':2}

for i in dic2:
    dic1[i]=dic2[i]
print(dic1)'''

#Output: {'a': 1, 'b': 2}
#-----------------------------------
# Problem-7 ==>Create a dictionary from two lists
#              (one for keys and one for values)

#Input: ['a','b'],[1,2]

'''dict={}
list1=['a','b']
list2=[1,2]

for i in range(len(list1)):
    dict[list1[i]]=list2[i]
print(dict)'''

#Output: {'a': 1, 'b': 2}
#----------------------------------------------
# Problem-8 ==>Print all values from a dictionary 

'''dict={'x':5,'y':10}
list=[]
for i in dict:
    list.append(dict[i])
print(list)'''

#Output: [5, 10]
#--------------------------------------
#Problem-9 ==>Get the length of a dictionary

'''dict={'a':1,'b':2,'c':3}
print(len(dict))
'''
# Output: 3
#-----------------(or)-----------------

'''dict={'a':1,'b':2,'c':3}
count=0
for i in dict:
    count+=1
print(count)'''

#Output: 3
#---------------------------------------
# Problem-10 ==>List all items in a dictionary as tuple

'''dict={'a':1,'b':2}
print(list(dict.items()))'''

#Output:  [('a', 1), ('b', 2)]
#----------------------------------------
# Problem-11 ==> Find the square of a number

'''num=6
print(6**2)'''

#Output: 36
#-----------------(or)-----------------
'''num=6
squ=1
for i in range(1,3):
    squ=squ*6
print(squ)'''

#Output: 36
#---------------------------------------
# Problem-12 ==>Find the sum of digits of a number

'''num=123
sum=0
while num!=0:
    quo=num%10
    sum=sum+quo
    num=num//10
print(sum)'''

#Output: 6
#-------------------------------------
# Problem-13 ==>Fint the smallest divisior of a number grater than 1

'''num=15
for i in range(2,num,1):
    if num%i==0:
        print(i)
        break'''
    
# Output: 3
#-------------------------------------
# Problem-14 ==> print the multiplication table of a number up to 10

'''num=3
for i in range(1,11):
    print(num*i,end=" ")'''
    
# Output: 3 6 9 12 15 18 21 24 27 30
#----------------------------------------
# Problem-15 ==> To count the number of even digits in a number

'''num=2481
count=0
while num!=0:
    quo=num%10
    if quo%2==0:
        count+=1
    num=num//10
print(count)'''

# Output: 3
#-----------------------------------------





  








