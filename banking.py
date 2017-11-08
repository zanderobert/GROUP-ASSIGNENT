import random

class Bank:
    def __init__(self, BankId, Name, Location):
        self.bank_id = BankId
        self.name = Name
        self.location = Location
        self.customers = {}
        self.tellers = {}
        self.loan = {}
        self.accounts = {}

    def add_accounts_info(self, customer_id, account):
        self.accounts[customer_id] = account

    def add_loan_info(self, customer_id, loan):
        self.loan[customer_id] = loan

    def add_customers(self, customer_id, customer):
        self.customers[customer_id] = customer

    def customers(self):
        return self.customers

    def add_tellers(self, teller_name, teller):
        self.tellers[teller_name] = teller

    def tellers(self):
        return self.tellers

    def toList(self):
        return [self.bank_id, self.name, self.location]


class Customer:
    def __init__(self, Id, cust_Name, Address, PhoneNo, AccNo, bank):
        self.Customer_id = Id
        self.customer_name = cust_Name
        self.Address = Address
        self.phoneNo = PhoneNo
        self.account_no = AccNo
        self.bank = bank

        #self.bank.add_customers(self.Customer_id)

    def add_customer(self, customer):
        self.bank.add_customers(self.Customer_id, customer)

    def General_Inquiry(self):
        pass

    def depositMoney(self, amount):
        if self.bank.tellers:
            teller = random.choice(self.bank.tellers.keys())
            self.bank.tellers[teller].collectMoney()
        my_account = self.bank.accounts[self.Customer_id]
        my_account.add_balance(amount)

    def WithdrawMoney(self, amount):
        my_account = self.bank.accounts[self.Customer_id]
        my_account.subtract_balance(amount)

    def OpenAccount(self, type):
        if self.bank.tellers:
            teller = random.choice(self.bank.tellers.keys())
            self.bank.tellers[teller].openAccount(type, self.Customer_id, self.account_no)

    def CloseAccount(self):
        pass

    def ApplyForLoan(self, amount):
        if self.bank.tellers:
            teller = random.choice(self.bank.tellers)
            teller.loanRequest(amount, self.account_no, self.Customer_id, Type=None)
        else:
            print ('No teller at the moment')

    def RequestCard(self):
        pass


class Teller:
    def __init__(self, Id, teller_name, bank):
        self.teller_id = Id
        self.name = teller_name
        self.bank = bank

        #self.bank.add_tellers(self.name)

    def add_teller(self,teller):
        self.bank.add_tellers(self.name, teller)

    def collectMoney(self):
        print ('%s collecting Money' %(self.name))

    def openAccount(self, type, Customer_id, account_no):
        if type.upper() == 'SAVINGS':
            account = Savings(Customer_id, account_no)
        elif type.upper() == 'CHECKING':
            account = Checking(Customer_id, account_no)
        else:
            print ("Account-types(Checking or Savings)")

        self.bank.add_accounts_info(Customer_id, account)

    def closeAccount(self):
        pass

    def loanRequest(self, amount, account_id, customer_id, Type=None):
        loan = Loan(account_id, customer_id, Type=None)
        self.bank.add_loan_info(customer_id, loan)

    def provideInfo(self):
        pass

    def issueCard(self):
        pass

class Account:
    def __init__(self, customer_id, account_no):
        self.cust_id = customer_id
        self.account_no = account_no
        self.balance = 0

    def add_balance(self, amount):
        self.balance += amount
        print ("%s deposited into %s account" % (amount, self.cust_id))

    def subtract_balance(self, amount):
        if self.balance >= amount:
            self.balance -= amount

        else:
            print ('insufficient balance')

    def check_balance(self):
        return  self.balance


class Checking(Account):
    def accountInfo(self):
        print ("Account-number: %s ,Account-type: %s, Account_balance: %s" \
        %(self.account_no, 'Checking', self.balance))

class Savings(Account):
    def accountInfo(self):
        print ("Account-number: %s ,Account-type: %s, Account_balance: %s" \
        %(self.account_no, 'Savings', self.balance))

class Loan:
    def __init__(self, id, account_id, customer_id, Type=None):
        self.loan_id = id
        self.loan_type = Type
        self.account_id = account_id
        self.customer_id = customer_id

    def amount(self, amount):
        self.amount = amount

    def payment(self, amount):
        if amount <= self.amount:
            self.amount -= amount
        else:
            print ('The amount exceeds the loan')
            
stanbic = Bank(1, 'Stanbic Bank', 'Kampala')

teller1 = Teller(1, 'teller1', stanbic)
teller2 = Teller(2, 'teller2', stanbic)
teller3 = Teller(3, 'teller3', stanbic)
teller1.add_teller(teller1)
teller2.add_teller(teller2)
teller3.add_teller(teller3)
print (stanbic.tellers)


customer1 = Customer(1, 'cust1','kampala', '43526', '85874', stanbic)
customer1.add_customer(customer1)
customer1.OpenAccount(savings)
customer1.depositMoney(50000)





