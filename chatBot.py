import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    [r"hi|hello|hey", ["Hello!", "Hi there!", "Hey! How can I help you?"]],
    [r"what is your name?", ["I'm CodTechBot, your friendly internship assistant."]],
    [r"how are you?", ["I'm just a bunch of code, but thanks for asking!"]],
    [r"what can you do?", ["I can chat with you, answer simple questions, and assist during your internship."]],
    [r"bye|exit|quit", ["Goodbye! Best of luck with your internship!", "See you again soon!"]]
]

def main():
    print("🤖 CodTechBot: Hello! Type 'quit' to exit.\n")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    main()
