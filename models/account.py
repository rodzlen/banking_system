from models.transaction import Transaction
from utils.decorators import validate_transaction
from utils.exceptions import  InsufficientFundsError, NegativeAmountError



class Account():
    bank_name = "khs은행"

    def __init__(self,  balance:int) -> None:
        self.transactions = []
        self.__balance = balance

    @classmethod
    def get_bank_name(cls) -> str:
        return cls.bank_name
    @classmethod
    def set_bank_name(cls, name:str)->None:
        cls.bank_name = name
    @validate_transaction
    def deposit(self, amount: int) -> None:
        if amount > 0:
            self.__balance += amount
            self.transactions.append(Transaction("입금",amount,self.__balance))
            return self.__balance
        else:
            raise NegativeAmountError()
        
    @validate_transaction       
    def withdraw(self, amount: int) -> None:
        if amount <0 :
            raise NegativeAmountError()
        elif amount > self.__balance:
            raise InsufficientFundsError(self.__balance)
        else:
            self.__balance -= amount
            self.transactions.append(Transaction("출금",amount,self.__balance)) 
            return self.__balance
    

    def get_balance(self) -> int:
        return self.__balance
    
    def get_transaction(self) -> list:
        return self.transaction
    
