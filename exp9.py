1  def factorial(n):
2      if n < 0:
3          return "Factorial does not exist for negative numbers"
4      elif n == 0:
5          return 1
6      else:
7          result = 1
8          for i in range(1, n + 1):
9              result *= i
10         return result
11
12 num = int(input("Enter a non-negative integer N: "))
13 print(f"The factorial of {num} is {factorial(num)}")
