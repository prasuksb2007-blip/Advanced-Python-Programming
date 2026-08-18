def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before the function call")
        result = func(*args, **kwargs)
        print("After the function call")
        return result
    return wrapper
@my_decorator
def addition(a, b):
    print("Hello from addition function!")
    print(f"The sum of {a} and {b} is: {a + b}")
addition(5, 3)
'''
--> Output:
Before the function call
Hello from addition function!
The sum of 5 and 3 is: 8
After the function call
'''

#iteration
class EvenNumbers:
    def __init__(self, limit):
        self.limit = limit
        self.current = 2

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.limit:
            num = self.current
            self.current += 2
            return num
        else:
            raise StopIteration
'''
--> Output:
2
4
6
8
10
'''

# Driver Code
obj = EvenNumbers(10)

#closure

for i in obj:
    print(i)

def multiplier(x):
    def multiply(y):
        return x * y
    return multiply

# Driver Code
double = multiplier(2)
triple = multiplier(3)

print(double(5))
print(triple(5))
'''
--> Output:
10
15
'''