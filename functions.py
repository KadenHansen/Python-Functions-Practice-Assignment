# max_num function
print("max_num:")
def max_num(num1, num2, num3):
    list = [num1, num2, num3]
    return max(list)
print(max_num(4, 7, 10))

# mult_list function
print("mult_list:")
def mult_list(numbers):
    total = 1
    for num in numbers:
        total *= num
    return total
numbers = [3, 10, 5]
print(mult_list(numbers))

# rev_string function
print("rev_string:")
def rev_string(string):
    return string[::-1]
print(rev_string("some string"))

# num_within function
print("num_within:")
def num_within(num, min, max):
    if num > min and num < max:
        return True
    else:
        return False
print(num_within(4, 1, 5))

# pascal function
# majority of code block courtesy of https://www.tutorialspoint.com/program-to-generate-pascal-s-triangle-in-python
print("pascal:")
def pascal(n):
   for i in range(n+1):
      for x in range(n-i):
         print(' ', end='')

      y = 1
      for x in range(1, i+1):
         print(y, ' ', sep='', end='')
         y = y * (i - x) // x
      print()
pascal(5)