# Welcome the user
print("Welcome to Adrian's Elite-101 Chatbot!")
# Collect the user’s name and age
name = input("Please input your name:")
age = int(input("Hi! " + name +" please input your age:"))

# Ask the user how it can help them
if(age<15):
    print("Wow " + name + " you are younger than me! How can I help you?")
elif(15<=age<18):
    print("Wow " + name +  " you must be in highschool! How can I help you?")
elif(18<=age<55):
    print("Wow " + name + " you must be an adult! How can I help you?")
elif(55<=age<120):
    print("Wow " + name + " you are older than my parents! How can I help you?")
elif(age<120):
    print("Wow " + name + " you might break a record! How can I help you?")
# Allow the user to choose from a menu/list of options on how they can continue the conversation
print("Please choose one of the following options \n1. Placeholder option 1\n2. Placeholder option 2\n3. Placeholder option 3")
# Add Exit Option in Menu
print("4. End Conversation")
# Add user input for Menu
number = int(input("Enter the number of your choice:"))
#Logic for the final statment
if(number == 1):
    print("Option 1")
elif(number == 2):
    print("Option 2")
elif(number == 3):
    print("Option 3")
elif(number == 4):
    print("Goodbye " + name + " Have a great day!")