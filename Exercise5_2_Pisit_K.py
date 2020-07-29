print("---------------------------------------------------------------------")
print("Hello! This is an application that will help measure your driving speed.")
print("---------------------------------------------------------------------")
s = float(input("How far do you travel (KM): "))         #s = distance (km)
t = float(input("And how long does it take you to drive (hr) : "))    #t = times (hr)

#Specifications to make s,t > 1
if s < 1 :
    print("Error : Please enter a number with one or more values.")
if t < 1 :
    print("Error : Please enter a number with one or more values.")

#Equation (#v = velocity (km/hr), #s = distance (km), #t = times (hr))
v = s/t
print("---------------------------------------------------------------------")
print("This is the speed you use when driving :",v,"Km/hr")

print() # empty line

#Specifications for alert !!
if v >= 100:
    print(">>>> You’re going too fast !!! <<<<")
elif v  <100:
    print(">>>> Great !! You drive carelessly. <<<<")

print("---------------------------------------------------------------------")
print("Thank You For Choosing Us")