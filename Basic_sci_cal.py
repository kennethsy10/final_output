import math

# Function to perform arithmetic operations
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."

def square(x):
    return x ** 2

def square_root(x):
    if x >= 0:
        return math.sqrt(x)
    else:
        return "Error! Negative number."

def power(x, y):
    return x ** y

# Function to display the calculator menu
def display_menu():
    print("\nSelect operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Square")
    print("6. Square Root")
    print("7. Power")
    print("8. View History")
    print("9. Update History")
    print("10. Delete History")
    print("11. Exit")

# Function to handle file operations (CRUD functions)
def write_to_file(result):
    with open("calculator_history.txt", "a") as file:
        file.write(str(result) + "\n")

def read_history():
    try:
        with open("calculator_history.txt", "r") as file:
            history = file.readlines()
        if history:
            print("\nHistory of results:")
            for index, line in enumerate(history, 1):
                print(f"{index}. {line.strip()}")
        else:
            print("No history found.")
    except FileNotFoundError:
        print("No history file found.")
        
def update_history(index, new_result):
    try:
        with open("calculator_history.txt", "r") as file:
            history = file.readlines()
        
        if index > len(history) or index < 1:
            print("Invalid index.")
            return
        
        history[index - 1] = str(new_result) + "\n"
        
        with open("calculator_history.txt", "w") as file:
            file.writelines(history)
        print("History updated successfully.")
    except FileNotFoundError:
        print("No history file found.")

def delete_history(index):
    try:
        with open("calculator_history.txt", "r") as file:
            history = file.readlines()
        
        if index > len(history) or index < 1:
            print("Invalid index.")
            return
        
        del history[index - 1]
        
        with open("calculator_history.txt", "w") as file:
            file.writelines(history)
        print("History deleted successfully.")
    except FileNotFoundError:
        print("No history file found.")

# Main program loop
def main():
    while True:
        display_menu()
        
        choice = input("Enter choice (1-11): ")
        
        if choice in ('1', '2', '3', '4', '5', '6', '7'):
            num1 = float(input("Enter first number: "))
            
            if choice in ('1', '2', '3', '4', '7'):
                num2 = float(input("Enter second number: "))
                
            if choice == '1':
                result = add(num1, num2)
            elif choice == '2':
                result = subtract(num1, num2)
            elif choice == '3':
                result = multiply(num1, num2)
            elif choice == '4':
                result = divide(num1, num2)
            elif choice == '5':
                result = square(num1)
            elif choice == '6':
                result = square_root(num1)
            elif choice == '7':
                result = power(num1, num2)
            
            print(f"Result: {result}")
            write_to_file(result)
        
        elif choice == '8':
            read_history()
        
        elif choice == '9':
            read_history()
            index = int(input("Enter the index number to update: "))
            new_result = input("Enter the new result: ")
            update_history(index, new_result)
        
        elif choice == '10':
            read_history()
            index = int(input("Enter the index number to delete: "))
            delete_history(index)
        
        elif choice == '11':
            print("Exiting the calculator. Goodbye!")
            break
        
        else:
            print("Invalid input, please try again.")

# Run the program
if __name__ == "__main__":
    main()
