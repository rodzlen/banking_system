from typing import Callable # Callable은 임포트 해줘야함 

def validate_transaction(func:Callable)->Callable:
        def wrapper(self, amount:int)-> None:
                if amount <= 0:
                        raise ValueError("금액은 0보다 커야 합니다.")
                return func(self, amount)
        return wrapper