

num= int(input("Enter the number you want to reverse: "))

reverse= 0
print(reverse)
while (num!=0):
    digit= int(num % 10)
    reverse= int((reverse*10)) + digit
    num= int(num/10)

print("Reversed number is : ", end="")
print(reverse)
