import random
import string

def generate_password():
    print("Welcome to the Password Generator!")
    
    
    length = int(input("Enter the desired length of the password: "))
    
    
    characters = string.ascii_letters + string.digits + string.punctuation
    
    pwd = ""
    for i in range(length):
        pwd+= ''.join(random.choice(characters)) 
    
    print(f"Your generated password is: {pwd}")

generate_password()
