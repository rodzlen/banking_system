from models.user import User
from models.account import Account
class BankingService:
    def __init__(self) -> None:
        self.users = []
        self.account = Account()

    def add_user(self, username: str) -> None:
        self.users.append(User(username))

    def find_user(self, username:str) -> User:
        try:
            for i in self.users:
                if i == username:
                    return username
        except Exception:
            print("없는 사용자입니다.")
            
    def user_menu(self, username:str) -> None:
        while True:
            if username in self.users:
                print(f"환영합니다 {username}님 \n 메뉴를 선택해 주세요")
                menu = input("1. 입금 2. 출금 3. 잔액확인 4. 거래내역".split(' '))
                if menu == "1" or menu == "입금":
                    amount = int(input("입금할 금액을 입력하세요: "))
                    self.account.deposit(amount)
                if menu == "2" or menu == "출금":
                    amount = int(input("출금할 금액을 입력하세요: "))
                    self.account.withdraw(amount)
                if menu == "3" or menu == "잔액확인":
                    self.account.get_balance()
                if menu == "4" or menu == "거래내역":
                    self.account.get_transaction()

    