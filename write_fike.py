from sys import argv

script,filename=argv

print("We're going to erase %s" % filename)
print("If you don't want that, hit ctrl+c.")
print("If you do want that, hit RETURN")

input("?")

print("Opening file...")
target=open(filename,"w")

print("Truncating the file, Good bye!")
target.truncate()

print("Now, I'm going to ask you for three lines")

line1=input("Line1: ")
line2=input("Line2: ")
line3=input("Line3: ")

print("I'm going to write these to the file")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("and finally, we close the file.")
target.close()

