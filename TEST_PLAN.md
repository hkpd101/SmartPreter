"""
Simple test cases for SmartPreter - Example code snippets to test each review type
"""

# Test Case 1: Basic Function (Good for "Explain Code")
def fibonacci(n):
    """Calculate fibonacci number recursively"""
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Test Case 2: Code with Bugs (Good for "Find Bugs")
def divide_numbers(a, b):
    result = a / b  # Bug: No zero division check
    return result

def process_list(items):
    for i in range(len(items) + 1):  # Bug: Index out of range
        print(items[i])

# Test Case 3: Inefficient Code (Good for "Optimize")
def find_duplicates(numbers):
    duplicates = []
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i != j and numbers[i] == numbers[j]:
                if numbers[i] not in duplicates:
                    duplicates.append(numbers[i])
    return duplicates

# Test Case 4: Security Issues (Good for "Security Check")
import subprocess
import os

def run_command(user_input):
    # Security issue: Command injection vulnerability
    os.system(user_input)
    
def sql_query(username):
    # Security issue: SQL injection vulnerability
    query = f"SELECT * FROM users WHERE username = '{username}'"
    return query

# Test Case 5: Style Issues (Good for "Style Review")
def badFunction(x,y):
    if x>y:
        return x
    else:
        return y

class myClass:
    def __init__(self,name):
        self.name=name
        
    def getName(self):
        return self.name

# Test Case 6: Complex Algorithm (Good for "Explain Code")
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

# Test Case 7: Error-Prone Code (Good for "Find Bugs")
def process_data(data):
    result = []
    for item in data:
        processed = item.upper().strip()  # Error if item is not string
        result.append(processed)
    return result

# Test Case 8: Resource Management (Good for "Security Check")
def read_file(filename):
    file = open(filename, 'r')  # Security issue: File not closed
    content = file.read()
    return content

print("📝 Test code snippets ready!")
print("Copy any of these functions into SmartPreter to test different review types:")
print("1. fibonacci() - Test 'Explain Code'")
print("2. divide_numbers() - Test 'Find Bugs'") 
print("3. find_duplicates() - Test 'Optimize'")
print("4. run_command() - Test 'Security Check'")
print("5. badFunction() - Test 'Style Review'")