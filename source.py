import re
import random
import io
import sys

# ... (previous code for responses, top_10_data, get_top_10) ...

def provide_python_code(request):
    """Provides Python code based on the user's request."""
    if re.search(r'code for (.*)', request):
        program_type = re.search(r'code for (.*)', request).group(1).strip()

        if program_type == "adding two numbers":
            return """
def add_two_numbers(a, b):
    return a + b
"""
    return "I'm sorry, I don't have code for that yet."


# Predefined responses with at least 20 interactions and arithmetic operations
responses = {
    r'hi|hello|hey': ['Hello! How can I help you today?', 'Hi there! What can I do for you?', 'Hey! Welcome to our support chat.'],
    r'how are you': ['Doing great! Ready to assist you.', 'I\'m doing well, thank you for asking.'],
    r'help|support': ['Sure, what do you need help with?', 'I’m here to assist. Please describe your issue.', 'I can help you with that. What seems to be the problem?'],
    r'pricing|cost|price': ['Our pricing details can be found on our website.', 'We offer competitive pricing. Would you like a link to pricing?', 'Please visit our website for detailed pricing information.'],
    r'contact|email|phone': ['You can reach us at support@example.com or call 123-456-7890.', 'Our contact information is available on the website.', 'For support, please email us at support@example.com.'],
    r'(.) problem (.)': ['I\'m sorry to hear that. Can you describe your problem in more detail?', 'Please provide more information about the issue you\'re facing.', 'I understand you\'re having a problem. Can you elaborate?'],
    r'bye|goodbye': ['Goodbye! Have a great day.', 'See you later!', 'Thanks for chatting with us. Goodbye!'],
    r'thanks|thank you': ['You\'re welcome!', 'Happy to help!', 'My pleasure!'],
    r'features|what can you do': ['I can answer your questions, provide support, and direct you to resources.', 'I\'m here to assist with pricing, contact information, and troubleshooting.', 'I can help you with a variety of tasks, including finding information and resolving issues.'],
    r'your name|what are you called': ['I\'m a customer support bot.', 'You can call me the SupportBot.'],  # I don\'t have a name, but I'm here to help.'],
    r'weather|temperature': ['I do not have access to real-time information, including weather.', 'I\'m sorry, I can\'t provide weather updates.', 'Please check a weather app or website for current conditions.'],
    r'time|date': ['I do not have access to real-time information, including the current time and date.'],
    r'location|where are you': ['I am a virtual assistant and do not have a physical location.', 'I exist within the digital realm.', 'I am here to help you, wherever you are.'],
    r'joke|tell me a joke': ['Why don\'t scientists trust atoms? Because they make up everything!', 'Parallel lines have so much in common. It\'s a shame they\'ll never meet.'],
    r'calculate (\d+) ([\+\-\*\/]) (\d+)': lambda match: f"{match.group(1)} {match.group(2)} {match.group(3)} = {eval(match.group(0)[9:])}",  # Arithmetic operations
    r'top 10 (?:players|people) in (.*)': lambda match: get_top_10(match.group(1)),  # Top 10 players/people in a field
    r'add (\d+) \+ (\d+)': lambda match: f"The sum of {match.group(1)} and {match.group(2)} is {int(match.group(1)) + int(match.group(2))}", # Addition operation with response variations
    r'add (\d+)\+(\d+)': lambda match: f"The sum of {match.group(1)} and {match.group(2)} is {int(match.group(1)) + int(match.group(2))}",  # Addition with '+' sign
    r'code for (.*)': lambda match: provide_python_code(match.group(0)),  # Add this line
     r'calculate (\d+) ([\+\-\*\/]) (\d+)': lambda match: f"{match.group(1)} {match.group(2)} {match.group(3)} = {eval(match.group(0)[9:])}",  # Arithmetic operations (existing)

    r'subtract (\d+) - (\d+)': lambda match: f"{match.group(1)} - {match.group(2)} = {int(match.group(1)) - int(match.group(2))}",  # Subtraction
    r'multiply (\d+) \* (\d+)': lambda match: f"{match.group(1)} * {match.group(2)} = {int(match.group(1)) * int(match.group(2))}",  # Multiplication

    r'(.*)': ['Can you please rephrase that?', 'I\'m not sure I understand. Could you clarify?', 'I didn\'t quite catch that. Could you try again?']
}


# Data for top 10 in different fields (example)
top_10_data = {
    "football": ["Lionel Messi", "Cristiano Ronaldo", "Neymar Jr.", "Kylian Mbappé", "Robert Lewandowski", "Erling Haaland", "Kevin De Bruyne", "Virgil van Dijk", "Mohamed Salah", "Harry Kane"],
    "basketball": ["LeBron James", "Kevin Durant", "Stephen Curry", "Giannis Antetokounmpo", "Luka Dončić", "Nikola Jokić", "Joel Embiid", "Jayson Tatum", "Damian Lillard", "James Harden"],
    "cricket": ["MS Dhoni", "Virat Kohli", "Kane Williamson", "Steve Smith", "Joe Root", "Rashid Khan", "Shakib Al Hasan", "Trent Boult", "Kagiso Rabada", "Jasprit Bumrah"]
    # Add more fields and data as needed
}




def get_top_10(field):
    field = field.lower()
    if field in top_10_data:
        return f"Top 10 in {field}:\n{', '.join(top_10_data[field])}"
    else:
        return "I don't have information about the top 10 in that field."

def chatbot_response(user_input):
    user_input = user_input.lower()
    for pattern, replies in responses.items():
        match = re.search(pattern, user_input)
        if match:
            if callable(replies):  # Check if the response is a function
                return replies(match)
            else:
                return random.choice(replies)
    return "I'm not sure I understand. Could you clarify?"

def chat():
    print("Customer Support Bot: Hi! Type 'exit' to end the chat.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Customer Support Bot: Thank you for chatting with us. Goodbye!")
            break
        print("Customer Support Bot:", chatbot_response(user_input))

# Run the chatbot
chat()
