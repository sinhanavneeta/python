"""
Give examples for below conditions
	1. single if :
	2. if else:
	3. if elif else:
	4. if elif elif else:
	5. Nested if:
"""

# 1. single if :
n = int(input("Please enter a number: "))
if n % 2 == 0:
    print("Given number is an even number")

# 2. if else:
n1 = int(input("Please enter a number: "))
if n1 % 2 == 0:
    print("Given number is an even number")
else:
    print("Given number is an odd number")

# 3. if elif else:
marks = int(input("Enter the marks: "))
# if marks >= 0 and marks <= 100:
if marks >= 35:
    print("pass")
elif marks >= 0 and marks <35:
    print("fail")
else:
    print("invalid input")


# 4. if elif elif else:
marks1 = int(input("Enter your marks: "))
if marks1 >= 90 and marks1 <= 100 :
    print("Grade A")
elif marks1 < 90 and marks1 >= 80:
    print("Grade B")
elif marks1 < 80 and marks1 >= 70:
    print("Grade C")
else:
    print("Grade D")


# 5. Nested if:
marks2 = int(input("Enter your marks: "))
if marks2 >= 60:
    print("You passed the examination")
    if marks2 >= 75:
        print("You got the distinction")
else:
    print("Sorry.... You are fail")


"""
1. Prepare state and assign North South West East 
	    north = []
		south = ['Andhra Prades', 'Telangana', 'Karnataka','Tamil Nadu', 'Kerala']
		west = []
		east = []
"""
north = ["Jammu & Kashmir", "Punjab", "Himachal Pradesh", "Delhi", "Bihar" ]
south = ['Andhra Prades', 'Telangana', 'Karnataka','Tamil Nadu', 'Kerala']
west = ["Gujarat", "Maharashtra", "Rajsthan"]
east = ["Assam", "West Bengal", "Manipur", "Nagaland", "Arunanchal Pradesh"]

# 2. Prepare dictionary with key as state name and value as "list of districts"
state = {
    "Karnataka" : ["Mysore", "Bengaluru", "Ooty", "Udupi", "Chikkamangaluru", "Mangaluru"],
    "Bihar" : ["Nalanda", "Patna", "Nawada", "Arrah"],
    "Uttar Pradesh": ["Varanasi", "Prayagraj", "Noida", "Lucknow"],
    "Delhi" : ["North Delhi", "East Delhi", "South Delhi", "Shahadara"],
    "Andhra Pradesh" : ["Gutoor", "Anantpur", "Chittoor", "East Godavari", "Kadapa", "Nellore" ]
}

print(state.items())

"""
4. Get employee details(in dict format, empid,name,sal, exp) and update hike for employee with below 
		If exp is 0 to 2 years - 10% Hike
				  2 to 5 years - 20% Hike
				  5 to 8 years - 30% Hike
				  8+           - No hike
"""
emp = {
    "emp_id" : 431,
    "name": "Navneeta Sinha",
    "sal" : 45000,
    "exp" : 1
}
if emp["exp"] >= 0 and emp["exp"] <= 2:
    emp["sal"] += emp["sal"] * 0.1
elif emp["exp"] > 2 and emp["exp"] <= 5:
    emp["sal"] += emp["sal"] * 0.2
elif emp["exp"] > 5 and emp["exp"] <= 8:
    emp["sal"] += emp["sal"] * 0.3
else :
    print("No Hike")
print(emp["sal"])
