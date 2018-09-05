num=int(input("please enter a number: "))
y=[]
for i in range(2,num):
	if num%i==0:
		y.append(i)
print(y)