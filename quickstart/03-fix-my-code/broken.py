# 活動費用計算機
# 這段程式會計算行銷活動的各項費用，並判斷有沒有超過預算

campaign_expenses = [
    {"item": "廣告投放", "unit_cost": 5000, "quantity": 3},
    {"item": "KOL 合作", "unit_cost": 8000, "quantity": 2},
    {"item": "印刷品製作", "unit_cost": 1200, "quantity": 5},
    {"item": "場地租借", "unit_cost": 15000, "quantity": 1},
]

budget = 60000

def calculate_total(expenses):
    total = 0
    for expense in expenses:
        total = total + expense["unit_cost"] * expense["quantty"]  # 錯誤一
    return total

def check_budget(total, budget):
    if total > Budget:  # 錯誤二
        print("超出預算！活動總費用：" + total + " 元")  # 錯誤三
    else:
        print("在預算內，活動總費用：" + str(total) + " 元")

total_cost = calculate_total(campaign_expenses)
check_budget(total_cost, budget)
