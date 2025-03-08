printdata="""addtion +
subtraction-
divition /
multiplication * """
print(printdata)
num_1=eval(input("eneter the number"))
num_2=eval(input("enetr the 2nd number"))
opr=input("enetr the opration")
if opr=="+":
   print(num_1+num_2)
elif opr=="-":
   print(num_1-num_2)
elif opr=="/":
   print(num_1/num_2)
elif opr=="*":
   print(num_1*num_2)
else:
   print("opration is invalid")