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

print("num_within:")

print("pascal:")