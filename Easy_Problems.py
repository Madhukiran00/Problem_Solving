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

# 4) Write a program to print middle character(s) in the given string or number. 

'''str="Wonder"
if len(str)%2==0:
    mid=len(str)//2
    print(str[mid-1:mid+1])
else:
    mid=len(str)//2
    print(str[mid])'''
    
# Output= nd

#-----------------------------------------------------------

# 5) Write a program to check whether the sum of digits in the number except  
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

#6) Write a program to check whether the digits in-between the first and last  
#digit are less than first and last digit, if yes then print true, otherwise print  false.  

'''num=1672
temp=num
last_digit=num%10
num=num//10
count=1
while num!=0:
    quo=num%10
    num=num//10
    if num==0:
        first_digit=quo
    
flag=True
while temp!=0:
    quo=temp%10
    if quo>first_digit and quo<last_digit:
        flag=True
    else:
        print("False")
        flag=False
        break
    temp=temp//10
if flag:
    print("True")'''
    
#Ouput=False
    
#-----------------------------------------------------------

# 7) Write a program to print the vowels in the given string in reverse order.  

'''str="Hello World"
vowels="aeiouAEIOU"
vow=""

for i in str:
    if i in vowels:
        vow+=i
print(vow[::-1])
'''
# Output= ooe

#-----------------------------------------------------------

# 8) Write a program to print the vowels in the given string and repeated  vowel should be printed only single time.  

'''str="Hello World"
vowels="aeiouAEIOU"
vow=""

for i in str:
    if i in vowels:
        if i not in vow:
            vow+=i
print(vow)
'''
# Output= eo

#-----------------------------------------------------------

# 9) Write a program to print the string after removing the duplicate characters  in the string.  

'''str="madam"
uniq=""
for i in str:
    if str.count(i)==1:
        uniq+=i
print(uniq)'''

# Output= d

#-----------------------------------------------------------
 
 # 10) Write a program to convert all the upper case letters in the given string to  lower case letter and vice versa

'''str="JohnWick"
new_str=str.swapcase()
print(new_str)'''

#Output=jOHNwICK

#-----------------------------------------------------

# 11) Write a program to print all the Upper case letters in the string in reverse  order and then followed by the lower case letters 

'''str="NumberOne"
upp_case=""
low_case=""

for i in str:
    if ord(i)>=65 and ord(i)<=90:
        upp_case+=i
    else:
        low_case+=i
print(upp_case[::-1]+low_case)'''

#Output:ONumberne  

#------------------------------------------------------------------------

# 12) Write a function to return the largest number in an array. 


'''list=[3,4,1,5,9]
def max_num(list):
    return max(list)
res=max(list)
print(res)'''

#output= 9

#-------------------------or -----------------

'''list=[3,1,4,1,5,9]

def max_num(list):
    max=list[0]
    for i in list:
        if i>max:
            max=i
    return max
print(max_num(list))'''

#Output= 9

#--------------------------------------------------
# 13)  Write a function to return the second largest number in an array. 

'''list=[3,1,4,1,5,9]
list.sort(reverse=True)
max_num=max(list)
def secound_max(list):
    for i in list:
        if i<max_num:
            return i
print(secound_max(list))
    '''
#Output= 5

#---------------------------or-------------------

'''list=[3,1,4,1,5,9]

def Secound_max(list):
    max=list[0]
    secound_max=list[1]
    for i in list:
        if i>max and i>secound_max:
            secound_max=max
            max=i
        if i<max and i>secound_max:
            secound_max=i
    return secound_max

print(Secound_max(list))'''
        
#Output= 5

#--------------------------------------------------

# 14) Write a function that returns the sum of all elements in an array.

'''list=[1,2,3,4,5]
def sum(list):
    sum=0
    for i in list:
        sum+=i
    return sum

print(sum(list))'''

#Output= 15

#--------------------------------------------------

# 15) Write a function to remove duplicate values from an array. 

'''list=[1,2,3,4,5,1,2,3]

def remove_duplicates(list):
    uniq=[]
    for i in list:
        if list.count(i)==1:
            uniq.append(i)
    return uniq
print(remove_duplicates(list))
    '''
    
#Output: [4,5]

#-----------------------------------------------------

# 16)  Write a function to check if an array is sorted in ascending  

'''list=[1,2,3,4,5]

def sorted(list):
    n=list[0]
    global Flag
    Flag=True
    for i in list:
        if i>=n:
            n=i
        else:
            Flag=False
            break
    return Flag
sorted(list)           

if Flag:
    print(True)
else:
    print(False)
'''

# Output= True

#-----------------------------------------------------

# 17) Write a function to reverse the elements in an array. 

'''list=[1,2,3,4,5]
def reverse(list):
    return list[::-1]

print(reverse(list))
'''
#Output= [5, 4, 3, 2, 1]

#------------------------------- or --------------------

'''list=[1,2,3,4,5]
def reverse(list):
    rev_list=[]
    for i in range(len(list)-1,-1,-1):
        rev_list.append(list[i])
        
    return rev_list
print(reverse(list))'''

# Output = [5, 4, 3, 2, 1]

#----------------------------------------------------

# 18) Write a function that removes all falsy values from an array.  Falsy values include false, 0, "", null, undefined, and None . 

'''list=[0,1,"false",2,'',3]
def dup(list):
    new_list=[]
    items=["false",0,"",'',"null","undefined","NaN"]
    for i in list:
        if i not in items:
            new_list.append(i)
    return new_list

print(dup(list))
            '''
#Output= [1, 2, 3]

#-----------------------------------------------------

# 19)  Write a function to find the unique elements in an array  (elements that appear only once).

'''list=[1,2,2,3,4,4,5]

def uniq(list):
    uniq=[]
    for i in list:
        if list.count(i)==1:
            uniq.append(i)
    return uniq
print(uniq(list))'''

#Output= [1, 3, 5]

#-----------------------------------------------------

# 20) Write a function that returns the sum of all even numbers in an  array. 

'''list=[1,2,3,4,5,6]

def sum_even(list):
    sum=0
    for i in list:
        if i%2==0:
            sum+=i            
    return sum
print(sum_even(list))'''

#Output= 12

#-----------------------------------------------------

# 21)  Write a function to reverse a given string.

'''str="hello"

def rev_str(str):
    return str[::-1]

print(rev_str(str))'''

#Output= olleh

#-----------------------------------------------------

# 22)  Write a function to check if a given string is a palindrome.

'''str="madam"
def palindrome(str):
    if str==str[::-1]:
        return True
    else:
        return False
print(palindrome(str))'''

#Output= True

#-----------------------------------------------------

# 23)  Write a function to count the number of vowels in a given string.

'''str="hello world"

def counnt_vowels(str):
    vowels="aeiouAEIOU"
    count=0
    for i in str:
        if i in vowels:
            count+=1
    return count
print(counnt_vowels(str))'''

#Output= 3

#-----------------------------------------------------

# 24)  Write a function to remove all vowels from a given string.

'''str="hello world"

def remove_vowels(str):
    vowels="aeiouAEIOU"
    for i in str:
        if i in vowels:
            str=str.replace(i,"")
    return str
print(remove_vowels(str))'''

#Output= hll wrld   

#-----------------------------------------------------

# 25)  Write a function that converts a string to title case (capitalize the first letter of each word).

'''str="hello world"

def title_case(str):
    return str.title()
print(title_case(str))'''

#Output= Hello World

#-----------------------------------------------------

#26) Write a function to convert a string to a number (without using parseInt or Number).

'''str="12345"

def str_to_num(str):
    num=0
    for i in str:
        num=num*10+ord(i)-ord('0')
        
    return num
print(str_to_num(str))
'''
#Output= 12345

#-----------------------------------------------------

# 27) Write a function to check if a string contains only numeric digits.

'''str="12345"
def is_num(str):
    for i in str:   
        if not i.isdigit():
            return False
    return True
        
print(is_num(str))'''
         
#Output= True

#-----------------------------------------------------

# 28)Write a function that counts the occurrences of a specific character in a string.

'''str="hello world"

def count_char(str,char):
    count=0
    for i in str:
        if i==char:
            count+=1
    return count
print(count_char(str,'l'))
'''

#Output= 3

#-----------------------------------------------------

# 29)  Write a function that converts an array of key-value pairs into an object.

'''list=[["name","Alice"],["age",25]]

def object(list):
    obj={}
    for i in list:
        obj[i[0]]=i[1]
    return obj
print(object(list)) '''

#Output= {'name': 'Alice', 'age': 25}

#-----------------------------------------------------

# 30)  Write a function that merges two objects, giving priority to the properties of the second object in case of conflict.

'''obj1={'a':1,'b':2}
obj2={'b':3,'c':4}

def merge(obj1,obj2):
    for i in obj2:
        obj1[i]=obj2[i]
    
    return obj1
print(merge(obj1,obj2))'''

#Output= {'a': 1, 'b': 3, 'c': 4}

#-----------------------------------------------------

# 31)  Write a function that returns the number of properties in an object.

'''obj={'a':1,'b':2,'c':3}

def count_prop(obj):
    count=0
    for i in obj:
        count+=1
    return count
print(count_prop(obj))'''

#Output= 3

#-----------------------------------------------------

# 32) Write a function that returns an array of all the values in an object.

'''obj={'a':1,'b':2,'c':3}

def values(obj):
     val=[]
     for i in obj:
         val.append(obj[i])
     return val

print(values(obj))'''

#Output= [1, 2, 3]

#---------------------------------------------------

# 33)  Write a function to check if an object is empty (i.e., has no properties).

'''obj={}

def is_empty(obj):
    if len(obj)==0:
        return True
    else:
        return False
print(is_empty(obj))'''

#Output= True

#--------------------------------------------------
