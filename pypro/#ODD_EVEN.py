#ODD_EVEN
import random
collector=[]
predicted=[]
for i in range(6):
  pred=input("Enter your prediction within 1 to 6 ")
  collector.append(pred)
  cpred=random.randint(1,6)
  predicted.append(cpred)
  if pred ==cpred:
    print("you are caught ")
    break
  else:
    print(" I missed")
print(collector)
print(predicted)