print("What is your name human?")
name = input()

print()
print("how old are you in years")

age= int(input())
print()

print("input your height in meters")
height = float(input())

print("Input your weight in kilogram: ")
weight = float(input())

print( name + "You are" + str(age) + "body mass index is: ", round(weight / (height * height), 2))
