# login system

pswd = "1234"
attempts = 0

while attempts <3 :
      password = input ("Enter Your Login Password : ")
      if password == pswd:
            print("Login Successful!")
            break
      else:
        print(" Incorrect Password, Try Again")
        attempts += 1
if attempts == 3:
    print(" Account Locked. Too Many Attempts.")