import random
i=0
print("Welcome! This is JARVIS Chat bot. For now this can:\n Accept Greetings.\n Evaluate a math problem,Just ask question like 'Can you solve a math question or problem?'\n Exit the application, Just say ' quit' or 'exit'.\n Tell you a joke, Just give a command like- 'Make me laugh' or 'Tell me a joke.'\n")
while i==0:
    Input=input("Talk with JARVIS:")
    if "hi" in Input.lower() or "hello" in Input.lower():
        response=random.choice([
        "Hello! How can I assist you today?",
        "Hi there! What’s on your mind?",
        "Hi! Need any help?",
        "Hello! Great to see you here!",
        "Hey there! How can I help you today?",
        "Hi! Hope you're having a good day!",
        "Hello! What would you like to chat about?",
        "Hey! Ready to get started?",
    ]
    )
        print(response)
    elif "math problem" in Input.lower() or "math question" in Input.lower() or "maths question" in Input.lower() or "maths problem" in Input.lower():
        mathques=input("Sure! Enter your math question:")
        try:
            print("The Result is ",eval(mathques))
        except Exception as e:
            print("Sorry, I couldn't solve the provided question.")
    elif "exit" in Input.lower() or "quit" in Input.lower():
        print("Okay exiting application.....")
        i=1
    elif "joke" in Input.lower() or "laugh" in Input.lower():
        response = random.choice( [
            "Why do programmers prefer dark mode? Because light attracts bugs!",
            "Why did the computer go to the doctor? It had a virus!",
            "Why do Java developers wear glasses? Because they don’t see sharp!",
            "How many programmers does it take to change a light bulb? None, that’s a hardware problem!",
            "Why was the cell phone wearing glasses? It lost its contacts!",
            "Why was the math book sad? It had too many problems!",
            "Why did the function break up with the loop? Because it kept going around in circles!",
            "What do you call 8 hobbits? A hobbyte!",
            "Why don't scientists trust atoms? Because they make up everything!",
            "Why was the computer cold? It left its Windows open!",
            "Why do programmers prefer dark mode? Because light attracts bugs!",
            "Why did the programmer quit his job? Because he didn’t get arrays.",
            "How many programmers does it take to change a light bulb? None. It's a hardware problem.",
            "Why do Java developers wear glasses? Because they don’t see sharp!",
            "I told my computer I needed a break, and now it won’t stop sending me Kit-Kat ads.",
            "Why was the JavaScript developer sad? Because they didn’t know how to 'null' their feelings.",
            "Why can’t a computer play tennis? Because it doesn’t know how to serve!",
            "Why do programmers hate nature? It has too many bugs.",
            "How does a computer get drunk? It takes screenshots!",
            "What’s a programmer’s favorite hangout place? The Foo Bar!"
            ]
            )
        print(response)
    else:
        responses =random.choice( [
        "I'm sorry, I couldn't understand that.",
        "Could you please clarify your question?",
        "I didn’t quite get that. Can you explain it differently?",
        "Sorry, I didn't understand what you meant.",
        "Could you rephrase that?",
        "I'm not sure I follow. Can you elaborate?",
        "That’s a bit confusing for me. Could you clarify?",
        "I didn't quite catch that. Can you say it again?",
        "Can you provide more details?",
        "I'm having trouble understanding. Can you simplify that?"
        ]
        )
        print(responses)
