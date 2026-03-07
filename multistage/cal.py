print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Modulus")

choice = int(input("Enter choice: "))

a = 20
b = 10

if choice == 1:
    print("Result:", a + b)
elif choice == 2:
    print("Result:", a - b)
elif choice == 3:
    print("Result:", a * b)
elif choice == 4:
    print("Result:", a / b)
elif choice == 5:
    print("Result:", a % b)
else:
    print("Invalid choice")
