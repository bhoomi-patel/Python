# lucky number 

luky_number = 7
gusse = 0 

while gusse != luky_number:
    gusse = int(input("Enter lucky number: "))
    if gusse < luky_number:
        print("Your lucky number is higher than this")
    elif gusse > luky_number:
        print("Your lucky number is lower than this")
    else:
        print("Congratulations! You guessed the lucky number!")
print ("you win")