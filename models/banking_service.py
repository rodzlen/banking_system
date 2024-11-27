from user import User
from account import Account
class BankingService:
    users = []
    def __init__(self) -> None:
        self.user = User()
        self.account = Account()

    def add_user(self, username: str) -> None:
        self.users.append(username)

    def find_user(self, username:str) -> User:
        try:
           return self.user(username)
        except Exception:
            print("없는 사용자입니다.")
            
    def user_menu(self, username:str) -> None:
        while True:
            input_user = input("이름을 입력해 주세요")
            if username == input_user:
                print(f"환영합니다 {username}님 \n 메뉴를 선택해 주세요")
                menu = input("1. 입금 2. 출금 3. 잔액확인 4. 거래내역".split(' '))
                if menu == "1" or menu == "입금":
                    self.account.deposit()
                if menu == "2" or menu == "출금":
                   self.account.withdraw()
                if menu == "3" or menu == "잔액확인":
                    self.account.get_balance()
                if menu == "4" or menu == "거래내역":
                    self.account.get_transaction()
                