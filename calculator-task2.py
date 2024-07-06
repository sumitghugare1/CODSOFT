def calculate(num1, num2, operator):
  """
  Performs the chosen operation on two numbers.

  Args:
      num1: The first number.
      num2: The second number.
      operator: The chosen operation (+, -, *, /).

  Returns:
      The result of the operation.
  """
  if operator == "+":
    return num1 + num2
  elif operator == "-":
    return num1 - num2
  elif operator == "*":
    return num1 * num2
  elif operator == "/":
    if num2 == 0:
      print("Error: Division by zero is not allowed.")
      return None
    else:
      return num1 / num2
  else:
    print("Invalid operator. Please use +, -, *, or /.")
    return None

while True:
  
  try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operator = input("Choose an operation (+, -, *, /): ")
  except ValueError:
    print("Invalid input. Please enter numbers.")
    continue

  result = calculate(num1, num2, operator)
  if result is not None:
    print(f"{num1} {operator} {num2} = {result}")


