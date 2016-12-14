def say_something(something):
    if something:
       print(" ".join(something)[::-1])
    else:
       print("Hello World!")
