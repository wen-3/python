hourly_salary = int(input("請輸入時薪:"))   # 時薪(125)
annual_salary = hourly_salary * 8 * 300    # 年薪
monthly_salary = int(input("請輸入每個月的花費："))   # 月支出(9000)
annual_free = monthly_salary * 12    # 年支出
annual_savings = annual_salary - annual_free   #年儲存
print(annual_savings)

