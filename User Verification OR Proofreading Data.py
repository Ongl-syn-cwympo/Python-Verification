# User Verification/Proofreading data ~ Asks the user if they accept what they inputed.
# Python code 
# Created by Ongl syn cwympo 
# https://github.com/Ongl-syn-cwympo

# Variables and declarations 
Name = list()
Messages = list()

while input("Say Hello.") == "Hello": 
  
  print("Enter your name")
  Name.append(input()) # Append in Pyhton takes a single argument, which is the item you want to add to the list.
  
  print("Write a short message")
  
  #Confiramtion comes from the user's input being "Yes"
  Message = input()
  if input("Confirm this message by typing in Yes") == "Yes":
    Messages.append(Message) # Append in Pyhton takes a single argument, which is the item you want to add to the list.
    print Name[-1] + ":" + Message # -1 means the last element 
    print("Message confirmed")
    break # Stops the program
  
  else:
    print("Message error ~ Not confirmed")
    print("Have another attempt") 
    # Ouputs an error message if the input is anything other than "Yes"
    # Allows the user to retry entering the data
    
