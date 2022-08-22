# Problem 1:
# A and B are holding some objects
# inp = [['A', 'Laptop'], ['A', 'Laptop'], ['A', 'Mouse'], ['B', 'Laptop'], ['A','Headset'],
# ['B','Headset'] ]
# Implement a logic which gives the following output
# out1 = [['A',4], ['B',2]]
# out2 = [['A','Laptop',2], ['A', 'Mouse',1], ['A','Headset',1], ['B','Laptop',1],
# ['B','Headset',1]]
# out3 = ['A','B',['Laptop','Headset']]]

# out1 = [['A',4], ['B',2]]
import math

inp = [['A', 'Laptop'], ['A', 'Laptop'], ['A', 'Mouse'], ['B', 'Laptop'], ['A','Headset'],
['B','Headset'] ]
countA = countB = 0
for i in range(len(inp)):
    if inp[i][0] == "A": countA += 1
    else: countB += 1
res = [["A", countA], ["B", countB]]
print(res)

# out2 = [['A','Laptop',2], ['A', 'Mouse',1], ['A','Headset',1], ['B','Laptop',1],
# ['B','Headset',1]]
res1 = [["A", "Laptop"], ["A", "Mouse"], ["A", "Headset"], ["B", "Laptop"], ["B", "Headset"]]
countALaptop = countAMouse = countAHeadset = countBLaptop = countBHeadset = 0
for i in range(len(inp)):
    if (inp[i][0] == "A") and (inp[i][1] == "Laptop"): countALaptop += 1
    elif (inp[i][0] == "A") and (inp[i][1] == "Mouse"): countAMouse += 1
    elif (inp[i][0] == "A") and (inp[i][1] == "Headset"): countAHeadset += 1
    elif (inp[i][0] == "B") and (inp[i][1] == "Laptop"): countBLaptop += 1
    else: countBHeadset += 1

res1 = [["A", "Laptop", countALaptop], ["A", "Mouse", countAMouse], ["A", "Headset", countAMouse], ["B", "Laptop", countBLaptop], ["B", "Headset", countBHeadset]]
print(res1)

# out3 = ['A','B',['Laptop','Headset']]]
# inp = [['A', 'Laptop'], ['A', 'Laptop'], ['A', 'Mouse'], ['B', 'Laptop'], ['A','Headset'],
# ['B','Headset'] ]
temp = []
arrA = []
arrB = []
for i in range(len(inp)):
    if inp[i][0] == "A" and (inp[i][1] not in arrA):   arrA.append(inp[i][1])
    elif inp[i][0] == "B" and (inp[i][1] not in arrB):   arrB.append(inp[i][1])
# print("arrA:\n", arrA)
# print("arrB:\n", arrB)
lengthA = len(arrA)
lengthB = len(arrB)
length = 0
if lengthA >= lengthB:
    length = lengthB
    for i in range(length):
        if (arrB[i] in arrA) and (arrB[i] not in temp):
            temp.append(arrB[i])    #["Laptop", "Headset"]
else:
    length = lengthA
    for i in range(length):
        if (arrA[i] in arrB) and (arrA[i] not in temp):
            temp.append(arrA[i])

res2 = ["A", "B", temp]
print(res2)


# print(type(1))
"""
Problem 2:
A = [1, 2, 3, 'ae']
B = [1, 1, 'b', 6]
if alpha char exists then it should be treated as 0
C = A + B if even otherwise 0
1) Get output C. With above example C = [2, 0, 0, 6]
2) An find out maximum repeated element in C
"""

A = [1, 2, 3, 'ae',7]
B = [1, 1, 'b', 6,'y']
C = []
for i in range(len(A)) :
   if bool(A[i]) and bool(B[i]):
       if type(A[i]) == int and (type(B[i]) == int) :
          if (A[i] + B[i]) % 2 == 0: C.append(A[i] + B[i])
          else : C.append(0)
       elif type(A[i]) != int:
           if B[i] % 2 == 0:
               C.append(B[i])
           else:
               C.append(0)
       elif type(B[i]) != int:
               if A[i] % 2 == 0:
                C.append(A[i])
               else:
                C.append(0)

   else:
       C.append(None)
print(C)

dict = {}
for i in range(len(C)):
    if C[i] in dict.keys():
        dict[C[i]] += 1
    else:
        dict[C[i]] = 1
print(dict)

maxVal = -math.inf
elem = 0
for key in dict:
    if maxVal <= dict[key]:
        maxVal = dict[key]
        elem = key
print(maxVal)
print(elem)

"""
Problem 3:
Program to find the largest sum of contiguous integers in the array. Example: if 
the input is (-10, 2, 3, -2, 0, 5, -15), the largest sum is 
"""
def calMaxSum(arr) :
    currSum = 0
    maxSum = 0
    for i in range(len(arr)):
        currSum = arr[i]

        for j in range(i + 1, len(arr)):
            if currSum < 0:
                currSum = 0
            currSum += arr[j]

            if currSum > maxSum:
                maxSum = currSum

    return maxSum
print(calMaxSum([-10, 2, 3, -2, 0, 5, -15]))    #  => 8
print(calMaxSum([-10, 2, 3, -2, 0, 5, 15]))     #  => 23






