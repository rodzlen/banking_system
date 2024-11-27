from models.account import Account
class User():
    def __init__(self, username:str) -> None:
        self.users =[] # 유저 목록 저장
        self.username= username
        self.account = Account()
