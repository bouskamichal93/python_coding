#Calculator - sum, substract, multiply and divide two input numbers

import os #for terminal clearing
#Functions
def sum(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 == 0:
        print("You can't divide with zero.")
    else:
        return n1 / n2

operations = {
    "+": sum,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
   num1 = float(input("First number: "))
   lets_continue = "yes"
   while lets_continue == "yes":
        for symbol in operations: #write down operators 
            print(symbol)
        user_symbol = input("Choose operation which you want to do: ")
        num2 = float(input("Second number: "))
        calc_function = operations[user_symbol]
        result = calc_function(num1, num2)
        print(f"{num1} {user_symbol} {num2} = {result}")

        lets_continue = input("Write 'yes', if you want to continue. Write 'again', if you want to run calculator again. Write 'no', if you want to end program. ")
        if lets_continue == "yes":
            num1 = result
        elif lets_continue == "again":
            os.system("clear")
            calculator() #recursion
        else:
          print("Thanks for using calculator app. ")
          break    

calculator()
