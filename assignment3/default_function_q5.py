
def student_info(name, age, course):
    print("Name:", name)
    print("Age:", age)
    print("Course:", course)

# Keyword arguments
student_info(age=20, course="Python", name="vivek")

 # Passing Function as an Argument

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def calculate(operation, x, y):
    result = operation(x, y)
    print("Result:", result)

# Passing function as argument
calculate(add, 10, 5)
calculate(subtract, 10, 5)