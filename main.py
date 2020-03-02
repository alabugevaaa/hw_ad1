# -*- coding: utf-8 -*-
from application.salary import calculate_salary
from application.people import get_employees
from datetime import datetime

if __name__ == '__main__':
    print(datetime.now())
    get_employees()
    calculate_salary()