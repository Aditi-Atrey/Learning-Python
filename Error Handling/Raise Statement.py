#Example 1
def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age
try:
    check_age(-5)
except ValueError as e:
    print(f"Error: {e}")

#Example 2
def process_data(data):
    try:
        result = int(data)
        return result * 2
    except ValueError:
        print("Logging: Invalid data received")
        raise
try:
    process_data("abc")
except ValueError:
    print("Handled at higher level")
