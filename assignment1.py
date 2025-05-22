# Prime Number Generator
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def generate_primes(start, end):
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes


# Number to Words Converter 
def num_to_words(n):
    if n == 0:
        return "zero"

    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen",
             "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty",
            "fifty", "sixty", "seventy", "eighty", "ninety"]

    def two_digits(num):
        if num < 10:
            return ones[num]
        elif 10 <= num < 20:
            return teens[num - 10]
        else:
            return tens[num // 10] + ("-" + ones[num % 10] if num % 10 != 0 else "")

    def three_digits(num):
        if num < 100:
            return two_digits(num)
        else:
            return ones[num // 100] + " hundred" + (" " + two_digits(num % 100) if num % 100 != 0 else "")

    result = ""
    if n >= 1000:
        result += ones[n // 1000] + " thousand"
        if n % 1000 != 0:
            result += " " + three_digits(n % 1000)
    else:
        result = three_digits(n)

    return result.strip()


# Tic-Tac-Toe Board Printer
def print_tic_tac_toe():
    board = [str(i) for i in range(1, 10)]
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")


# Anagram Checker
def are_anagrams(s1, s2):
    if len(s1) != len(s2):
        return False

    for char in s1:
        if s1.count(char) != s2.count(char):
            return False

    return True

# Password Strength Checker
import string
def check_password_strength(password):
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)
    return has_upper and has_lower and has_digit and has_special

# Longest Word Finder
def find_longest_word(sentence):
    words = sentence.split()
    return max(words, key=len)

# List Flattening
def flatten_list(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            result.append(item)
    return result

# Frequency Counterr
def word_frequency(text):
    words = text.lower().split()
    freq = {}
    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    return freq


# Character Counter
def character_count(text):
    freq = {}
    for char in text:
        if char == ' ':
            continue
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq

# Student Gradebook
def student_gradebook():
    records = {}
    while True:
        name = input("Enter name to add students. Enter 'stop' to terminate: ")
        if name.lower() == 'stop':
            break
        score = int(input(f"Enter grades for {name}: "))
        records[name] = score
    query = input("Query student name: ")
    print(records.get(query, "Not found"))

# Read and Count Words
def read_file_stats(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    words = sum(len(line.split()) for line in lines)
    chars = sum(len(line) for line in lines)
    return {"lines": len(lines), "words": words, "characters": chars}

# Simple Log Writer
from datetime import datetime
def log_run(filename="log.txt"):
    with open(filename, "a") as f:
        f.write(f"Run at {datetime.now()}\n")

# CSV Reader
import csv
def csv_above_75(filename):
    with open(filename, newline='') as f:
        reader = csv.DictReader(f)
        return [row['Name'] for row in reader if float(row['Marks']) > 75]

# Bank Account Simulation
class BankAccount:
    def __init__(self, name):
        self.name = name
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def get_balance(self):
        return self.balance

# Library Management System
class Book:
    def __init__(self, title):
        self.title = title
        self.available = True

class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, title):
        self.books[title] = Book(title)

    def borrow_book(self, title):
        if title in self.books and self.books[title].available:
            self.books[title].available = False
            return f"Borrowed '{title}'"
        return "Not available"

    def return_book(self, title):
        if title in self.books:
            self.books[title].available = True
            return f"Returned '{title}'"

# Employee Management
class Employee:
    def __init__(self, name, department):
        self.name = name
        self.department = department

class EmployeeManager:
    def __init__(self):
        self.employees = []

    def add_employee(self, name, department):
        self.employees.append(Employee(name, department))

    def get_by_department(self, dept):
        return [e.name for e in self.employees if e.department == dept]

# Simple Quiz App
def quiz_app():
    questions = [
        {
            "q": "Which team won the last Super Bowl?",
            "options": ["A. Baltimore Ravens", "B. Kansas City Chiefs", "C. Philadelphia Eagles", "D. San Francisco 49ers"],
            "answer": "C"
        },
        {
            "q": "Which of these players has the most rings?",
            "options": ["A. Peyton Manning", "B. Drew Brees", "C. Aaron Rodgers", "D. Tom Brady"],
            "answer": "D"
        },
        {
            "q": "Who won MVP last season?",
            "options": ["A. Patrick Mahomes", "B. Josh Allen", "C. Jalen Hurts", "D. Lamar Jackson"],
            "answer": "B"
        }
    ]

    score = 0
    for i, q in enumerate(questions, 1):
        print(f"\nQuestion {i}: {q['q']}")
        for opt in q['options']:
            print(opt)
        user_ans = input("Your answer (A/B/C/D): ").strip().upper()
        if user_ans == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect! The correct answer was {q['answer']}.")

    print(f"\nFinal Score: {score}/{len(questions)}")



# Expense Tracker
def expense_tracker():
    week = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    expenses = {}
    for day in week:
        amount = float(input(f"Enter total expense for {day}: "))
        expenses[day] = amount
    total = sum(expenses.values())
    print(f"Total: ${total:.2f}, Avg/day: ${total/7:.2f}")

# To-Do App with File Persistence
def todo_app(filename="todo.txt"):
    try:
        with open(filename, "r") as f:
            tasks = [line.strip() for line in f]
    except FileNotFoundError:
        tasks = []

    while True:
        cmd = input("Command (add/done/remove/show/quit): ").lower()
        if cmd == "add":
            task = input("Task: ")
            tasks.append("[ ] " + task)
        elif cmd == "done":
            idx = int(input("Task number to mark done: ")) - 1
            tasks[idx] = tasks[idx].replace("[ ]", "[X]")
        elif cmd == "remove":
            idx = int(input("Task number to remove: ")) - 1
            tasks.pop(idx)
        elif cmd == "show":
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
        elif cmd == "quit":
            break

    with open(filename, "w") as f:
        for task in tasks:
            f.write(task + "\n")

