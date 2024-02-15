import sys

def check_odd_even(number):
    assert len(sys.argv) == 2, "more than one argument is provided"
    assert isinstance(number, int), "Argument must be an integer"
    if number % 2 == 0:
        print("I am Even")
    else:
        print("I am Odd")

if __name__ == "__main__":
    try:
        assert len(sys.argv) == 2, "more than one argument is provided"
        number = int(sys.argv[1]) 
        check_odd_even(number)
    except AssertionError as e:
        print("AssertionError:", e)
    except ValueError:
        print("AssertionError:", "Argument must be an integer")
