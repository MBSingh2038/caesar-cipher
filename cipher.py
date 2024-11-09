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
