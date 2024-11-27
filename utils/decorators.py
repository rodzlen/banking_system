def validate_transaction(func:callable)->callable:
        return True if amount > 0 else False