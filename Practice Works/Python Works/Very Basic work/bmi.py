#Q write a program to calculate the bmi of a person where weight and height are input by the user


height = float(input("Enter height in meters: "))
weight = float(input("Enter weight in kilograms: "))
bmi = weight / (height ** 2)
print("Your bmi is:",bmi)
