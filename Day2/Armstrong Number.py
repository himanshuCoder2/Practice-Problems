i=int(input("Enter the number to check the Armstrong number :- "))
sum=0
digit=i

while(i>0):
    sum=sum+(i%10)*(i%10)*(i%10) # for the cube to generate
    i=i//10   # divide by 10 value of value to loop

if digit == sum:     # digit == sum
    print("Given number is  Armstrong Number")
else:
    print("Given number is not Armstrong Number")