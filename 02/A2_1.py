def evaluate_postfix(expression):
    stack = []  # Stack declaration to implement and evaluate Postfix.
    
    # Defining functions for evaluation. 
    operators = {'+': lambda x, y: x + y,  
                 '-': lambda x, y: x - y,
                 '*': lambda x, y: x * y,
                 '/': lambda x, y: x / y} 

    # loop for iterating over the expression.
    for token in expression:
        # condition to check if the token is digit/operator
        if token.isdigit(): 
            stack.append(float(token))
        elif token in operators:
            if len(stack) < 2:
                raise ValueError("Invalid expression")
            
            # pop from stack and push the value in the operator1 and operator 2.
            operand2 = stack.pop()
            operand1 = stack.pop()
            result = operators[token](operand1, operand2)
            stack.append(result)
        
        # If there is anything other than operator and digit raise error.
        else:
            raise ValueError("Invalid token: {}".format(token))

    if len(stack) != 1:
        raise ValueError("Invalid expression")
    return stack[0]

# Taking input from user
postfix_exp= input("Enter Postfix expression: ") 

# Function call to calculate the expression.
result = evaluate_postfix(postfix_exp)

# Display result
print("Result: ", result)