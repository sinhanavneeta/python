# I REQ. Gathering : Print numbers from 1 to 10
i = 1
while i <= 10:
    print(i)
    i += 1
print("End of while loop")


# Print numbers between 1 to 10 except 5.
print("========================================")
i = 0
while(i < 10):
    i += 1

    if i == 5:
        print("Number is 5, don't print this")
        continue
    print(i)


# II REQ. Gathering : Print numbers from 10 to 1
# 10 9 8 7 6 5 4 3 2 1
# STATE
print("======================================")
i = 10
while i > 0:
    print(i)
    i -= 1

 # Print even numbers between 1 to 100
print("======================================")
print("Print numbers from 1 to 100")
i = 1
# validation logic
while i <= 100:
    print(i)
    i += 1      # business logic


# Print numbers between 1 to 100 which are divisible by 5 and 3
'''
1 2 3 4 5 6 7 8 9 10 .15.. 100
'''
'''
validation logic  : if else
business logic    : while
'''
print("=============================================================")
print("Print numbers between 1 to 100 which are divisible by 5 and 3")
i = 1
while i <= 100:     #business logic
    #validation logic
    if i % 3 == 0 and (i % 5 == 0):
        print(i)
    i += 1

# REQ: Print odd numbers(exclude divisible by 5) from 1 to 100
# 1 3 5 7 9 11 13 ...
print("==============================================================")
print("Print odd numbers(exclude divisible by 5) from 1 to 100")
i = 1
while i <= 100:
    if i % 2 == 1:
        print(i)
    i += 1

# REQ: Print even numbers between 1 to 20
# 2 4 6 8 10 12 .....
# 1 2 3 4 5 6 7 8 9 10 ....20
print("====================================")
print("----even numbers between 1 to 20----")
i = 2
list = []
while i <= 20:
    list.append(i)
    i += 2
print(list)

# REQ: Print numbers divisible  by 5 between 1 to 100
# 0 5 10 15 20 25 .....
print("------Divisible by 5------")
i = 0
while i <= 100:
    print(i)
    i += 5


# REQ: Print numbers divisible  by 3
# 3 6 9 12 .....

print("------Divisible by 3------")
i = 3
while i <= 100:
    print(i)
    i += 3

# REQ: Print numbers divisible  by 7
# 7 14 21 28 35 42 .......

print("------Divisible by 7------")
i = 7
while i <= 100:
    print(i)
    i += 7


# Print numbers divisible by 3 and 7
print("------Divisible by 3 and 7----------")
i = 1
while i <= 100:
    if (i % 3 == 0) and (i % 7 == 0):
        print(i)
    i += 1


# Print numbers divisible by 5 or 6
print("------Divisible by 5 or 6----------")
i = 1
while i <= 100:
    if (i % 5 == 0) or (i % 6 == 0):
        print(i)
    i += 1

# print the numbers which ends with 0 between 100 and 500
print("----------------------------------")


print("------Numbers which ends with 0----------")
list = []
i = 100
while i <= 500:
   list.append(i)
   i += 10
print(list)
