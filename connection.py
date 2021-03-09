import pandas
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Password09",
    database="banking_system"
)


def connect_db(sql, val=0):
    mycursor = mydb.cursor()
    mycursor.execute(sql, val)
    data = mycursor.fetchall()
    mydb.commit()
    return data
    """print(data)
    for x in data:
        print(x)
    """


def push_data(first_name, last_name, age, gender, contact_number, address, pin):
    sql = "INSERT INTO customers (first_name, last_name, age, gender, contact_number, address, pin) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    val = (first_name, last_name, age, gender, contact_number, address, pin)
    connect_db(sql, val)


def pull_data(pin):
    customer_id_list = pull_customer_id(pin)
    sql = "SELECT * FROM customers WHERE PIN = {}".format(pin)
    data = connect_db(sql)
    # show_customer_data(data)
    return data


def pull_customer_id(pin):
    sql = "SELECT customer_id FROM customers WHERE PIN = {}".format(pin)
    customer_id_list = connect_db(sql)
    customer_id = customer_id_list[0][0]
    if customer_id == None:
        invalid_pin()
    return customer_id


def pull_account(customer_id):
    sql = "SELECT * FROM accounts WHERE customer_id = {}".format(customer_id)
    account_data = connect_db(sql)
    return account_data


def pull_balance(account_number):
    sql = "SELECT balance FROM accounts WHERE account_number = {}".format(account_number)
    balance_tuple = connect_db(sql)
    balance = balance_tuple[0][0]
    if balance == None:
        invalid_balance()
    return balance


def push_account(customer_id, account_type, balance, date_created):
    sql = "INSERT INTO accounts (customer_id, account_type, balance, date_created) VALUES (%s, %s, %s, %s)"
    val = (customer_id, account_type, balance, date_created)
    new_acc = connect_db(sql, val)
    print(new_acc)


def invalid_pin():
    pin = input("Invalid PIN entered. Please, retry:")
    pull_cust_id(pin)


def invalid_balance():
    account_number = input("Invalid balance. Please, retry:")
    pull_balance(account_number)


#push_account(31, "checking", 600.00, "2021-03-08")
"""
pull_account(1)
pull_balance(10001)
"""
