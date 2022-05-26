# ATM Program
import os

def menu(id):
  print ("Press 1 to view account balance")
  print ("Press 2 to withdraw")
  print ("Press 3 to deposit")
  print ("Press 4 to exit")

  try:
    choice = int(input())
    if choice == 1:
      with open(id + ".txt") as f:
        account = f.readlines()
      
      if account:
        print ("Your balance is $" + account[0])
        menu(id)
      else:
        print ("Your balance is $0")
        menu(id)
    elif choice == 2:
      withdraw(id)
      menu(id)
    elif choice == 3:
      print (1)
    else:
      print("Thank you. Goodbye.")
      return
  except:
    menu(id)

def withdraw(id):
  new_balance = 0
  
  with open(id + ".txt") as f:
    balance = f.readlines()
  f.close()

  try:
    amount = int(input("Please enter amount: $"))
  except:
    withdraw(id)

  if amount > int(balance[0]):
    print ("You cannot withdraw more than you have.")
    withdraw(id)

  int_balance = int(balance[0])
  new_balance = int_balance - amount
                    
  fwrite = open(id + ".txt", "w")
  fwrite.write(str(new_balance))
  fwrite.close()

def create_account(id):
  open(id + ".txt", "w")
  menu(id)

def start():
  try:
    id = int(input("Please enter your bank ID: "))
    str_id = str(id)
    if os.path.isfile(str_id + ".txt"):
      menu(str_id)
    else:
      create_account(str_id)
  except:
    start()

start()
#menu("9999")