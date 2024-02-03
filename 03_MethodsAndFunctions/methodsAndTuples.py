# return multiple values from a fn

stock_prices = [('APPL', 200), ('GOOG', 500), ('MSFT', 100)]

for ticker, stock_price in stock_prices:
    print('stock price = ' + str(stock_price) + ' for Organization ' + ticker)

work_hours = [('Abby', 100), ('Billy', 500), ('Cassie', 800)]


def employee_check(work_hours):
    emp = ('', 0)
    for current_emp in work_hours:
        if emp[1] < current_emp[1]:
            emp = current_emp
    return emp


print(f'Employee of the month {employee_check(work_hours)}')
