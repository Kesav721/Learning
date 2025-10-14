Op=input(" enter the device ").upper()
logic1=int(input("Enter the logic A 0/1 "))
logic2=int(input("Enter the logic B 0/1 "))

if Op == "AND":
    if logic1 == 0 & logic2==0:
       print("0")
    elif logic1 ==0 & logic2==1:
       print("0")
    elif logic1 == 1 & logic2==0:
       print("0")
    elif logic1 ==1 & logic2==1:
       print("1")
if Op == "OR":
    if logic1 == 0 & logic2==0:
       print("0")
    elif logic1 ==0 & logic2==1:
       print("1")
    elif logic1 == 1 & logic2==0:
       print("1")
    elif logic1 ==1 & logic2==1:
       print("1")
if Op == "XOR":
    if logic1 == 0 & logic2==0:
       print("0")
    elif logic1 ==0 & logic2==1:
       print("1")
    elif logic1 == 1 & logic2==0:
       print("1")
    elif logic1 ==1 & logic2==1:
       print("0")
if Op == "XNOR":
    if logic1 == 0 & logic2==0:
       print("1")
    elif logic1 ==0 & logic2==1:
       print("0")
    elif logic1 == 1 & logic2==0:
       print("0")
    elif logic1 ==1 & logic2==1:
       print("1")

if Op == "NAND":
    if logic1 == 0 & logic2==0:
       print("1")
    elif logic1 ==0 & logic2==1:
       print("1")
    elif logic1 == 1 & logic2==0:
       print("1")
    elif logic1 ==1 & logic2==1:
       print("0")
if Op == "NOR":
    if logic1 == 0 & logic2==0:
       print("1")
    elif logic1 ==0 & logic2==1:
       print("0")
    elif logic1 == 1 & logic2==0:
       print("0")
    elif logic1 ==1 & logic2==1:
       print("0")
if Op=="NOT":
    if logic1==0:
       print("1")
    elif logic1==1:
       print("0")
    else :
      print("Not allowed")
    