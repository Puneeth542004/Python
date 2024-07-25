str=[]
char=0
while True:
    s=input("enter charecter=")
    if(s=='*'):
        break
    else:
        char=char+1
        str.append(s)
print("number of chareters entered:")
print(char)
print(string)
string="".join(string)
print(string2)
u,1,d,s,spl==0,0,0,0,0
for i in range(0,len(string2)):
    if string2[i].isupper():
        u=u+1
    elif string2[i].islower():
        l=l+1
    elif string2[i].isdigit():
        d=d+1
    elif string2[i].isspace():
        s=s+1
    else:
        spl=spl+1
print("uppercase:",u)
print("lowercase",l)
print("digit:",d)
print("spaces:",s)
print("special char:",spl)

