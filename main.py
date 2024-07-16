# python Banking program


def show_balance(balance):
    print(f"Your balance is  ${balance: 2f}")
    print("* * * * * * * * * * * * * * * * * ")


def deposit():
    amount = float(input("Enter an amount to be deposited: "))
    print("* * * * * * * * * * * * * * * * * ")

    if amount < 0:
        print("* * * * * * * * * * * * * * * * * ")
        print("That's not a valid amount")
        print("* * * * * * * * * * * * * * * * * ")
        return 0
    else:
        return amount


def withdraw(balance):
    print("* * * * * * * * * * * * * * * * * ")
    amount = float(input("Enter amount to be withdraw: "))
    print("* * * * * * * * * * * * * * * * * ")

    if amount > balance:
        print("* * * * * * * * * * * * * * * * * ")
        print("Insufficient funds")

        return 0
    elif amount < 0:
        print("* * * * * * * * * * * * * * * * * ")
        print("Amount must be greater than zero")
        print("* * * * * * * * * * * * * * * * * ")
        return 0
    else:
        return amount

def main():
    balance = 0
    is_running = True

    while is_running:
        print("Banking Program")
        print("* * * * * * * * * * * * * * * * * ")
        print("1.Show Balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Exit")
        print("* * * * * * * * * * * * * * * * * ")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            print("* * * * * * * * * * * * * * * * * ")
            show_balance(balance)
        elif choice == '2':
            print("* * * * * * * * * * * * * * * * * ")
            balance += deposit()
        elif choice == '3':
            balance -= withdraw(balance)
            print("* * * * * * * * * * * * * * * * * ")
        elif choice == '4':
            is_running = False
            print("* * * * * * * * * * * * * * * * * ")
        else:
            print("That is not a valid choice")
    print('Thank you have a nice day')

if __name__ == "__main__":
    main()






