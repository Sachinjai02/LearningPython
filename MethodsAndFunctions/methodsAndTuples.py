# return multiple values from a fn

stock_prices = [('APPL', 200), ('GOOG', 500), ('MSFT', 100)]

for ticker, stock_price in stock_prices:
    print('stock price = ' + str(stock_price) + ' for Organization ' + ticker)

work_hours = [('Abby', 100), ('Billy', 500), ('Cassie', 800)]


def employee_check(work_hours):
    max_hours = 0
    employee_name = ''
    for emp_name, hours in work_hours:
        if max_hours < hours:
            max_hours = hours
            employee_name = emp_name
    return (employee_name, max_hours)


print(f'Employee of the month {employee_check(work_hours)}')
