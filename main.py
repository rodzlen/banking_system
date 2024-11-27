from service import banking_service


bank_service = banking_service.BankingService()
def main()-> None:
    while True:
        username = input("이름을 입력하세요")
        bank_service.user_menu(username)
main()