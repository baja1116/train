def add(x, y):
    return x+y

def subtraction(x,y):
    return x-y

def multiplication(x,y):
    return x*y

def division(x, y):
    return x/y

print(add(5,10))
print(subtraction(5,10))
print(multiplication(5, 10))
print(division(10, 0.5))

print("select an option")
print("1. add")
print("2. subtract")
print("3. multiply")
print("4. divide")

while True:
    choice = input("enter choice: 1, 2, 3, 4 : 1")

    if choice in ('1', '2','3','4'):
        num1 = float(input("enter your first number please: "))
        num2 = float(input("enter your second number please: "))

        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")

        elif choice == '2':
            print(f"{num1} - {num2} = {subtraction(num1, num2)}")
        elif choice == '3':
            print(f"{num1} * {num2} = {multiplication(num1, num2)}")
        elif choice == '4':
            print(f"{num1} / {num2} = {division(num1, num2)}")
        
        next_calculation = input("would you like to do anothe project? Y OR N: ").lower()
        if next_calculation == "n":
            print("please have a wondeful day")
            break
    else:
        print("that was not an option.")


        

