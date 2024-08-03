import spacy

# Load the spaCy model
nlp = spacy.load('en_core_web_sm')

def chatbot_response(user_input):
    doc = nlp(user_input)
    
    if "hello" in doc.text.lower():
        return "Hi there! How can I assist you today?"
    elif "help" in doc.text.lower():
        return "Sure, I can help you with that. What do you need help with?"
    elif "bye" in doc.text.lower():
        return "Goodbye! Have a great day!"
    else:
        return "I'm not sure how to respond to that. Can you please rephrase?"

def chat():
    print("Chatbot: Hello! Type 'bye' to end the chat.")
    while True:
        user_input = input("You: ")
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")
        if "bye" in user_input.lower():
            break

chat()
