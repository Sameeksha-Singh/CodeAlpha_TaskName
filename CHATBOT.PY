# Simple Rule-Based Chatbot

def chatbot_response(user_input):
    user_input = user_input.lower()   # convert input to lowercase for matching

    if "hello" in user_input or "hi" in user_input:
        return "Hi! 👋"
    elif "how are you" in user_input:
        return "I'm fine, thanks! How about you?"
    elif "bye" in user_input:
        return "Goodbye! 👋 Have a nice day!"
    else:
        return "Sorry, I don't understand that."

def run_chatbot():
    print("Chatbot: Hello! I'm your simple chatbot. Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        response = chatbot_response(user_input)
        print("Chatbot:", response)

        if "bye" in user_input.lower():
            break

# Run the chatbot
run_chatbot()
