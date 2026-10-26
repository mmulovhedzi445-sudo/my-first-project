print("Hello! I am your learning chatbot.")
print("I can answer simple questions.")

while True:
    question = input(
        "Ask me something (type 'bye' to exit): "
    ).lower()

    if question == "bye":
        print("Goodbye! Keep learning Python and AI.")
        break

    elif "python" in question:
        print("Python is a programming language.")

    elif "ai" in question or "artificial intelligence" in question:
        print("AI helps computers perform tasks that usually need human intelligence.")

    elif "hello" in question or "hi" in question:
        print("Hello! How can I help you?")

    else:
        print("I don't know that answer yet. I am still learning!")
