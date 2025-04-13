def calculator():
    print("📟 Welcome to Simple Calculator")

    try:
        num1 = float(input("🔢 Enter first number: "))
        num2 = float(input("🔢 Enter second number: "))

        print("\nChoose Operation:")
        print("1. ➕ Addition")
        print("2. ➖ Subtraction")
        print("3. ✖ Multiplication")
        print("4. ➗ Division")

        choice = input("Enter choice (1/2/3/4): ")

        if choice == '1':
            result = num1 + num2
            operation = "Addition"
        elif choice == '2':
            result = num1 - num2
            operation = "Subtraction"
        elif choice == '3':
            result = num1 * num2
            operation = "Multiplication"
        elif choice == '4':
            if num2 == 0:
                print("❌ Error: Division by zero is not allowed.")
                return
            result = num1 / num2
            operation = "Division"
        else:
            print("❌ Invalid choice.")
            return

        print(f"\n✅ Result of {operation}: {result}")

    except ValueError:
        print("⚠ Please enter valid numbers.")

if __name__ == "__main__":
    calculator()
