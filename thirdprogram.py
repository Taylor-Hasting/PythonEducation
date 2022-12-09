inputed_number = input('Specify any Number you want ')
inputed_number = int(inputed_number)
print(inputed_number)

if inputed_number > 0:
    print('inputed number: ' + str(inputed_number) + ' is bigger than 0.')
elif inputed_number == 0:
    print('inputed number: ' + str(inputed_number) + ' is 0, you muppet.')
else:
    print('inputed number: ' +str(inputed_number) + ' is smaller than 0.')
