import time
from datetime import date
today = date.today()
def say_something(something):
    if something:
       print(" ".join(something)[::-1]+today)
    else:
       print("Hello World! " +today)
