"""
sql = "INSERT INTO customers (first_name, last_name, age, gender,contact_number, address,PIN) VALUES (%s,%s,%s,%s,%s, %s,%s)"
val = [('Peter', 'Malok', '45', 'M', '9173650908', 'Lowstreet 4', "1111"),
       ('Amy', 'Patkinson', '25', 'F', '9893652223', 'Apple st 652', "2223"),
       ('Hannah', 'Li', '36', 'F', '6463653335', 'Mountain 21', "3335"),
       ('Michael', 'Ozman', '28', 'M', '7183658885', 'Valley 345', "8885"),
       ('Sandy', 'Brukhr', '36', 'F', '3214654563', 'Ocean blvd 2', "4563"),
       ('Betty', 'Thompson', '27', 'F', '9294563908', 'Green Grass 1', "3214"),
       ('Richard', 'Thompson', '23', 'M', '9175633214', 'Sky st 331', "7891"),
       ('Susan', 'Alvarez', '18', 'F', '4563650105', 'One way 98', "8523"),
       ('Vicky', 'Minaj', '20', 'F', '4543369808', 'Yellow Garden 2', "3698"),
       ('Ben', 'Tiger', '56', 'M', '5183654562', 'Park Lane 38', "4562"),
       ('William', 'Alison', '63', 'M', '9293645628', 'Central st 954', "8866"),
       ('Chuck', 'Morris', '32', 'M', '4562140908', 'Main Road 989', "9203"),
       ('Viola', 'Dilberg', '55', 'F', '3383650105', 'Sideway 1633', "8105")
       ]
mycursor.executemany(sql, val)
mydb.commit()
"""
    def push_data(f_name, l_name, age, gender, contact_n, address, pin):
        sql1 = "INSERT INTO customers (first_name, last_name, age, gender, contact_number, address, pin) VALUES (%s, %s, %s, %s,%s, %s,%s) "
        sql2 = "("+f_name + "," + l_name + "," + age + "," + gender + \
            "," + contact_n + "," + address + "," + pin+")"
        sql = sql1 + sql2

        return str(sql)


date_created = pd.to_datetime('today')


use banking_system

CREATE TABLE `customers` (`customer_id` INT auto_increment,
                          `first_name` VARCHAR(50),
                          `last_name` VARCHAR(50),
                          `age` int,
                          `gender` VARCHAR(1),
                          `contact_number` VARCHAR(10),
                          `address` VARCHAR(50),
                          `employee_id` INT,
                          `PIN` INT,
                          PRIMARY KEY(`customer_id`),
                          FOREIGN KEY(`employee_id`)
                          references employees(`employee_id`)
                          )

INSERT INTO customers
SELECT * FROM tmp_customers


use banking_system

CREATE TABLE `employees` (`employee_id` INT auto_increment,
                          `first_name` VARCHAR(50),
                          `last_name` VARCHAR(50),
                          `age` INT,
                          `gender` VARCHAR(1),
                          `contact_number` VARCHAR(10),
                          `address` VARCHAR(50),
                          PRIMARY KEY(`employee_id`)
                          )

CREATE TABLE `customers` (`customer_id` INT auto_increment,
                          `first_name` VARCHAR(50),
                          `last_name` VARCHAR(50),
                          `age` int,
                          `gender` VARCHAR(1),
                          `contact_number` VARCHAR(10),
                          `address` VARCHAR(50),
                          `employee_id` INT,
                          `PIN` INT,
                          PRIMARY KEY(`customer_id`),
                          FOREIGN KEY(`employee_id`) REFERENCES employees(`employee_id`)
                          )

CREATE TABLE `accounts` (`account_number` INT auto_increment default 1000000,
                         `customer_id` INT,
                         `account_type` VARCHAR(10),
                         `balance` FLOAT,
                         `date_created` VARCHAR(10),
                         PRIMARY KEY(`account_number`),
                         FOREIGN KEY(`customer_id`) REFERENCES customers(`customer_id`)
                         )

CREATE TABLE `credit_cards` (`creditcard_number` INT auto_increment default 9000000,
                             `customer_id` INT,
                             `date_created` VARCHAR(10),
                             `balance` FLOAT,
                             `minimum_payment` TINYINT DEFAULT 50,
                             `payment_date` VARCHAR(10),
                             `payment_due` VARCHAR(50),
                             PRIMARY KEY(`creditcard_number`),
                             FOREIGN KEY(`customer_id`) REFERENCES customers(`customer_id`)
                             );


use banking_system;
INSERT INTO customers(first_name, last_name, age, gender, contact_number, address, PIN)
 VALUES('Peter', 'Malok', '45', 'M', '9173650908', 'Lowstreet 4', "1111"),
       ('Amy', 'Patkinson', '25', 'F', '9893652223', 'Apple st 652', "2223"),
       ('Hannah', 'Li', '36', 'F', '6463653335', 'Mountain 21', "3335"),
       ('Michael', 'Ozman', '28', 'M', '7183658885', 'Valley 345', "8885"),
       ('Sandy', 'Brukhr', '36', 'F', '3214654563', 'Ocean blvd 2', "4563"),
       ('Betty', 'Thompson', '27', 'F', '9294563908', 'Green Grass 1', "3214"),
       ('Richard', 'Thompson', '23', 'M', '9175633214', 'Sky st 331', "7891"),
       ('Susan', 'Alvarez', '18', 'F', '4563650105', 'One way 98', "8523"),
       ('Vicky', 'Minaj', '20', 'F', '4543369808', 'Yellow Garden 2', "3698"),
       ('Ben', 'Tiger', '56', 'M', '5183654562', 'Park Lane 38', "4562"),
       ('William', 'Alison', '63', 'M', '9293645628', 'Central st 954', "8866"),
       ('Chuck', 'Morris', '32', 'M', '4562140908', 'Main Road 989', "9203"),
       ('Viola', 'Dilberg', '55', 'F', '3383650105', 'Sideway 1633', "8105");

INSERT INTO employees(first_name, last_name, age, gender, contact_number, address)
 VALUES('Scott', 'Taylor', '35', 'M', '9173896398', 'High street 4'),
       ('Laura', 'Lewes', '29', 'F', '9893656623', 'Apple st 5');

INSERT INTO accounts(account_number, customer_id, account_type, balance, date_created)
VALUES('10001', '1', 'checking', '2500.00', '2020-07-01'),
	   ('10002', '2', 'checking', '1500.80', '2020-08-01'),
       ('10003', '3', 'savings', '8005.08', '2020-09-01'),
       ('10004', '4', 'checking', '5500.20', '2020-10-01'),
       ('10005', '5', 'savings', '3000.89', '2020-11-01'),
       ('10006', '6', 'checking', '750.56', '2020-12-01'),
       ('10007', '7', 'checking', '500.12', '2021-01-01'),
       ('10008', '8', 'savings', '10000.60', '2021-02-01'),
       ('10009', '9', 'checking', '2050.75', '2021-01-01'),
       ('10010', '10', 'checking', '8500.14', '2021-02-01'),
       ('10011', '11', 'savings', '8960.45', '2021-05-01'),
       ('10012', '12', 'savings', '12560.23', '2019-04-01'),
       ('10013', '13', 'checking', '6208.50', '2019-05-01'),
       ('10014', '6', 'savings', '8960.45', '2021-01-01'),
       ('10015', '12', 'checking', '2560.23', '2020-04-01'),
       ('10016', '3', 'checking', '6208.50', '2020-05-01');
