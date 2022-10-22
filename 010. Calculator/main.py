import art
from replit import clear
def add(n1,n2):
  return n1+n2
def sub(n1,n2):
  return n1-n2
def multiply(n1,n2):
  return n1*n2
def div(n1,n2):
  return n1/n2
op_dict={
  "+":add,
  "-":sub,
  "*":multiply,
  "/":div,
}

def calculator():
  print(art.logo)
  n1=float(input("Enter first number: "))
  print("What operation would you like to do")
  for key in op_dict:
    print(key)
  op=input("Pick an operation from the line above: ")
  n2=float(input("Enter second number: "))
  answer=float(f"{op_dict[op](n1,n2):.2f}")
  print(f"{n1} {op} {n2} = {answer}")
  
  calc_running = True
  while(calc_running):
    switch=input(f"type 'y' to continue calculating with {answer}, type 'n' to exit, type 'r' to begin a new calculation: ")
    if(switch== 'y'):
      answer_prev=answer
      op=input("Pick an operation: ")
      nx=float(input("Enter next number: "))
      answer=float(f"{op_dict[op](answer,nx):.2f}")
      print(f"{answer_prev} {op} {nx} = {answer}")
    elif(switch=='n'):
      print("Thank you")
      calc_running = False
    elif(switch== 'r'):
      calc_running = False
      clear()
      calculator()
    else:
      print("Invalid input. Exiting")
      calc_running= False
calculator()







