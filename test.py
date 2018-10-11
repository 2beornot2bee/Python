num=int(input("enter the number to check all its divisior: "))
div_li=[]
for i in range(2,num):
    if num%i==0:
        div_li.append(i)
print(div_li)