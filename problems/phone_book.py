# phone book

phone_book = {}
while True:
    print("\n1. Add Contact \n2. View Contacts \n3. Remove Contact \n4. Exit")
    choice = int(input("Enter Your Choice: "))
    if choice == 1:
       name= input("Enter Name: ")
       number= int(input("Enter Your Number:"))
       phone_book[name] = number
       print(f'Contact {name} is added with number {number}.')
    elif choice ==2 :
        if phone_book:
          print ("Contacts : ")
        for name,number in phone_book.items():
           print(f'{name} : {number }')
    elif choice == 3 :
       name = input("Enter Name to Remove: ")
       if name in phone_book:
          del phone_book[name]
          print (f'Contact {name} has been deleted')
       else :
          print(f'Contact {name} is not found in phone book.')
    elif choice == 4 :
        print("Exiting Phone Book")
        break
    else :
        print("Enter Valid Choice")