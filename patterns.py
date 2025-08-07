# 1)
# n=6
# for i in range(n):
#     for j in range(n):
#         if i==0 or i==n-1 or j==0 or j==n-1:
#             print("*",end=" ") 
#         else:
#             print(" ",end=" ")
            
#     print("")

#Output:
# * * * * * * 
# *         * 
# *         * 
# *         * 
# *         * 
# * * * * * * 
#------------------------------------------    
# 
# 2)
# n=4  
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         if j==1:
#             print(" "*(n-i),end=" ")
#         print(i,end=" ")
        
#     print("")

#Output:
#     1 
#    2 2 
#   3 3 3 
#  4 4 4 4 
#----------------------------------------
# 
# 3)
# n=4
# for  i in range(n+1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print("")

#Output:
# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
#-----------------------------------------

# 4)
# n=4

# for i in range(n,0,-1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print("")

#Output:
# 1 2 3 4 
# 1 2 3 
# 1 2 
# 1 
#---------------------------------------
# 5)
# n=4
# k=1
# for i in range(n):
#     for j in range(0,i+1):
        
#         print(k,end=" ")
#         k=k+1
#     print("")

#Output:
# 1 
# 2 3 
# 4 5 6 
# 7 8 9 10 
#--------------------------------------
# 6)
# n=4

# for i in range(1,n+1):
#     for j in range(1,i+1):
#         if (i+j)%2==0:
#             print("1",end=" ")
#         else:
#             print("0",end=" ")
#     print("")

#Output:
# 1 
# 2 3 
# 4 5 6 
# 7 8 9 10 
#---------------------------------------
# 7)
# n=4

# for i in range(n)

#------------------------------
# #8)
# n=5
# for i in range(n):
#     for j in range(n):
#         if j==0:
#             print(" "*i,end="")
#         print("*",end=" ")
#     print("")

#Output:
# * * * * * 
#  * * * * * 
#   * * * * * 
#    * * * * * 
#     * * * * * 
#-------------------------------
#9)
# n=4
# for i in range(n):
#     for j in range(i+1):
#         if j==0:
#             print(" "*(n-i),end="")
#         print("*",end=" ") 
#     print("")
# for i in range(n-2,-1,-1):
#     for j in range(i+1):
#         if j==0:
#             print(" "*(n-i),end="")
#         print("*",end=" ")
#     print("")

#Output:
#     * 
#    * * 
#   * * * 
#  * * * * 
#   * * * 
#    * * 
#     * 
#----------------------------------------
# 10
# n=7
# for j in range(n):
#     for j in range(n):
#         print("*")
        
        
#---------------------------------------
# 11)
# n=6
# for i in range(n):
#     for j in range(n):
#         print("*",end=" ")
#     print("")

#Output:
# * * * * * * 
# * * * * * * 
# * * * * * * 
# * * * * * * 
# * * * * * * 
# * * * * * * 

#---------------------------------------
# 12)

# n=5
# for i in range(n):
#     for j in range(i+1):
#         print("*",end=" ")
#     print("")

#Output:
# * 
# * * 
# * * * 
# * * * * 
# * * * * *
#---------------------------------------
# 13)
# n=5
# for i in range(n,-1,-1):
#     for j in range(i):
#         print("*",end=" ") 
#     print("")

#Output:
#* * * * * 
# * * * * 
# * * * 
# * * 
# * 
#----------------------------------------
# 14)
# n=5

# for i in range(n+1):
#     for j in range(i):
#         if j==0:
#             print("  "*(n-i),end="")
#         print("*",end=" ")
#     print("")
    
#Output:
#         * 
#       * * 
#     * * * 
#   * * * * 
# * * * * * 
#--------------------------------------
#15
# n=5
# for i in range(n,-1,-1):
#     for j in range(i):
#         if j==0:
#             print("  "*(n-i),end="")
#         print("*",end=" ")
#     print("")
    
#Output:
# * * * * * 
#   * * * * 
#     * * * 
#       * * 
#         * 
#--------------------------------------
#16

# n=4

# for i in range(n,0,-1):
#     for j in range(i+1):
#         print("*",end=" ")
#     print("")
    
# for i in range(n+1):
#     for j in range(i+1):
#         print("*",end=" ")
#     print("")
    
#Output:

# * * * * * 
# * * * * 
# * * * 
# * * 
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 

#--------------------------------
#17

# n=5
# for i in range(n+1):
#     for j in range(i):
#         if j==0:
#             print(" "*(n-i),end="")
#         print("*",end=" ")
#     print("")

#Output:
#     * 
#    * * 
#   * * * 
#  * * * * 
# * * * * * 

#------------------------------------
#18

# n=4

# for i in range(n,-1,-1):
#     for j in range(i):
#         if j==0:
#             print(" "*(n-i),end="")
#         print(j+1,end=" ")
#     print("")

#Output:
# 1 2 3 4 
#  1 2 3 
#   1 2 
#    1 
#-----------------------------------
# 19)


#-------------------------------------
# 20)

# n=5

# for i in range(n+1):
#     for j in range(i):
#         if j==0:
#             print(" "*(n-i),end=" ")
#         if (i>=2 and i<n and j>0 and j<(i-1)) :
#             print(" ",end=" ") 
#         else: 
#             print("*",end=" ")
#     print("")
    
#Output:
#      * 
#     * * 
#    *   * 
#   *     * 
#  * * * * * 
#-------------------------------------------------

#21)
# n=5

# for i in range(n,-1,-1):
#     for j in range(i):
#         if j==0:
#             print(" "*(n-i),end=" ")
#         if (i>=2 and i<n and j>0 and j<(i-1)) :
#             print(" ",end=" ") 
#         else: 
#             print("*",end=" ")
#     print("")

#Output:
#  * * * * * 
#   *     * 
#    *   * 
#     * * 
#      * 
#----------------------------------------------


# file=open("file.txt","")





