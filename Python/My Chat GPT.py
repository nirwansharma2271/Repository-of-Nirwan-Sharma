import random
print("This is an experimental AI BOT. Use it wisely.")
print("Possible things you can ask to this BOT are:\n     #Greet the bot with a 'hi'\n     #ask the bot about itself? or 'What are you?'\n     #Can you tell me a joke?\n     #Can you solve a math problem?\n     #Exit\n     #Thank the chatbot.")

i = 2
while i > 1:
    m = input("Message Chat BOT:")
    if m.lower() == "hi" or m.lower() == "hello":
        response=random.choice(["Hello! How may I help you?","Hi! How are you doing?","Hello my friend! How are you?","Hello! How may I help you?","Hi! How are you doing?","Hello my friend! How are you?","Hello! How may I help you?","Hi! How are you doing?","Hello my friend! How are you?","Hello! How may I help you?","Hi! How are you doing?","Hello my friend! How are you?"])
        print(response + "\n")
    elif m.lower() == "can you tell me about yourself?" or m.lower() == "what are you?":
        response=random.choice(["I am a chat bot created by NIRWAN SHARMA. I can, for now, only answer the questions on the list.\n","I am a simple chat bot.","I am like chat gpt but very simple.","I am a chat bot created by NIRWAN SHARMA. I can, for now, only answer the questions on the list.\n","I am a simple chat bot.","I am like chat gpt but very simple.""I am a chat bot created by NIRWAN SHARMA. I can, for now, only answer the questions on the list.\n","I am a simple chat bot.","I am like chat gpt but very simple.""I am a chat bot created by NIRWAN SHARMA. I can, for now, only answer the questions on the list.\n","I am a simple chat bot.","I am like chat gpt but very simple."])
        print(response + "\n")
        print()
    elif m.lower() == "exit":
        print("Exiting Program..")
        i = 1
    elif m.lower() == "can you tell me a joke?":
        response = random.choice(["Why don't scientists trust atoms? Because they make up everything!","What did one ocean say to the other ocean? Nothing, they just waved!","What do you get when you cross a snowman and a vampire? Frostbite!", "Why was the math book sad? Because it had too many problems.","Why couldn't the bicycle stand up by itself? Because it was two-tired!","Parallel lines have so much in common. It’s a shame they’ll never meet.",])
        print(response + "\n")
    elif m.lower() == "can you solve a math problem?":
        math_problem = input("Sure, what math problem would you like me to solve?:")
        try:
            result = eval(math_problem)
            print("The result is:", result, "\n")
        except Exception as e:
            print("Sorry, I couldn't solve that math problem. Please enter a valid expression.\n")
    elif m.lower() == "thanks" or m.lower() == "thankyou":
        response=random.choice(["Your Welcome","Welcome!","No problem!","Happy to help you!"])
        print(response)
    else:
        response=random.choice(["Sorry, I could not understand you.","What?","Couldn't understand","I repeat i can only understand the things in the list."])
        print(response)
