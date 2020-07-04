def div100(func):
    def wrapper(*args):
      result = func(*args)
      if result == 0 :
          print(f"We are Ok!")
      else :
          print(f"Bad news guys, we got {result}")
    return wrapper


@div100
def test2(a):
    v = a % 100
    return v
test2(77777735423400)
