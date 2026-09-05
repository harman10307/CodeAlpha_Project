# TASK 4: BASIC CHATBOT

# Function to generate chatbot responses
def chatbot_response(user_input):

    # Convert input to lowercase
    user_input = user_input.lower().strip()

    if user_input == "hello" or user_input == "hi":
        return "Hi! Nice to meet you."

    elif user_input == "how are you":
        return "I'm fine, thanks!"

    elif user_input == "what is your name":
        return "My name is PythonBot."

    elif user_input == "what can you do":
        return "I can chat with you using predefined responses."

    elif user_input == "thank you" or user_input == "thanks":
        return "You're welcome!"

    elif user_input == "bye":
        return "Goodbye! Have a nice day!"

    else:
        return "Sorry, I don't understand that."


# Main program
print("=" * 50)
print("              BASIC CHATBOT")
print("=" * 50)

print("Chatbot: Hello! I am PythonBot.")
print("Chatbot: Type 'bye' to exit the chatbot.")

# Continuous conversation
while True:

    user_input = input("\nYou: ")

    response = chatbot_response(user_input)

    print("Chatbot:", response)

    # Stop the chatbot when user says bye
    if user_input.lower().strip() == "bye":
        break

print("\nChatbot session ended.")
print("Thank you for chatting!")