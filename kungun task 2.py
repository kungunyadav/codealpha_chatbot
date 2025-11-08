responses = {
    "hello": "Hi! How are you?",
    "how are you": "I am fine, thank you! How about you?",
    "bye": "Goodbye! See you later."
}

print("Chatbot started. Type anything ('bye' to exit).")

while True:
    user_input = input("You: ").lower()
    if user_input in responses:
        print("Bot: " + responses[user_input])
        if user_input == "bye":
            break
    else:
        print("Bot: Sorry, I don't understand that.")