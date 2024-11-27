class Account():
    bank_name = ""

    def __init__(self, transaction:list[dict], balance:int) -> None:
        self.transaction = transaction
        self.__balance = balance

    @classmethod
    def get_bank_name(cls) -> str:
        return cls.bank_name
    @classmethod
    def set_bank_name(cls, name:str)->None:
        cls.bank_name = name

    def deposit(self, amount: int) -> None:
        if amount >0:
            self.__balance += amount
            self.transaction.append({"입금":amount})
            return self.__balance
        else:
            print("양수만 입력해 주세요")
            
    def withdraw(self, amount: int) -> None:
        if amount <0 :
            print("양수만 입력해 주세요")
        elif amount > self.__balance:
            print("잔고가 부족합니다.")
        else:
            self.__balance -= amount
            self.transaction.append({"출금": amount}) 
            return self.__balance
    
    def get_balance(self) -> int:
        return self.__balance
    
    def get_transaction(self) -> list:
        return self.transaction
    
