# Define predefined rules and responses
rules = {
    "hello": "Hello! How can I assist you today?",
    "how are you": "I'm just a chatbot, but I'm here to help!",
    "what's your name": "I'm a chatbot called CODAI.",
    "bye": "Goodbye! Have a great day!",
}


# Function to process user input and provide appropriate response
def chatbot_response(user_input):
    # Convert user input to lowercase for case-insensitive matching
    user_input = user_input.lower()

    # Search for a matching rule in the predefined rules
    for rule, response in rules.items():
        if rule in user_input:
            return response

    # If no matching rule is found, provide a default response
    return "I'm sorry, I don't understand that."


# Get user input and provide chatbot responses
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    response = chatbot_response(user_input)
    print("CODAI:", response)
