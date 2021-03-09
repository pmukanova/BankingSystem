import numpy as np
import connection as con
import accounts as ac


class Person():
    def __init__(self, first_name, last_name, age, gender, contact_number, address):
        self.first_name, self.last_name = first_name, last_name
        self.age, self.gender = age, gender
        self.contact_number, self.address = contact_number, address

    @classmethod
    def create(cls, from_db):
        id = from_db  # need to update
        return cls(id)

    @classmethod
    def delete(cls, from_db):
        del cls


class Customer(Person):
    def __init__(self, first_name, last_name, age, gender, contact_number, address, PIN):
        super().__init__(first_name, last_name, age, gender, contact_number, address)
        self.pin = PIN

    def create_profile():
        print("Please,enter your information below to create account.")
        first_name = input("First name: \n")
        if isinstance(first_name, str):
            pass
        else:
            raise TypeError("Please,enter string value")
            create_profile()
        last_name = input("Last name: \n")
        if isinstance(last_name, str):
            pass
        else:
            raise TypeError("Please,enter string value")
            create_profile()
        age = int(input("Age: \n"))
        if isinstance(age, int):
            pass
        else:
            raise TypeError("Please,enter int value")
            create_profile()
        gender = input("Gender: \n")
        if gender in ['M', 'F']:
            pass
        else:
            raise TypeError("Please,enter M or F")
            Customer.create_profile()
        contact_number = int(input("Contact number: \n"))
        if isinstance(contact_number, int):
            pass
        else:
            raise TypeError("Please,enter int value")
            create_profile()
        address = input("Address: \n")
        if isinstance(address, str):
            pass
        else:
            raise TypeError("Please,enter string value")
            Customer.create_profile()
        pin = int(input("Please, set your PIN: \n"))
        if isinstance(pin, int):
            pass
        else:
            raise TypeError("Please,enter int value")
            create_profile()
        Customer.commit_new_customer(first_name, last_name, age,
                                     gender, contact_number, address, pin)

    def create_cust_account(cust_id):
        print("Please select account type: \n ")
        account_type = input("Please, press 1 for Checking account. \n "
                             "Please, press 2 for Savings account. Interest rate is %1. \n ")
        if int(account_type) == 1:
            ac.CheckingAccount.create_account(cust_id, acc_type="Checking")
        elif int(account_type) == 2:
            ac.SavingsAccount.create_account(cust_id, acc_type="Savings")
        else:
            Customer.create_cust_account(cust_id)

    def commit_new_customer(first_name, last_name, age, gender,
                            contact_number, address, pin):
        con.push_data(first_name, last_name, age, gender,
                      contact_number, address, pin)
        print("You have succsesfully created profile with us!")
        customer_id = con.pull_customer_id(pin)
        Customer.create_cust_account(customer_id)


class Employee(Person):
    def __init__(self, first_name, last_name, age, gender, contact_number, address):
        super().__init__(first_name, last_name, age, gender, contact_number, address)
