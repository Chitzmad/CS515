# Function to check if the expressionis balanced in terms of Parenthesis, square and curly.
def is_balanced(expression):
    # Declaration of stack to implent code.
    stack = [] 

    # Defining Dictionary to store key value pairs of brackets.
    opening_brackets = {'(': ')', '[': ']', '{': '}'}
    closing_brackets = {')', ']', '}'}

    for char in expression:
        # If there is opening bracket then add it to stack
        if char in opening_brackets:
            stack.append(char)
        
        # If there is closing bracket then 2 conditions to take care of.
        elif char in closing_brackets:
            # if stack empty.
            if not stack:
                return False
            # if not empty then compare it to the opening pair to return true/false.
            last_opening_bracket = stack.pop()
            if opening_brackets[last_opening_bracket] != char:
                return False

# length of stack used to determin the number of pairs of brackets.
    return len(stack) == 0

# Taking input from the user
expression = input("Enter an expression: ")
if is_balanced(expression):
    print("The expression has balanced parentheses, square brackets, and curly braces.")
else:
    print("The expression does not have balanced parentheses, square brackets, or curly braces.")
