📌 Project Overview
MEENA is a lightweight, rule-based conversational AI chatbot built in Python. Created as a project for the DecodeLabs AI Internship, it demonstrates fundamental programming concepts such as control flow, conditional logic (if/elif/else), string manipulation, and continuous loops.

Unlike Large Language Models (LLMs), MEENA uses exact-match pattern recognition to respond to specific user commands, making it fast, deterministic, and beginner-friendly.

🚀 Features
Continuous Conversation Loop: Runs indefinitely until the user explicitly asks to exit.

Personalized Interaction: Asks for the user's name at startup and remembers it throughout the session.

20+ Pre-programmed Intents: Recognizes greetings, well-being checks, definitions of tech concepts (AI, ML, Python, Flutter), and system commands.

Built-in Help Menu: Displays a list of available commands at startup and whenever the user types help.

Dynamic Date/Time: Fetches the current system date and time on demand.

Screen Clearing Simulation: Simulates a console wipe using newline characters.

Graceful Error Handling: Catches unrecognized inputs and politely guides the user to the help menu.

🛠️ Prerequisites & Installation
Requirements:

Python 3.6 or higher.

No external libraries or pip installations required (uses only the built-in datetime module).

Installation:

Save the script in a file named meena_bot.py.

Open your terminal or command prompt.

Navigate to the directory containing the file.

🎮 How to Run
Execute the script using Python:

python meena_bot.py
(On some systems, you may need to use python3 meena_bot.py)
