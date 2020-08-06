print("==================================================")
print("This is a program for building a pyramid.")
print("")
print("Enter the number of pyramid layers you want.")
print("==================================================")
number = int(input("Your number : "))
space = " "
print("")
for x in range(number):
    print(space * (number-x) + "*" * (2*x+1))
print("==================================================")
