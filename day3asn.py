print("Basic calculator")
print("n1)Addition \n2)subtraction \n3)Multiplication \n4)Division \n")
choice = input("enter your choice \n")
num1=float(input("enter number 1 :"))
num2=float(input("enter number 2 :"))
if choice == "1":
    print(num1,"+",num2,"=",(num1+num2))

elif choice =="2":
    print(num1,"-",num2,"=",(num1-num2))

elif choice=="3":
    print(num1,"*",num2,"=",(num1*num2))

elif choice =="4":
    print(num1,"/",num2,"=",(num1/num2))

else:
    print("invalid choice ")

