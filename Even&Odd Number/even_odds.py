numbers = float(input("Enter your numbers to check either even or odd: "))



prcise_number = "{:.2f}".format(numbers)
print(f"Your number is: {prcise_number}")
if numbers % 2 == 0:
    print("Its an even number")
else:
    print("Its an odd number")