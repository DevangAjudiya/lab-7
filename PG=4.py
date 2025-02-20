#write a program that reads a string from the keyboard and creates dictionary containing frequency of each character occurring in the string
d1={}
st=input("enter the string= ")
for i in range(len(st)):
    key=st[i]
    value=st.count(st[i])
    d2={key:value}
    d1.update(d2)
print(d1)
    
    
    
    
    
