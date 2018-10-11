import datetime
now=datetime.datetime.now()
year=int(now.year)

name=input("What is your name?: ")
print ("your name is ",name)
age=input("What is your age?: ")
age=int(age)
later=100-age
print("you will be 100 years old on ",year+later,".")