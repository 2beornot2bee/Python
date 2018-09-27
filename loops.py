the_count=[1,2,3,4,5]
fruits=["apples","oranges","pears","apricots"]
change=[1,"penies",2,"dimes",3,"quarters"]


#first for-loop

for number in the_count:
    print(f"This is count {number}")

#same as above

for fruit in fruits:
    print(f"A fruit of type {fruit}")

#mix list  , checks {} side

for i in change:
    print(f"I got {i}")

# an empty list

elements=[]

#then use the range function

for i in range(0,6):
    print(f"Adding {i} to the list.")
    elements.append(i)

# now print therm out

for i in elements:
    print(f"Element was {i}")

elements=range(1,10)

for i in elements:
    print(f"Element was {i}")

    
