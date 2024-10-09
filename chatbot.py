import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# Initialize lemmatizer
lemmatizer = WordNetLemmatizer()

# Define a function to process user input
def process_input(user_input):
    # Tokenize the input and lemmatize each word
    tokens = word_tokenize(user_input.lower())
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens]
    return lemmatized_tokens

# Define a function to get responses based on keywords
def get_response(user_input):
    # Process user input
    lemmatized_input = process_input(user_input)

    # Define keywords and their corresponding responses
    responses = {
        "castle swimmer": "Castle Swimmer is a story about a mystical castle and its swimmers navigating through challenges.",
        "main characters": "The main characters include Siren, Kappa, Pagoon, Pim, and Queen Nee.",
        "siren": "Siren is a strong-willed character who seeks to break his curse and live freely.",
        "kappa": "Kappa is a significant character connected to prophecies and has a complicated past.",
        "prophecy": "The prophecy reveals challenges and destinies that the characters must face.",
        "chapter 83": "In Chapter 83, Siren learns he is cursed and confronts the burdens of prophecy.",
        "chapter 84": "Chapter 84 discusses the role of mini-gods and the importance of not trusting prophecies.",
        "chapter 85": "Chapter 85 features Pim's apologies and Siren's emotional struggles with his past.",
        "chapter 86": "Chapter 86 shows Siren’s determination to break the curse and his relationship with his friends.",
        "chapter 87": "In Chapter 87, Kappa and Mono face uncertainty about their future after the Mini God is destroyed.",
        "chapter 88": "Chapter 88 highlights Kappa's internal conflict and his connection to another prophecy.",
        "chapter 89": "In Chapter 89, Kappa reunites with Queen Nee and discusses the absence of the beacon and its consequences.",
        "mini-god": "Mini-gods are powerful beings that can curse and share their powers.",
        "queen nee": "Queen Nee is a pivotal character who interacts with Kappa and discusses prophecies.",
        "evil witches": "Kappa refers to his friends as 'evil witches' from the dark seas, which creates confusion.",
        "beacon": "The beacon's absence led to chaos and destruction among the castles.",
        "trust prophecies": "The characters in Castle Swimmer learn that trusting prophecies can lead to dire consequences.",
        "siren's past": "Siren's past is filled with pain and memories that haunt him, particularly related to his mother.",
        "friendship": "The bonds between Siren, Kappa, and their friends are crucial for overcoming challenges.",
        "summary": "Castle Swimmer is an anime that follows the journey of Siren, who battles against curses and prophecies to save his people. Along with his friends, he faces internal struggles, complex relationships, and the weight of destiny as they seek to break free from the constraints of their fates. The story intertwines themes of friendship, sacrifice, and the search for freedom in a mystical underwater world.",
    }

    # Check for keywords or phrases in the user input and respond accordingly
    user_input_lower = user_input.lower()
    for keyword, response in responses.items():
        if keyword in user_input_lower:
            return response

    return "I'm sorry, I don't have information on that topic."

# Main loop for the chatbot
if __name__ == "__main__":
    print("Welcome to the Castle Swimmer Chatbot!")
    print("Ask me anything about Castle Swimmer Chapters 83-89. Type 'exit' to quit.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye!")
            break
        response = get_response(user_input)
        print(f"Chatbot: {response}")
