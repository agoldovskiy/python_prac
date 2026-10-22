"""
задачи на выбрасывание исключений
                                """
def parse_number(value):
    for i in range(len(value)):
        if i == 0:
            if value[i] not in "+-0123456789":
                raise ValueError
        else:
            if value[i] not in "0123456789":
                raise ValueError
    return int(value)

try:
    print(parse_number("+1982"))
    print(parse_number("728"))
    print(parse_number("-2198"))
    print(parse_number("892nb"))
except ValueError:
    print("not a number")

class BankError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class InvalidAmountError(BankError):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class InsufficientFundsError(BankError):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class AccountBlockedError(BankError):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

def withdraw(balance, amount):
    if amount <= 0:
        raise InvalidAmountError
    if balance - amount < 0:
        raise InsufficientFundsError
    return balance - amount