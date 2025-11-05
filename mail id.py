mail=input("enter the user's mail id :")
try:
    i=mail.index('@')
    print("your mail id is valid!")
except:
    print("your mail id is invalid!")
