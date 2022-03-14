# # Add
# def add(n1, n2):
#   return n1 + n2
  
#   # Subtract
# def subtract(n1, n2):
#   return n1 - n2
  
#   # Multiply
# def multiply(n1, n2):
#   return n1 * n2
  
#   # Divide
# def divide(n1, n2):
#   return n1 / n2


# operations = {
#   '+':add,
#   '-':subtract,
#   '*':multiply,
#   '/':divide
# }

# num1 = int(input("First Number: "))
# pick_operations = input("+\n-\n*\n/\n What operation do you want to pick? ")
# num2 = int(input("Second Number: "))

# for i in operations:
#   if i == pick_operations:
#     function = operations[i]
#     symbol = i
    
# answer1 = function(num1,num2)


# print(f"{num1} {symbol} {num2} = {answer1}") 

# num3 = int(input("Third Number: "))

# pick_operations = input("What operation do you want to pick? ")

# for i in operations:
#   if i == pick_operations:
#     function = operations[i]
#     symbol2 = i
    
# answer2 = function(answer1,num2)

# print(f"{answer1} {symbol2} {num2} = {answer2}") 
from replit import clear
import art

# Add
def add(n1, n2):
  return n1 + n2
  
  # Subtract
def subtract(n1, n2):
  return n1 - n2
  
  # Multiply
def multiply(n1, n2):
  return n1 * n2
  
  # Divide
def divide(n1, n2):
  return n1 / n2


operations = {
  '+':add,
  '-':subtract,
  '*':multiply,
  '/':divide
}


def calculator():  
  print(art.logo)
  
  num1 = float(input("First Number: "))

  continue_input = True
  while continue_input:
    pick_operations = input("+\n-\n*\n/\n What operation do you want to pick? ")
    num2 = float(input("Next Number: "))
  
    cal_function = operations[pick_operations]

      
    answer = cal_function(num1,num2)
    print(f"{num1} {pick_operations} {num2} = {answer}")
  
    continue_ornot = input("Do you want to continue_ornot y/n ") 
    if continue_ornot == "n":
      continue_input = False
      clear()
      calculator()

    else:
      num1 = answer
  
  

calculator()