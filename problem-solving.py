# name="madhukiran"
# new_list=[]
# for i in range(len(name)):
#     var=name[i]
#     count=0
#     for j in range(len(name)):
#         if  var==name[j]:
            
#             count+=1
#     if  var not in new_list:
#         new_list.extend([name[i],count])
        
# for i in range(0,len(new_list),2):
#     print(new_list[i],new_list[i+1])
      
# print("\n")


# #=---------------------------------------

# name="madhukiran"
# di={}
# for ch in name:
#     di[ch]=di.get(ch,0)+1
    
# for ch,count in di.items():
#     print(ch,count)




# name="ma_dhu_ki_ran_" 
# new_str=" "
# for i in range(len(name)):
#     if name[i]=="_" and i<=len(name)-2:
#         cap_let=(name[i+1]).upper()
#         new_str+=cap_let
        
#     else:
#         if  name[i] !="_" and chr(ord((name[i]).lower())-32)!= new_str[-1]:
#             new_str+=name[i]
# print(new_str)
        
        
# user=input("enter num\n")


# llist=[ ch for ch in name]


# lis=[[1,2,3],[4,5],[6,7,8,9]]
# new_lis=[]
# for i  in range(len(lis)):
#     new_lis.append(len(lis[i]))
# print(max(new_lis))



var="aaaabbbccddggjj"

# di={}

# for i in var:
#     di[i]=di.get(i,0)+1
# print(di)

# print(di.get(i))

# for i in range(len(var)):
#     v=var[i]
# #     for j in range(len(var))
    
# lis=[1,2,3,4]

# lis1=[1,2,3,4]

# print(lis is lis1)

# a=10
# a=11
# print( a is a)


# n="aaavvddsgteehf"
# new_lis=[]
# for i in range(len(n)):
#     var=n[i]
#     count=0
#     for j in range(len(n)):
#         if var==n[j]:
#             count+=1
#     if var not in new_lis:
#         new_lis.extend([n[i],count])
        
# i=0
# while i<len(new_lis)-1:
#     print(new_lis[i],new_lis[i+1])
#     i+=2
        
# lis=[2,8,9,4,5,3]
# max_num=max(lis)
# lis.remove(max_num)
# print(max(lis))

# lis=[2,8,9,4,5,3]
    


# output=[x  for x in range(10) if x%2==0]  
# print(output)   




# user=int(input("Enter the number of items"))
# di={}
# for i in range(user):
#     key,val=input("Enter the key and val ").split()
#     di[key]=val
# print(di)


# list Comprehension

# lis=list(map(int,input("Enter num").split()))
# print(lis)

# lis=input("Enter you name\n")
# li=[x for x in lis] 
# print(li)


# a=list(map(int,input().split()))

# print(a)
    
    
    
# lis=[3,5,7,9,4,3,7]

# fir_sec
# for i in range(len(lis)):
    
# [[1,2],
#  [3,4]]

# r,c=map(int,input().split())
# main=[]
# for i in range(r):
#     sub=[]
  
#     for j in range(c):
#         sub.append(int(input()))
#     main.append(sub)

# print(main)



# lis=[3,5,6,8,9,3]

# fir=lis[0]
# sec=lis[1]

# for i in range(len(lis)):
    
#     if lis[i]>=fir and lis[i]<=sec:
#         sec=fir
#         fir=lis[i]
#     else:
#         if lis[i]<=fir and lis[i]>= sec:
#             sec=lis[i]
        
# print(fir,sec)
        
        
        
# lis=[[1,2,3],[4,5,6],[7,8,9]]
# sum=0
# for i in range(len(lis)): 
#     sum+=lis[i][i]
# print(sum)


# name="madam"
# def palin(name):
#     j=len(name)-1
#     for i in range(len(name)//2):
#             if name[i]!=name[j]:
#                 return False
#             else:
#                 j-=1
#     return True       
# print(palin(name))


num=121
temp=num
res=0
while num!=0:
    rem=num%10
    res=res*10+rem
    num=num//10
print(temp==res)
    
        
        

        

    


        