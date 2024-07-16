import common

def add(a:int, b:int) -> int:
    return a + b

def sub(a: int, b: int) -> int:
    return a - b

print(common.__name__)

if __name__ == "__main__":
    print(add(2,3))
    print(sub(5,2))

    