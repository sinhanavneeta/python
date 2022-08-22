"""
Arithmatic operators
Addition : Calculate sum of two numbers
"""
#Hard coding
# version 1
print(10 + 20)
# version 2
x = 15
y = 41
print(x+y)
print(sum([2, 3]))
# version 4
output = x + y
print("sum of x and y : ", output)
# version 5
x1 = int(input("Enter first number: "))
y1 = int(input("Enter second number: "))
sum = x1 + y1
print("sum of x1 and y1 is: ", sum)

arr = [4, 6, 56, 78, 45]
num = sum([4, 6])

for x in arr:
    num += x

print(num)


tup = (1, 5, 6, 4, 3)
sum1 = 0
for x in tup:
    sum1 += x
print(sum1)


"""
substraction : Calculate substraction of two numbers
#Hard coding
# version 1
"""
print(10 - 20)
# version 2
print(x-y)
# version 3
output = x - y
print("substraction of x and y : ", output)
# version 4
x1 = int(input("Enter first number: "))
y1 = int(input("Enter second number: "))
subs = x1 - y1
print("substraction of x1 and y1 is: ", subs)

"""
multiplication : Calculate multiplication of two numbers
#Hard coding
# version 1
"""
print(10 * 20)
# version 2

print(x1*y1)
# version 4
output = x1 * y1
print("multiplication of x and y : ", output)
# version 5

mul = x1 * y1
print("multiplication of x1 and y1 is: ", mul)

"""
division : Calculate division of two numbers
#Hard coding
# version 1
"""
print(10 / 20)
# version 2

print(x1 / y1)
# version 4
output = x1 / y1
print("division of x and y : ", output)
# version 5

div = x1 / y1
print("division of x1 and y1 is: ", div)

"""
exponential operator : Calculate exponential of two numbers where the first number is co-efficient and the second number is expnential 
#Hard coding
# version 1
"""
print(10 ** 20)
# version 2
print(x ** y)
# version 3
output = x ** y
print("exponential of x and y : ", output)
# version 4
x1 = int(input("Enter first number: "))
y1 = int(input("Enter second number: "))
exponent = x1 ** y1
print("exponential of x1 and y1 is: ", exponent)

"""
# Assignment opeartors
"""
x = 23
# we are assigning value 23 to a variable x
y = 32
output = x + y
print(output)
x = x + y
print(x)

# shorthand operators
# plus opearator
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
x += y
print(x)

y = y + x
print(y)

y += x
print(y)

# shorthand minus operator

x = x - y
print(x)
x -= y
print(x)
y = y - x
print(y)
y -= x
print(y)

# shorthand multiplication operator
x = x * y
print(x)
x *= y
print(x)
y = y * x
print(y)
y *= x
print(y)


# shorthand division operator
x = x / y
print(x)
x /= y
print(x)
y = y / x
print(y)
y /= x
print(y)

# shorthand floor division operator
x = x // y
print(x)
x //= y
print(x)
y = y // x
print(y)
y //= x
print(y)

# shorthand exponential operator
x = x ** y
print(x)
x **= y
print(x)
y = y ** x
print(y)
y **= x
print(y)


# Logical operators
# and, or, not
# and
print(x < 5 and x < 10)
print(x > 10 and x < 5)
print(x > 10 and y < 10)
print(x < 5 and y < 15)
bool1 = x > 10
bool2 = y < 10
print(bool1 and bool2)

# or
print(x < 5 or x < 10)
print(x > 10 or x < 5)
print(bool1 or bool2)

# not
x = 10
print(not (x > 10 and x < 21))
print(not(True))
print(not (False))

"""
comparison operators : used to compare two values
"""
print(x == y)
print(x >= y)
print(x <= y)
print(x > y)
print(x < y)
print(x != y)


"""
identity operators : is, is not 
gives output as True if both the variables have same value as well as same address.
"""

x = 5
y = 5
print(x is y)
print(x is not y)

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
print(x is y)
print(x is not y)


"""
Membership Operators : in, not in
return true if the specific variable or constant is present in the list 
otherwise returns false
"""

x = ["a", "b", "c"]
print("a" in x)
print("b" not in x)

