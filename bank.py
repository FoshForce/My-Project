class Bank :
    def __init__(self, name) :
        self.__name = name
        self.__account = []
        
    def get_name(self) :
        return self.__name
    
    def add_account(self, account) :
        self.__account.append(account)
        
    def get_account_by_card_id(self, card_id) :
        for account in self.__account :
            if account == account_id :
                return account
        return None

class Customer : 
    def __init__(self, name, id) :
        self.__name = name
        self.__id = id
        
    def get_name(self) :
        return self.__name
    
    def get_id(self) :
        return self.__id
        
class Account :
    def __init__(self,card ,account_id, customer, balance = 0 ) :
        self.__card = card
        self.__account_id = account_id
        self.__customer = customer
        self.__balance = balance
        
    def deposit(self, amount) :
        if amount > 0 :
            self.__balance += amount
            return "Deposit successful"
        else :
            return "Invalid deposit amount"
        
    def withdraw(self, amount) :
        if amount > 0 and amount <= self.__balance :
            self.__balance -= amount
            return "Withdraw successful" 
        else : 
            return "Invalid withdraw amount"
        
    def get_balance(self) :
        return self.__balance
    
    def get_account_id(self) :
        return self.__account_id
    
    def get_customer(self) :
        return self.__customer
    
class Card :
    def __init__(self, card_id, pin) :
        self.__card_id = card_id
        self.__pin = pin
    
    def validate_pin(self, pin) :
        if pin == self.__pin :
            return self.__card_id
        else : 
            return "Invalid PIN"
        
class transaction :
    def __init__(self, account, amount, transaction_type) :
        self.__account = account
        self.__amount = amount
        self.__transaction_type = transaction_type
        
    def get_account(self) :
        return self.__account
    
    def get_amount(self) :
        return self.__amount
    
    def get_transaction_type(self) :
        return self.__transaction_type
 
card1 = Card(67010751, '094615')    
person1 = Customer("Yokphon", 1349901370146)
Account1 = Account(card1, 1946151065, person1, 10000)

Bank1 = Bank("Kasikorn Bank")
Bank1.add_account(Account1)

### Account1 | card_id : 67010751 | card_pin : 094615 | account_id : 1946151065 | account_name : Yokphon | id : 1349901370146 | balance : 10000)

