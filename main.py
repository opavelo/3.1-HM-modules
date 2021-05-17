from application.Salary import calculate_salary
from application.db.people import get_employees
from datetime import datetime, date, time

if __name__ == '__main__':
    print('main.py')
    print(f'Текущее время: {datetime.now()}' )
    calculate_salary()
    get_employees()


