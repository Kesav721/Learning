import random
a=int(input("Guess the number between 1 and 100 "))
gen=random.randint(1,100)
while True:
  try:
    
    if a > gen:
        print("Too high!") 

    elif a<gen:
        print("Too low!")

    elif a==gen:
        print("Congratulations!You guessed the number")
        break
  except ValueError:
       print("Please enter a valid number")


