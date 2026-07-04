import datetime
import random
import re
import sys

def get_current_time():
    """Returns the current time in HH:MM AM/PM format."""
    now = datetime.datetime.now()
    return now.strftime("%I:%M %p")

def get_current_date():
    """Returns the current date in YYYY-MM-DD format."""
    today = datetime.date.today()
    return today.strftime("%B %d, %Y")

def get_joke():
    """Returns a random programming joke."""
    jokes = [
        "Why do programmers prefer dark mode? Because light attracts bugs!",
        "There are 10 types of people in the world: those who understand binary, and those who don't.",
        "Why did the programmer quit his job? Because he didn't get arrays.",
        "I would tell you a joke about UDP, but you might not get it.",
        "A SQL query goes into a bar, walks up to two tables and asks... 'Can I join you?'"
    ]
    return random.choice(jokes)

def get_weather():
    """Returns a placeholder weather response."""
    # In a real application, this would call an external API (e.g., OpenWeatherMap).
    return "The weather currently is sunny and 25°C (Placeholder)."

def calculate(expression):
    """Evaluates a simple mathematical expression."""
    try:
        # Using a regular expression to ensure only basic math characters are evaluated
        # to avoid security risks with eval().
        allowed_chars = re.compile(r'^[0-9+\-*/().\s]+$')
        if allowed_chars.match(expression):
            # Using eval is generally dangerous, but we've restricted the input.
            result = eval(expression)
            return f"The result is {result}"
        else:
            return "Invalid expression. Please use numbers and +, -, *, / only."
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except Exception:
        return "I couldn't calculate that. Please try a simple expression like '5 + 3'."

def show_menu():
    """Displays the available commands for the user."""
    menu = """
    Here is what I can do:
    1. Answer basic questions (e.g., 'What is your name?', 'How are you?')
    2. Tell a joke (say 'tell me a joke')
    3. Show time and date (say 'time' or 'date')
    4. Calculate simple math (say 'calculate 5+5')
    5. Check weather (say 'weather')
    6. Exit (say 'exit', 'quit', 'bye')
    """
    return menu

def get_response(user_input):
    """
    Processes the user input and returns an appropriate response using rule-based logic.
    """
    # Convert input to lowercase and remove leading/trailing whitespace
    # to make the matching case-insensitive and robust.
    text = user_input.lower().strip()

    # 1. Greeting Detection
    greetings = ['hi', 'hello', 'hey', 'good morning', 'good evening']
    if text in greetings:
        return "Hello there! How can I help you today?"

    # 2. Basic Questions
    elif "your name" in text:
        return "I am RuleBot, your friendly assistant."
    elif "who created you" in text:
        return "I was created by a Senior Python Developer."
    elif "how are you" in text:
        return "I am just a computer program, but I'm doing perfectly fine! Thank you for asking."
    elif "what can you do" in text or "help" in text or "menu" in text:
        return show_menu()

    # 3. Optional Features Handling
    elif "joke" in text:
        return get_joke()
    elif "time" in text:
        return f"The current time is {get_current_time()}."
    elif "date" in text:
        return f"Today's date is {get_current_date()}."
    elif "weather" in text:
        return get_weather()
    elif text.startswith("calculate "):
        # Extract the expression part after the word 'calculate '
        expression = text.replace("calculate ", "")
        return calculate(expression)

    # 4. Unknown Input Handling
    else:
        return "I'm sorry, I don't understand that. Type 'help' to see what I can do."

def main():
    """
    The main function that runs the continuous conversation loop.
    """
    print("========================================")
    print("Welcome to RuleBot! (Type 'help' for options)")
    print("========================================")

    # Continuous Conversation using while True
    while True:
        try:
            # Get user input
            user_input = input("\nYou: ")

            # Handle empty input
            if not user_input.strip():
                print("RuleBot: Please say something!")
                continue

            # Exit Commands
            exit_commands = ['exit', 'quit', 'bye', 'goodbye']
            if user_input.lower().strip() in exit_commands:
                print("RuleBot: Goodbye! Have a great day!")
                break

            # Generate and print response
            response = get_response(user_input)
            print(f"RuleBot: {response}")

        # Handle KeyboardInterrupt (Ctrl+C) gracefully
        except KeyboardInterrupt:
            print("\nRuleBot: Goodbye! Have a great day!")
            sys.exit()

if __name__ == "__main__":
    # Start the chatbot when the script is run
    main()
