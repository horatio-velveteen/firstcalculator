
#Writing out my calucltor project, first time ever

#This function will add two numbers
def add(x, y):
    return x + y

#This function will subtract two numbers
def subtract(x, y):
    return x - y

#This function will multiply
def multiply(x, y):
    return x * y

#This function will divide
def divide(x, y):
    return x / y


#now we have our functions, next we going to have instructions

print("Select an operation")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

#Take input from the user
choice = input("Enter choice (1/2/3/4):")

num1 = int(input("Enter your first number:"))
num2 = int(input("Enter your second number:"))

if choice == '1':
    print(num1, '+', num2, '=', add(num1, num2))

elif choice == '2':
    print(num1, '-', num2, '=', subtract(num1, num2))

elif choice == '3':
    print(num1, '*', num2, '=', multiply(num1, num2))

elif choice == '4':
    print(num1, '/', num2, '=', divide(num1, num2))

else:
    print("Invalid input")

