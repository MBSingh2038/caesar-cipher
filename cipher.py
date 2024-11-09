#Without checking lower and uppercase texts
'''
#Taking a plain sentence as input
input_text = input("Please Enter a Sentence:- ")

#Converting the input text to lowercase
input_text=input_text.lower()

#Initializing the variables
encrypted_text = "" #An empty string
shift_value = 5 #Shift value

for char in input_text:
  #Checking for lower case
  if('a'<= char <='z'):
    new_character = chr((ord(char) - ord('a') + shift_value) % 26 + ord('a'))
    encrypted_text=encrypted_text + new_character
  else:
    encrypted_text+=char

#Displaying the output
print("The entered sentence is:\n",input_text)
print("The encrypted sentence is:\n",encrypted_text)

'''

#Checking the lower and upper case also
'''
#Taking a plain sentence as input
input_text = input("Please Enter a Sentence:- ")

#Initializing the variables
encrypted_text = "" #An empty string
shift_value = 5 #Shift value

for char in input_text:
  #Checking for lower case
  if('a'<= char <='z'):
    new_character = chr((ord(char) - ord('a') + shift_value) % 26 + ord('a'))
    encrypted_text=encrypted_text + new_character
  #Checking for lozer case
  elif('A'<=char<='Z'):
    new_character = chr((ord(char) - ord('A') + shift_value) % 26 + ord('A'))
    encrypted_text=encrypted_text + chr(ord(char)+shift_value)
  else:
    encrypted_text+=char

#Displaying the output
print("The entered sentence is:\n",input_text)
print("The encrypted sentence is:\n",encrypted_text)

'''
#Taking shift value from the user
#Taking input for number of places to be shifted
while True:
  shift=input("Please enter the number of places to shift:- ")
  if(shift.isdecimal()):
    shift_value = int(shift)
    if (0 <= shift_value <= 25):
      break
    else:
      print("You should enter a number between 0 and 25!")
  else:
    print("Please input a valid number")

#Taking input for the plain text
input_text = input("Please Enter a Sentence:- ")

#Initializing an empty encrypted text
encrypted_text = ""

for char in input_text:
  #Checking for lower case
  if('a'<= char <='z'):
    new_character = chr((ord(char) - ord('a') + shift_value) % 26 + ord('a'))
    encrypted_text=encrypted_text + new_character
  #Checking for lozer case
  elif('A'<=char<='Z'):
    new_character = chr((ord(char) - ord('A') + shift_value) % 26 + ord('A'))
    encrypted_text=encrypted_text + chr(ord(char)+shift_value)
  else:
    encrypted_text+=char
  
print("The entered sentence is:\n",input_text)
print("The encrypted sentence is:\n",encrypted_text)

