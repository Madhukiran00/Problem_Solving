name="madhukiran"
new_list=[]
for i in range(len(name)):
    var=name[i]
    count=0
    for j in range(len(name)):
        if  var==name[j]:
            
            count+=1
    if  var not in new_list:
        new_list.extend([name[i],count])
        
for i in range(0,len(new_list),2):
    print(new_list[i],new_list[i+1])
      
print("\n")
#=---------------------------------------

name="madhukiran"
di={}
for ch in name:
    di[ch]=di.get(ch,0)+1
    
for ch,count in di.items():
    print(ch,count)