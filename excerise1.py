first_number = input("Enter the first number: ") 
second_number = input("Enter the second number:")

temp = first_number
first_number = second_number
second_number = temp    

print("The value of the first number after swapping: {}".format(first_number))
print("The value of the second number after swapping: {}".format(second_number))