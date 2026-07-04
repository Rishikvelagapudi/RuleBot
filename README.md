# Smart AI Chatbot - Powered by Google Gemini

A dynamic, fully conversational AI chatbot built in Python using the Google Gemini API. Unlike traditional rule-based chatbots, this bot can understand natural language, answer complex questions, write code, and chat continuously while remembering context.

## Features
- **Dynamic AI Conversations**: Answers any question just like Google or ChatGPT.
- **Contextual Memory**: Remembers what you said earlier in the conversation.
- **Easy Exit Commands**: Type 'exit', 'quit', or 'bye' to smoothly close the application.
- **Secure Configuration**: Uses `python-dotenv` to safely load API keys without hardcoding them in the script.

## Folder Structure

```
rulebot/
│
├── .env                 # (You create this) Contains your secret GEMINI_API_KEY
├── .env.example         # Example of how to format your .env file
├── .gitignore           # Prevents secrets from being pushed to GitHub
├── chatbot.py           # The main Python script running the AI logic
├── README.md            # Project documentation (this file)
└── requirements.txt     # Python dependencies
```

## Setup Instructions

1. **Install Dependencies**
   Open your terminal in this directory and run:
   ```bash
   pip install -r requirements.txt
   ```

2. **Get a Free Google Gemini API Key**
   - Go to [Google AI Studio](https://aistudio.google.com/app/apikey)
   - Click "Create API Key"

3. **Configure Your Key**
   - Create a new file in this folder named exactly `.env` (don't forget the dot!).
   - Add the following line to the file, replacing the placeholder with your real key:
     ```env
     GEMINI_API_KEY=your_actual_api_key_here
     ```

4. **Run the Chatbot**
   ```bash
   python chatbot.py
   ```

## Sample Output

```
    ========================================
    Welcome to the Smart AI Chatbot!
    Powered by Google Gemini
    ========================================
    - Ask me anything! (e.g., "Explain quantum physics", "Write a python script")
    - Type 'exit', 'quit', or 'bye' to end the chat.
    ========================================

You: hello!
AI: Hello! How can I help you today?

You: what is the capital of France?
AI: The capital of France is Paris.

You: what did I just ask you about?
AI: You just asked me about the capital of France!

You: exit
AI: Goodbye! Have a great day!
```

## How It Works
- The bot uses `google.generativeai` to connect to Google's powerful LLMs.
- It specifically initializes the `gemini-1.5-flash` model which is optimized for fast, general-purpose text tasks.
- It uses `.start_chat(history=[])` to maintain an ongoing session, allowing the AI to remember the context of your current conversation loop.

---
*This project was created to demonstrate how to build and integrate real generative AI into Python applications securely.*
