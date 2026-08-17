import random

responses = {
    "hello": [
        "Hello! How can I help you today?",
        "Hi! Welcome to Student Support.",
        "Hey! What can I help you with?"
    ],

    "course": [
        "You can check your college portal for available courses.",
        "Please contact your department for detailed course information."
    ],

    "attendance": [
        "You can check your attendance through the college portal.",
        "For attendance-related queries, contact your class coordinator."
    ],

    "exam": [
        "Exam schedules are usually available on the college notice board or portal.",
        "Please check with your department for the latest examination updates."
    ],

    "fees": [
        "For fee-related information, please contact the accounts department.",
        "You can check the student portal for your fee details."
    ],

    "library": [
        "The library provides books and digital learning resources.",
        "For book availability, check with the library department."
    ],

    "help": [
        "I can help with courses, attendance, exams, fees and library queries."
    ]
}


def get_response(message):
    message = message.lower()

    for keyword in responses:
        if keyword in message:
            return random.choice(responses[keyword])

    return "Sorry, I didn't understand. Try asking about courses, attendance, exams, fees or library."


print("=" * 45)
print("          CAMPUSASSIST AI")
print("=" * 45)
print("Type 'bye' to exit the chatbot.\n")

while True:
    user_message = input("You: ")

    if user_message.lower() == "bye":
        print("Bot: Thank you! Have a great day.")
        break

    print("Bot:", get_response(user_message))
