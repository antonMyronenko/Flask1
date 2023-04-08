from app import exm
from random import choice
from math import factorial

@exm.route('/')
def index():
    list_ = [randrange(1, 200) for x in range(15)]
    list_.sort()
    return str(list_)

@exm.route('/personal_data')
def personal_data():
    name = "Anton"
    age = "16"
    country = "Ukraine"
    return f"Hello, my name is {name}, im {age} years old, im from {country}"

@exm.route('/random_number')
def random_number():
    number = choice(range(101))
    if number < 50: return number * 1.5
    else: return factorial(number)