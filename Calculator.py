# Creating an easy Calculator using Python


print ('''
 _____________________
|  _________________  |
| |                 | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|''')

print("Welcome the python Calculator\n")

# Functions for performing the opearations

#for addition
def add(n1,n2):
    return n1+n2

#for substraction
def sub(n1,n2):
    return n1-n2

#for multiplication
def mul(n1,n2):
    return n1*n2

#for division
def div(n1,n2):
    return n1/n2

#for findindg modulas
def mod(n1,n2):
    return n1%n2

#list of all the operations
operations = {
    "+" : add,
    "-" : sub,
    "*" : mul,
    "/" : div,
    "%" : mod
    }
# Use the dictionary operations 
#Defing a function to call all the operaations 

def Calculator():
    #Asking the user for further operations with the answer
    should_accumulate = True
    
    num1 = float(input("Please enter the first number >>>  "))

    while should_accumulate:
        for keys in operations :
            print(keys)
        operation = input("Please pick any operation ? ")
        num2 = float(input("Please enter the second number ? "))
        answer = (operations[operation](num1,num2))
        print(f"{num1} {operation} {num2} = {answer}")

        choice = input("Type 'y' to continue if you want to continue the calculations with {answer} else type 'n' " )

        if choice == 'y':
            num1 = answer
        else:
            should_accumulate = False
            print("\n"*20)
            Calculator()

Calculator()

