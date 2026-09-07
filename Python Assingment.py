# Keep asking until the user gives a valid integer
while True:
    try:
        age = int(input("Please enter your age: "))
        print(f"Your age is: {age}")
        break  # Exit the loop once a valid number is entered
    except ValueError:
        print("Invalid input! Please enter numbers only.")
# List of 5 fruits
fruits = ["Apple", "Banana", "Orange", "Mango", "Grapes"]

# 1. Write fruits to the file
with open("fruits.txt", "w") as file:
    for fruit in fruits:
        file.write(fruit + "\n")

# 2. Read fruits from the file and display them
print("Fruits from file:")
with open("fruits.txt", "r") as file:
    for line in file:
        print(line.strip())
        # Dictionary with 5 students and their marks
    students = {
        "Alice": 85,
        "Bob": 92,
        "Charlie": 78,
        "David": 95,
        "Emma": 88
    }

    # Display all students and marks
    print("All Students and Marks:")
    for name, mark in students.items():
        print(f"{name}: {mark}")

    # Find the student with the highest mark
    top_student = max(students, key=students.get)
    print(f"\nStudent with the highest mark: {top_student} ({students[top_student]})")
    # Define Book class


class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display_details(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Price: ${self.price}")
        print("-" * 20)


# Create two book objects
book1 = Book("To Kill a Mockingbird", "Harper Lee", 15.99)
book2 = Book("1984", "George Orwell", 12.50)
# Display their details
book1.display_details()
book2.display_details()


def find_peak_usage(logs: object):
    # Create an hourly counter with 24 hours (0 to 23) initialized to 0
    hour_counts = [0] * 24

    for log in logs:
        # The ISO timestamp format is: "YYYY-MM-DDTHH:MM:SS"
        # The hour is located between index 11 and 13
        hour = int(log[11:13])
        hour_counts[hour] += 1

    # Find the maximum count
    max_logins = max(hour_counts)

    # index() automatically returns the smallest (earliest) index in case of a tie
    return hour_counts.index(max_logins)


# Example usage:
logs = [
    "2026-08-04T13:21:18",
    "2026-08-04T13:45:00",
    "2026-08-04T09:10:05",
    "2026-08-04T09:55:20"
]

print("Peak hour:", find_peak_usage(logs))  # Output: 9 (tie between 9 and 13, returns earliest: 9)
