import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    # Greeting
    [
        r"Hi|Hello|Hey|Good Morning|Good Evening",
        ["Hello! Welcome to Book Haven. How can I assist you today?"]
    ],

    # Name query
    [
        r"My name is (.*)",
        ["Hello %1! It's nice to meet you. How can I assist you with your book shopping?"]
    ],

    # Book Inquiry
    [
        r"Can you recommend me a book on (.*)",
        ["We have great books on %1. Here are some suggestions:\n1. 'Sapiens: A Brief History of Humankind' by Yuval Noah Harari\n2. 'The Selfish Gene' by Richard Dawkins\n3. 'Cosmos' by Carl Sagan. Would you like to buy one?"]
    ],

    # Book Search
    [
        r"Do you have (.*) book?",
        ["Yes, we have '%1'. Would you like to add it to your cart?"]
    ],

    # Checkout
    [
        r"I want to buy (.*)",
        ["Great choice! Would you like to check out or continue shopping?"]
    ],

    # Order status
    [
        r"What is the status of my order?",
        ["Please provide your order number and I will check the status for you."]
    ],

    # Offer Inquiry
    [
        r"Do you have any offers?",
        ["Yes, we are offering a 20% discount on all fiction books this week! Check out our 'Deals' section for more."]
    ],

    # Help with browsing
    [
        r"How can I browse books?",
        ["You can browse books by category such as Fiction, Non-fiction, Science, History, and more! Let me know what interests you."]
    ],

    # Return Policy
    [
        r"What is your return policy?",
        ["We accept returns within 30 days if the book is in unused condition. You can contact our customer service for a return label."]
    ],

    # Order tracking
    [
        r"How can I track my order?",
        ["You can track your order by logging into your account or by using the tracking number provided in the confirmation email."]
    ],

    # Cart Inquiry
    [
        r"Add (.*) to my cart",
        ["I have added '%1' to your cart. Would you like to continue shopping or proceed to checkout?"]
    ],

    # Purchase confirmation
    [
        r"Proceed to checkout",
        ["You're all set! Please provide your shipping details to complete the order."]
    ],

    # Payment Methods
    [
        r"What payment methods do you accept?",
        ["We accept Credit/Debit Cards, UPI, and PayPal. How would you like to pay?"]
    ],

    # Book Genres
    [
        r"Tell me about your book categories",
        ["We have a wide range of categories including Fiction, Non-Fiction, Mystery, Romance, Science, History, and more."]
    ],

    # Thank you
    [
        r"Thank you|Thanks",
        ["You're welcome! Happy reading! Let me know if you need any further assistance."]
    ],

    # Goodbye
    [
        r"quit|exit|bye",
        ["Thank you for visiting Book Haven! Have a great day and enjoy your books!"]
    ],

    # Fallback
    [
        r"(.*)",
        ["I'm sorry, I didn't quite understand that. Can you please rephrase your query related to books, orders, or offers?"]
    ]
]

def bookstore_chatbot():
    print("Welcome to Book Haven - Your Online Bookstore!")
    print("Type 'quit' anytime to exit the chat.\n")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    bookstore_chatbot()
