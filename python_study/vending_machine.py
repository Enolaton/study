"""
Made By ChatGPT
"""
class VendingMachine:
    def __init__(self):
        self.items = {
            "콜라": 1200,
            "사이다": 1100,
            "커피": 900,
            "물": 700,
            "q": 0  # 종료 옵션
        }
        self.money = 0
        self.first_insert = True  # 첫 투입 상태 기록

    def show_menu(self):
        print("\n===== 음료 목록 =====")
        for name, price in self.items.items():
            if name == "q":
                print(f"{name}: 종료")
            else:
                print(f"{name}: {price}원")
        print("=====================")
        print(f"현재 잔액: {self.money}원")

    def insert_money(self, price):
        """금액 투입 단계"""
        while self.money < price:
            user_input = input(
                "금액을 투입하세요: " if self.first_insert else f"{price - self.money}원이 필요합니다. 금액을 투입하세요: "
            )
            self.first_insert = False  # 첫 투입 후 False로 변경

            if not user_input.isdigit():  # 숫자가 아니면 안내
                print("잘못 입력하셨습니다. 숫자만 입력해주세요.")
                continue

            amount = int(user_input)
            if amount <= 0:
                print("올바른 금액을 넣어주세요.")
                continue

            self.money += amount
            print(f"{amount}원이 투입되었습니다. 현재 잔액: {self.money}원")
            if self.money < 600:
                print("현재 금액이 600원 미만입니다. 음료를 구매하려면 돈을 더 넣어주세요.")

    def buy_item(self, name):
        if name not in self.items:
            print("해당 음료는 없습니다.")
            return

        if name == "q":
            print("\n프로그램을 종료합니다.")
            self.return_change()
            exit()

        price = self.items[name]

        # 금액 투입 단계
        self.insert_money(price)

        # 구매 완료
        self.money -= price
        print(f"{name}이(가) 나왔습니다! 잔액: {self.money}원")

        # 구매 후 메뉴 재출력
        self.show_menu()

    def return_change(self):
        """잔돈 반환"""
        if self.money <= 0:
            print("반환할 거스름돈이 없습니다.")
            return
        print("\n=== 거스름돈 반환 ===")
        change = self.money
        for unit in [1000, 500, 100]:
            count = change // unit
            change %= unit
            if count > 0:
                print(f"{unit}원: {count}개")
        if change > 0:
            print(f"잔돈 중 {change}원은 반환되지 않았습니다. (100원 단위 미만)")
        print("=====================")
        self.money = 0


# 프로그램 실행
machine = VendingMachine()
machine.show_menu()

while True:
    user_input = input("\n음료 이름을 입력하거나 'q'로 종료: ").strip().lower()
    machine.buy_item(user_input)
