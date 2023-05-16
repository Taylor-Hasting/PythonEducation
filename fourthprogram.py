password = 'Rainbow'

while True:
    inputed_password = input('Enter the Password: ')
    #uninterruped this will prompt the user to enter the password
    if inputed_password == password:
        break
    #break function will close out of the loop but won't close the program
    #will close the true loop.
    #break out of the loop when the user inputs the correct password
    
print('password correct!')
print('access granted!')
