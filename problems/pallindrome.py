# pallindrome - function to chk string is pallindrom or not

def palindrome():
    user_input = input("Enter a string: ")
    if user_input == user_input[::-1]:
        if user_input.isalpha():
            print("✅ YES! Given string is a palindrome.")
        print("✅ YES! Given string is a palindrome.")
    else:
        print("❌ NO, Given string is not a palindrome.")

palindrome()