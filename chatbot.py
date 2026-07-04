import os
import sys
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables from a .env file (if it exists)
load_dotenv()

def setup_gemini():
    """
    Configures the Gemini API using the key from the environment variable.
    """
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("Error: GEMINI_API_KEY environment variable not found.")
        print("Please create a .env file in this directory and add:")
        print("GEMINI_API_KEY=your_actual_api_key_here")
        print("You can get a free key from: https://aistudio.google.com/app/apikey")
        sys.exit(1)
    
    genai.configure(api_key=api_key)
    # Using the recommended standard model for general text tasks
    model = genai.GenerativeModel('gemini-1.5-flash')
    # Start a chat session to maintain conversation history (smart conversational AI)
    chat = model.start_chat(history=[])
    return chat

def show_menu():
    """Displays instructions for the user."""
    menu = """
    ========================================
    Welcome to the Smart AI Chatbot! 
    Powered by Google Gemini
    ========================================
    - Ask me anything! (e.g., "Explain quantum physics", "Write a python script")
    - Type 'exit', 'quit', or 'bye' to end the chat.
    ========================================
    """
    return menu

def main():
    """
    The main function that runs the dynamic conversation loop.
    """
    print(show_menu())
    
    # Setup the conversational AI
    chat = setup_gemini()

    while True:
        try:
            # Get user input
            user_input = input("\nYou: ")

            # Handle empty input
            if not user_input.strip():
                print("AI: Please say something!")
                continue

            # Check for exit commands
            exit_commands = ['exit', 'quit', 'bye', 'goodbye']
            if user_input.lower().strip() in exit_commands:
                print("AI: Goodbye! Have a great day!")
                break

            # Send the message to Gemini and get the response
            # We use try/except to handle potential network or API errors
            try:
                response = chat.send_message(user_input)
                print(f"AI: {response.text}")
            except Exception as e:
                print(f"AI: Oops! Something went wrong while connecting to the AI. Error: {e}")

        # Handle KeyboardInterrupt (Ctrl+C) gracefully
        except KeyboardInterrupt:
            print("\nAI: Goodbye! Have a great day!")
            sys.exit()

if __name__ == "__main__":
    main()
