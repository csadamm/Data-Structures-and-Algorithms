#Method to apply the operator between 2 values
#We will require the token (as the token will be an operator)
#We also need b and a (the last 2 values added to the stack)
def applyOperator(token, b, a):
    if token == "+":
        result = b + a
    elif token == "-":
        result = b - a
    elif token == "*" or token == "x":
        result = b * a
    elif token == "/":
        result = b / a
    return result
    

expression = input("Enter your expression: ")
#This will split up our expression into individual tokens 
#Ex: 2 5 + will split into ["2", "5", "+"]
tokens = expression.split()
stack = []
#This is used to check if we have an operator
operators = {"+", "-", "/", "*", "x"}

#Sift through every value in our split up expression
for token in tokens:
    #If the string is a digit, we will convert the token to an integer and push it to the stack
    if token.isdigit():
        token = int(token)
        stack.append(token)
        #Print stack at every operation
        print(f"Stack: {stack}")
    #Else if the token is one of our operators we will execute this code
    elif token in operators:
        #Pop out the last 2 values and store them
        a = stack.pop()
        b = stack.pop()
        #Apply the operator to the last 2 values and push the result
        result = applyOperator(token, b, a)
        stack.append(result)
        #Print stack at every operation
        print(f"Stack: {stack}")
    #If its neither a digit nor an operation, we have an invalid input, end program.
    else:
        print("Invalid input")
        
