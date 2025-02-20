d1={(1,54):45466,(1,54):45666,(2,54):44666,(1,54):45466,(1,54):44666,(2,54):4546660,(1,54):44666,(2,54):54666}
ls1=[]
ls2=[]
for k,v in d1.items():
    if(k[0]==1):
        ls1.append(v)
    elif(k[0]==2):
        ls2.append(v)
print("max in diparment1=",max(ls1))
print("max in diparment2=",max(ls2))
        
d1={(1,50):45466,(1,52):45666,(2,34):44666,(1,54):45466,(1,58):44666,(2,64):4546660,(1,84):44666,(2,5):54666}
d2={}
max1=0
k1=0
r1=0
max2=0
k2=0
r2=0
for k,v in d1.items():
    if(k[0]==1):
        if(v>max1):
            max1=v
            k1=k[0]
            r1=k[1]
    elif(k[0]==2):
        if(v>max2):
            max2=v
            k2=k[0]
            r2=k[1]
print("max in diparment1=",k1,r1,max1)
print("max in diparment2=",k2,r2,max2)

d1={(1,54):45466,(1,54):45666,(3,54):44666,(1,54):45466,(1,54):44666,(2,54):4546660,(4,54):44666,(2,54):54666}
d2={}
for k,v in d1.items():
    if k[0] not in d2:
        d2[k[0]]={"max":v,"min":v,"total":v}
    else:
        if(v> d2[k[0]]["max"]):
           d2[k[0]]['max']=v
        elif(v> d2[k[0]]["min"]):
            d2[k[0]]['min']=v
            d2[k[0]]['total']+=v
print(d2)
            
