print("#" * 50) 
print("Welcome to my AI chat bot named MEENA created as a project for DecodeLabs as an AI Intern") 
print("#" * 50) 

# Loop for continuous userInput 
userName = input("Enter your name: ").strip().capitalize() 
print(""" 
 Available Commands: 
 • hi / hello / hey
 • morning / evening / night
 • how are you / your name 
 • who created you / what is my name
 • what is ai / python / flutter / machine learning
 • deep learning / data science
 • status / date / clear
 • bye / exit / quit 
 """) 
while True: 
    userInput = input("Enter Prompt: ").strip().lower() 
    print(userName + ": " + userInput) 
    
    # 1. Standard Greetings
    if userInput in ["hi", "hello", "hey"]: 
        print("MEENA: Hello! Nice to meet you.") 
        
    # 2. Morning Greeting
    elif userInput in ["good morning", "morning"]: 
        print("MEENA: Good Morning! Have a productive day.") 
        
    # 3. Evening Greeting
    elif userInput in ["good evening", "evening"]: 
        print("MEENA: Good Evening!") 
        
    # 4. Night Greeting
    elif userInput in ["good night", "night"]: 
        print("MEENA: Good night! Sleep well.")
        
    # 5. Well-being Check
    elif userInput == "how are you": 
        print("MEENA: I'm functioning perfectly. How about you?") 
        
    # 6. Bot Identity
    elif userInput == "your name": 
        print("MEENA: I'm MEENA, your AI Bot.") 
        
    # 7. Creator Info
    elif userInput in ["who created you", "creator", "decodelabs"]:
        print("MEENA: I was created by an AI Intern at DecodeLabs!")
        
    # 8. User Identity Recall
    elif userInput in ["what is my name", "my name"]:
        print(f"MEENA: Your name is {userName}.")
        
    # 9. Definition: AI
    elif userInput == "what is ai": 
        print("MEENA: Artificial Intelligence enables machines to perform tasks requiring human intelligence.") 
        
    # 10. Definition: Python
    elif userInput == "python": 
        print("MEENA: Python is widely used in AI, Data Science, and Web Development.") 
        
    # 11. Definition: Flutter
    elif userInput == "flutter": 
        print("MEENA: Flutter is Google's framework for building cross-platform apps.") 
        
    # 12. Definition: Machine Learning
    elif userInput == "machine learning": 
        print("MEENA: Machine Learning allows computers to learn from data.") 
        
    # 13. Definition: Deep Learning
    elif userInput == "deep learning":
        print("MEENA: Deep Learning is a subset of ML based on artificial neural networks.")
        
    # 14. Definition: Data Science
    elif userInput == "data science":
        print("MEENA: Data Science combines math, statistics, and code to extract insights from data.")
        
    # 15. System Status Check
    elif userInput in ["status", "system check"]:
        print("MEENA: Systems: 100% operational. Memory: Stable. Core: Active.")
        
    # 16. Current Date/Time Request
    elif userInput in ["date", "time"]:
        import datetime
        now = datetime.datetime.now()
        print(f"MEENA: The current system date and time is: {now.strftime('%Y-%m-%d %H:%M:%S')}")
        
    # 17. User Affirmation
    elif userInput in ["i am good", "fine", "good"]:
        print("MEENA: Glad to hear that! How can I help you today?")
        
    # 18. Clear Screen Simulation
    elif userInput == "clear":
        print("\n" * 50)
        print("MEENA: Chat screen cleared.")
        
    # 19. Help Menu
    elif userInput == "help": 
        print(""" 
 Available Commands: 
 • hi / hello / hey
 • morning / evening / night
 • how are you / your name 
 • who created you / what is my name
 • what is ai / python / flutter / machine learning
 • deep learning / data science
 • status / date / clear
 • bye / exit / quit 
 """) 
 
    # 20. Exit Conditions (Removed duplicates like "Exit" since userInput is converted to lower case)
    elif userInput in ["bye", "exit", "quit", "goodbye", "see you later"]: 
        print("MEENA: Thank you for chatting. Goodbye!") 
        break 
        
    # Fallback Error Catch
    else: 
        print("MEENA: Sorry, I don't understand. Type 'help' to see available commands.")
