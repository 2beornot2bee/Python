my_list=[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
num=input("please enter a number between 5 to 89: ")
second_list=[]
for element in my_list:
	if int(element)>=int(num):
		break
	second_list.append(element)
print(second_list)