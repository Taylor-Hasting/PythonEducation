#This a simple barebones password checker.
#This is to teach the basic understanding of an if else statement.
#Don't use your IT brain here, this is just an example of the statement.


password = 'Password123'


inputed_password = input('please enter the password: ')

inputed_password = str(inputed_password)

if inputed_password == password:
    print('Correct Password')
    print('Access Granted')
else:
    print('Wrong password!!!')
    print('Access Denied!!!')
