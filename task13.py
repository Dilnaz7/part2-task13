x = int(input("Enter the number: "))
print("All the squares in the given range are:")
for number in range(1, x+1): 
    number=number**2
    if number<=x:
        print(number)
        

