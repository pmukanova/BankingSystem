import connection as connection
import customer as cust
import accounts as ac


def identify():
    """ Validates type of user. If user type is new customer asks to create profile.
        If user type is exixsting customer, shows customer menu.
        Runs until user enters either 1 or 2.
    """
    print("Welcome to Springboard Banking System!")
    user_type = int(input("Please, press \n1 if you are new customer \n"
                          + "2 if you are existing customer \n"))
    if user_type == 1:
        cust.Customer.create_profile()
    elif user_type == 2:
        show_customer_menu()
    else:
        print("Please, enter 1 or 2")
        identify()


def show_customer_menu():
    """ Asks for customer's pin. Pulls data from db by pin.
        Gets account info from accounts table by customer_id
    """
    pin = input("Please, enter your PIN: \n")
    data = connection.pull_data(pin)
    customer_id = connection.pull_customer_id(pin)
    print("\nHello, {} {}! \n".format(data[0][1], data[0][2]))
    cust_account_info = connection.pull_account(customer_id)
    cust_account_number = select_account(cust_account_info)
    menu_option = display_menu()
    enter_amount(menu_option, cust_account_number)


def select_account(cust_account_info):
    """ Prints customer's accounts list. Asks customer to select account.
        Returns:
            int: account number.
            Primary key of accounts table.
    """
    print("Please, select account from: ")
    account_numbers = []
    for i in cust_account_info:
        account_type = i[2]
        account_num = i[0]
        account_numbers.append(account_num)
        print(account_type.upper(), " account number: {} \n".format(account_num))
    input_number = input("Please, select account number for transaction: \n")
    for account_number in account_numbers:
        if account_number == int(input_number):
            return account_number
        else:
            print("Please, enter valid account number from below. ")
            select_account(cust_account_info)


def display_menu():
    """Displays menu options: Deposit, Withdrawal, Check Balance to a customer.
       Runs until customer enters either 1,2 or 3.
       Returns:
        int: customer choice.
    """
    customer_choice = input("\nPlease, press 1 for Deposit."
                            "\nPlease, press 2 for Withdrawal."
                            "\nPlease, press 3 for Check Balance.\n")
    if int(customer_choice) in [1, 2, 3]:
        return int(customer_choice)
    else:
        print("Please,enter 1,2 or 3")
        display_menu()


def enter_amount(menu_option, account_number):
    """Checks which menu option a customer chose and calls methods accordingly."""
    if menu_option == 3:
        ac.BankAccounts.check_balance(account_number)
    elif menu_option == 2:
        amount = input("Please, enter amount to withdraw.\n")
        ac.BankAccounts.withdraw(amount, account_number)
    elif menu_option == 1:
        amount = input("Please, enter amount to deposit.\n")
        ac.BankAccounts.deposit(amount, account_number)


identify()
