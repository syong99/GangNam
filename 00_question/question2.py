
class Account:
    def __init__(self,account_name,balance = 0):
        self.account_name = account_name
        self.balance = balance

    def deposit(self,amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount}원이 입금되었습니다.")
        else:
            raise ValueError("error")
            
    def withdraw(self,amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"{amount}원이 출금되었습니다.")
        else:
            raise ValueError('error')
    
    def disply_balance(self):
        print(f"{self.account_name}님의 현재 잔액은 {self.balance}원 입니다.")
    
class Bank:
        def __init__(self,name):
            self.name = name
            self.accounts = []
        
        def crate_account(self,account_name,balance = 0):
            account = Account(account_name,balance)
            self.accounts.append(account)
            print(f"{account_name}님의 계좌가 생성되었습니다.")
        
        def get_account(self, account_name):
            for account in self.accounts:
                if account.account_name == account_name:
                    return account
                print(f"{account_name}님의 확인된 계좌가 없습니다.")
        
        def display_accounts(self):
            print(f"{self.name}의 모든 계좌 정보:")
            for account in self.accounts:
                print(f"소유주:{account.account_name}, 잔액:{account.balance}원")

bank = Bank("Bank")

while True:
    print("1. 계좌 생성")
    print("2. 입금")
    print("3. 출금")
    print("4. 조회")
    print("5. 계좌 목록")
    print("종료")

    choice = input("원하시는 작업을 선택해주세요 : ")
    
    if choice == '종료':
        print("프로그램을 종료합니다")
        break
    elif choice == "1":
        account_name = input("이름을 입력해주세요 :")
        bank.crate_account(account_name)
    elif choice == "2":
        account_name = input("이름을 입력해주세요 : ")
        account = bank.get_account(account_name)
        if account:
            amount = int(input("입금할 금액을 입력하세요 : "))
            account.deposit(amount)
    elif choice == "3":
        account_name = input("이름을 입력해주세요 : ")
        bank.get_account(account_name)
        if account:
            amount = int(input("출금할 금액을 선택해주세요."))
            account.withdraw(amount)
    elif choice == "4":
        account_name = input("이름을 입력해주세요 : ")
        account = bank.get_account(account_name)
        if account:
            account.disply_balance()
    elif choice == "5":
        bank.display_accounts()
