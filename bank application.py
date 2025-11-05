bank_accounts={}
def create_account():
    acc_number=input("enter the account number:")
    if acc_number in bank_accounts:
        print("Account already exists!")
    else:
        name=input("enter the name of the account holder:")
        bank_accounts[acc_number]={"Name":name, "balance":0}
        print(f"Account created for {name} with account number {acc_number}")
print(bank_accounts)
def deposit():
    acc_number=input("enter the account number:")
    if acc_number in bank_accounts:
        amount=float(input("enter the amount to deposit:"))
        if amount>0:
            bank_accounts[acc_number]['balance']+=amount
            print(f"deposited {amount}.balance {bank_accounts[acc_number]['balance']}")
        else:
            print("invalid deposit amount!")
    else:
        print("account does not exist")
def withdrawl():
    acc_number=input("enter the account number")
    if acc_number in bank_accounts:
        amount=float(input("enter the amount to withdraw:"))
        if 0<amount<=bank_accounts[acc_number]['balance']:
            
            bank_accounts[acc_number]['balance']-=amount
            print(f"amount withdrawn {amount}. Remaining balance {bank_accounts[acc_number]['balance']}")
        else:
            print("insufficient balance!")
    else:
        print("account not found!")
def check_balance():
    acc_number=input("enter the account number:")
    if acc_number in bank_accounts:
        print(f"account holder:{bank_accounts[acc_number]['Name']}")
        print(f"current balance:{bank_accounts[acc_number]['balance']}")
    else:
        print("invalid account number!")
def main():
    while True:
        print("\n--bank menu--")
        print("1.create account")
        print("2.deposit ammount")
        print("3.withdraw ammount")
        print("4.check balance")
        print("5.Exit")
        choice=input("enter your choice:")
        if choice=='1':
            create_account()
        elif choice=='2':
            deposit()
        elif choice=='3':
            withdrawl()
        elif choice=='4':
            check_balance()
        elif choice=='5':
            print("thank you for using our banking application visit us again!!!")
            break
main()
    
