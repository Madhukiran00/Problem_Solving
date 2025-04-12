#Problem-1
'''list=[1,2,3,4,5]
sum=0
for i in list:
    sum+=i
print(sum)'''
#------------------------------
#Problem-2
'''list=[4,6,8,9,3,2]
print(max(list))'''

#-------------------------------
#Problem-3
'''list=[1,2,3,4,5,6,7,8,9]
count=0
for i in list:
    if i%2==0:
        count+=1
print(count)'''

#---------------------------------
#Problem-4
'''list=[1,2,3,4,1,2,3,4]
uniq=[]

for i in list:
    if i not in uniq:
        uniq.append(i)
print(uniq)'''

#-----------------------------------
#Problem-5
'''list=[5,1,9,6]
max=max(list)

for i in range(max-1,0,-1):
    if i in list:
        print(i)
        break'''
#-------------------------------------
#Problem-6
str="apple banana applie"
list=str.split(" ")
dict={}
for i in list:
    # dict(i)=list.count(i)
    print(i)