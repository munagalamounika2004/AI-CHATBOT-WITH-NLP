import nltk
import random
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

nltk.download('punkt')
nltk.download('wordnet')


categories = {
    "famous places": {
        "Rome": {
            "info": "Rome is the capital city of Italy, known for its history and art.",
            "food": "Famous for pasta dishes like Carbonara and Amatriciana.",
            "culture": "Rich Roman heritage, ancient ruins, and renaissance art.",
            "attractions": "Colosseum, Roman Forum, and Vatican City."
        },
        "Paris": {
            "info": "Paris is known for the Eiffel Tower and romantic charm.",
            "food": "Famous for croissants, baguettes, and French wine.",
            "culture": "A hub of fashion, art, and philosophy.",
            "attractions": "Eiffel Tower, Louvre Museum, and Notre-Dame Cathedral."
        },
        "New York": {
            "info": "The Big Apple, known for Times Square and Broadway.",
            "food": "Try iconic New York-style pizza and bagels.",
            "culture": "Melting pot of cultures, vibrant arts, and media scene.",
            "attractions": "Statue of Liberty, Central Park, and Empire State Building."
        },
        "Tokyo": {
            "info": "A blend of tradition and technology in Japan.",
            "food": "Sushi, ramen, and street food like takoyaki.",
            "culture": "Anime, tea ceremonies, and advanced technology.",
            "attractions": "Shibuya Crossing, Tokyo Tower, and historic temples."
        },
        "Cairo": {
            "info": "Home to the Great Pyramids of Giza in Egypt.",
            "food": "Known for dishes like koshari and falafel.",
            "culture": "Ancient Egyptian civilization, Coptic and Islamic traditions.",
            "attractions": "Pyramids of Giza, Egyptian Museum, and Khan el-Khalili."
        },
        "Sydney": {
            "info": "Famous for its Opera House and beaches in Australia.",
            "food": "Seafood is popular; also try meat pies and pavlova.",
            "culture": "Laid-back vibe with strong indigenous and British roots.",
            "attractions": "Sydney Opera House, Bondi Beach, and Harbour Bridge."
        }
    },
    "famous people": {
        "Albert Einstein": {
            "info": "Physicist known for the theory of relativity.",
            "work": "Revolutionized physics with E=mc^2.",
            "birth": "Born in Ulm, Germany in 1879.",
            "achievements": "Won Nobel Prize in Physics in 1921."
        },
        "Leonardo da Vinci": {
            "info": "Renaissance artist and inventor.",
            "work": "Painted the Mona Lisa and The Last Supper.",
            "birth": "Born in Vinci, Italy in 1452.",
            "achievements": "Mastered art, anatomy, and engineering."
        },
        "Marie Curie": {
            "info": "First woman to win a Nobel Prize, known for work on radioactivity.",
            "work": "Discovered polonium and radium.",
            "birth": "Born in Warsaw, Poland in 1867.",
            "achievements": "Won Nobel Prizes in both Physics and Chemistry."
        },
        "Mahatma Gandhi": {
            "info": "Led India's independence movement with non-violence.",
            "work": "Inspired civil rights movements worldwide.",
            "birth": "Born in Porbandar, India in 1869.",
            "achievements": "Known for Satyagraha and non-violent protests."
        },
        "Nelson Mandela": {
            "info": "Anti-apartheid revolutionary and former President of South Africa.",
            "work": "Helped end apartheid and fostered reconciliation.",
            "birth": "Born in Mvezo, South Africa in 1918.",
            "achievements": "Received Nobel Peace Prize in 1993."
        },
        "Steve Jobs": {
            "info": "Co-founder of Apple, revolutionized personal technology.",
            "work": "Introduced iPhone, iPad, and Mac.",
            "birth": "Born in San Francisco, USA in 1955.",
            "achievements": "Pioneered the modern smartphone era."
        }
    },
    "animals": {
        "Elephant": {
            "info": "Largest land animal with strong memory.",
            "habitat": "Savannas, forests, and grasslands.",
            "diet": "Herbivore—eats grass, roots, fruit, and bark.",
            "traits": "Highly social and intelligent."
        },
        "Lion": {
            "info": "Known as the king of the jungle.",
            "habitat": "African savannas and grasslands.",
            "diet": "Carnivore—hunts zebras, wildebeest, etc.",
            "traits": "Live in prides and roar loudly."
        },
        "Dolphin": {
            "info": "Intelligent and playful marine mammal.",
            "habitat": "Oceans and some rivers.",
            "diet": "Carnivore—eats fish and squid.",
            "traits": "Use echolocation and travel in pods."
        },
        "Tiger": {
            "info": "Large striped feline predator.",
            "habitat": "Forests and grasslands in Asia.",
            "diet": "Carnivore—feeds on deer, wild boars.",
            "traits": "Strong swimmers and solitary hunters."
        },
        "Penguin": {
            "info": "Flightless bird adapted to aquatic life.",
            "habitat": "Southern Hemisphere, especially Antarctica.",
            "diet": "Carnivore—eats krill, fish, and squid.",
            "traits": "Waddle and swim expertly."
        },
        "Giraffe": {
            "info": "Tallest land animal with a long neck.",
            "habitat": "Savannas and woodlands in Africa.",
            "diet": "Herbivore—eats leaves from tall trees.",
            "traits": "Gentle and graceful giants."
        }
    },
    "colors": {
        "Blue": {
            "info": "Symbolizes calm, trust, and intelligence.",
            "use": "Used in tech logos and uniforms.",
            "emotion": "Brings peace and productivity."
        },
        "Red": {
            "info": "Represents passion, urgency, and energy.",
            "use": "Seen in warning signs and fashion.",
            "emotion": "Evokes excitement and intensity."
        },
        "Green": {
            "info": "Stands for nature and health.",
            "use": "Popular in eco-friendly branding.",
            "emotion": "Creates a sense of balance and harmony."
        },
        "Yellow": {
            "info": "Associated with sunshine and joy.",
            "use": "Used in smiles, emojis, and road signs.",
            "emotion": "Lifts mood and boosts creativity."
        },
        "Purple": {
            "info": "Symbol of luxury and creativity.",
            "use": "Linked to royalty and imagination.",
            "emotion": "Stimulates problem-solving and introspection."
        },
        "Orange": {
            "info": "Energetic and attention-grabbing.",
            "use": "Seen in sports logos and construction.",
            "emotion": "Encourages enthusiasm and action."
        }
    }
}

lemmatizer = WordNetLemmatizer()

print("=" * 50)
print("🤖 Welcome to the Fun NLP ChatBot! 🤖")
print("Ask me about famous places, people, animals, or colors.")
print("Type 'bye' anytime to exit. Let's chat!")
print("=" * 50)

last_topic = None
last_category = None

fallback_replies = [
    "Sorry, I didn’t quite get that. Try asking about a place, person, animal, or color.",
    "I'm still learning. Can you ask in a different way?",
    "Hmm, not sure I understand. Want to try again?",
    "Oops! That went over my circuits. Try rephrasing?",
    "Interesting! But I need more details. Ask me something like 'Tell me about Tokyo.'"
]

greeting_inputs = ["hi", "hello", "hey", "how are you", "how's it going"]
greeting_responses = [
    "Hey there! I'm doing great, how about you? 😊",
    "Hello! Ready for some fun facts?",
    "Hi! Let’s dive into some trivia!",
    "Hey hey! What are we exploring today?",
    "What's up? I’m always in chat mode."
]

while True:
    user_input = input("You: ").strip().lower()
    if user_input in ["bye", "exit", "quit"]:
        print("ChatBot: Goodbye! 👋")
        break

    if user_input in greeting_inputs:
        print(f"ChatBot: {random.choice(greeting_responses)}")
        continue

    tokens = word_tokenize(user_input)
    tokens = [lemmatizer.lemmatize(word) for word in tokens if word.isalnum()]

    matched = False

    for category, items in categories.items():
        if category in user_input:
            print(f"ChatBot: Here are some {category} you can ask about:")
            for item in items:
                print(f"- {item}")
            matched = True
            break

    if not matched and last_topic and last_category:
        item_info = categories[last_category][last_topic]
        for key in item_info:
            if key in user_input:
                print(f"ChatBot: Here's something about {last_topic}'s {key}: {item_info[key]}")
                matched = True
                break

    if not matched:
        for category, items in categories.items():
            for item, details in items.items():
                if item.lower() in user_input:
                    print(f"ChatBot: Here's something about {item}: {details['info']}")
                    keys = list(details.keys())
                    if len(keys) > 1:
                        print(f"Would you like to know more about their {', '.join(keys[1:])}?")
                    last_topic = item
                    last_category = category
                    matched = True
                    break
            if matched:
                break

    if not matched:
        print(f"ChatBot: {random.choice(fallback_replies)}")




