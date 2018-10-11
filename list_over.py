import random
the_man=random.sample(range(1,50),6)
the_man1=random.sample(range(1,50),6)
the_man2=random.sample(range(1,50),6)
the_man3=random.sample(range(1,50),6)
the_man4=random.sample(range(1,50),6)
the_man5=random.sample(range(1,50),6)
ran=[]
ran2=True
print("Random list 1:", the_man)
print("Random list 1:", the_man1)
print("Random list 1:", the_man2)
print("Random list 1:", the_man3)
print("Random list 1:", the_man4)
print("Random list 1:", the_man5,"\n")

while ran2:
	for number1 in the_man:
		for number2 in the_man1:
			for number3 in the_man2:
				for number4 in the_man3:
					for number5 in the_man4:
						for number6 in the_man5:
							if number1==number2 and number1==number3 and number1==number4 and number1==number5 and number1==number6:
								ran.append(number1)
								print("Random list 1:", the_man)
								print("Random list 1:", the_man1)
								print("Random list 1:", the_man2)
								print("Random list 1:", the_man3)
								print("Random list 1:", the_man4)
								print("Random list 1:", the_man5,"\n")
								if len(ran)!=0:
									ran2=False
									
print("the common value:", ran)
