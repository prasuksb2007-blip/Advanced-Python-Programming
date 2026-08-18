"""
The aim of this program is to efficiently compute the nth Fibonacci number using techniques that
optimize time complexity, ensuring that the computation is fast and scalable even for large values of n.
"""
def fib_iter(n):
    """
    Computes the nth Fibonacci number efficiently using an iterative approach.
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    if n == 0:
        return 0
    elif n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        c = a + b
        a = b
        b = c
    return b


def main():
    print("=" * 45)
    print("      EFFICIENT FIBONACCI CALCULATOR     ")
    print("=" * 45)
    
    try:
        # Accepting user input as per acceptance criteria
        user_input = input("Enter position (n): ")
        n = int(user_input)
        
        result = fib_iter(n)
        
        print("-" * 45)
        print(f"The {n}th Fibonacci number is: {result}")
        print("-" * 45)
        
    except ValueError as e:
        print(f"\nError: Please enter a valid non-negative integer. ({e})")


if __name__ == "__main__":
    main()

"""
--> Output
=============================================
      EFFICIENT FIBONACCI CALCULATOR     
=============================================
Enter position (n): 10
---------------------------------------------
The 10th Fibonacci number is: 55
---------------------------------------------
"""