#Q Check if string is palindrome

string=input("Enter the string : ")

string2=string.upper()
reverse=string2[::-1]

if string2 == reverse:
    print("The sentence is palidrome")
else:
    print("The sentence is not palindrome")
