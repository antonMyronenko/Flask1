from app import exm
from random import randrange
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
    t = randrange(0, 100)
    if t < 50: 
        return f"{t*1.5}"
    return f"{factorial(t)}"