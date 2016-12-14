import sys
from hello import say_hello
from hello import say_something

if __name__ == "__main__":
    say_something(sys.argv[1:])


