def cal():
    print("Welcome to your Simple Calculator using python!")
    print('''Choose an operation:
    operation no.  operation
    1. Addition (+)
    2. Subtraction (-)
    3. Multiplication (*)
    4. Division (/)
    5. Exit''')

    n1=input("Enter operation choice(e.g. 1 for addition)")
    if n1=='5':
        print("Goodbye!")
        exit()
        
    n2=float(input("Enter 1st Number:"))
    n3=float(input("Enter 2nd Number:"))
    
    if n1=='1':
        print("The addition of the given two numbers is:")
        print(n2+n3)
    elif n1=='2':
        print("The subtraction of the given two numbers is:")
        print(n2-n3)
    elif n1=='3':
        print("The multiplication of the given two numbers is:")
        print(n2*n3)
    elif n1=='4':
        print("The division of the given two numbers is:")
        print(n2/n3)
    
    else:
        print("Invalid operation choice")
        print("You can try again or exit")
        cal()
        
cal()
    
