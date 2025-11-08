# 자판기 클래스 정의
class VendingMachine:
    def __init__(self):
        self.items = {
            "콜라": 1200,
            "사이다": 1100,
            "커피": 900,
            "물": 700
        }
        self.balance = 0

    def insert_money(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount}원이 투입되었습니다. 현재 잔액: {self.balance}원")
            if self.balance < 600:
                print("현재 금액이 600원 미만입니다. 음료를 구매하려면 돈을 더 넣어주세요.")
        else:
            print("올바른 금액을 넣어주세요.")

    def show_menu(self):
        print("\n===== 음료 목록 =====")
        for name, price in self.items.items():
            print(f"{name}: {price}원")
        print("=====================")
        print(f"현재 잔액: {self.balance}원")

    def select_item(self, name):
        if name not in self.items:
            print("해당 음료는 없습니다.")
            return
        price = self.items[name]
        if self.balance < price:
            print(f"잔액이 부족합니다. {price - self.balance}원이 더 필요합니다.")
            return
        self.balance -= price
        print(f"{name}이(가) 나왔습니다! 잔액: {self.balance}원")

    def return_change(self):
        if self.balance <= 0:
            print("반환할 거스름돈이 없습니다.")
            return
        print("\n=== 거스름돈 반환 ===")
        change = self.balance
        for unit in [1000, 500, 100]:
            count = change // unit
            change %= unit
            if count > 0:
                print(f"{unit}원: {count}개")
        if change > 0:
            print(f"잔돈 중 {change}원은 반환되지 않았습니다. (100원 단위 미만)")
        print("=====================")
        self.balance = 0


# ✅ 프로그램 바로 실행
machine = VendingMachine()

while True:
    print("\n===== 자판기 메뉴 =====")
    print("1. 돈 넣기")
    print("2. 음료 보기")
    print("3. 음료 선택")
    print("4. 거스름돈 반환")
    print("5. 종료")
    print("=======================")

    choice = input("선택: ")

    if choice == "1":
        try:
            amount = int(input("투입할 금액: "))
            machine.insert_money(amount)
        except ValueError:
            print("숫자를 입력해주세요.")

    elif choice == "2":
        machine.show_menu()

    elif choice == "3":
        name = input("구매할 음료 이름: ")
        machine.select_item(name)

    elif choice == "4":
        machine.return_change()

    elif choice == "5":
        print("자판기를 종료합니다.")
        machine.return_change()
        break

    else:
        print("올바른 메뉴를 선택해주세요.")
