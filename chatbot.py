import random
responses = {
    "greeting": ["Hello!", "Hi there!", "Hey!", "Nice to meet you!"],
    "farewell": ["Goodbye!", "See you later!", "Take care!"],
    "thanks": ["You're welcome!", "No problem!", "My pleasure!"],
    "default": ["Sorry, I don't understand.", "Could you please repeat that?", "I'm not sure I follow."],
}

def generate_response(user_input):
    if user_input.lower() in ["hello", "hi", "hey"]:
        return random.choice(responses["greeting"])
    elif user_input.lower() in ["goodbye", "bye"]:
        return random.choice(responses["farewell"])
    elif "thank" in user_input.lower():
        return random.choice(responses["thanks"])
    else:
        return random.choice(responses["default"])


def main():
    print("Chatbot: Hello! How can I assist you today?")
    
    while True:
        user_input = input("You: ")
        response = generate_response(user_input)
        print("Chatbot:", response)

        if user_input.lower() in ["quit", "exit", "bye"]:
            print("Chatbot: Goodbye!")
            break

if __name__ == "__main__":
    main()
