#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

bills = float(input("What was the total bills? $ "))
tips = int(input("How much tip would u like to give? 10, 12 or 15? "))
people = int(input("How many people would you want to split? "))
total_bills = tips / 100 * bills + bills
bills_each_person= total_bills / people
finnal_bills = "{:.2f}".format (bills_each_person)
print(f"Your Total Bills is: ${total_bills} ")
print(f"Each person should pay: ${finnal_bills}")