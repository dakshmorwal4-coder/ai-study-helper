def explain(topic):
    return f"Here is a simple explanation of {topic}. This feature will be improved using AI soon."

def summarize(text):
    return f"Summary of the text: {text[:50]}..."

def generate_questions(topic):
    return [
        f"What is {topic}?",
        f"Explain {topic} in simple terms.",
        f"Why is {topic} important?"
    ]

if __name__ == "__main__":
    topic = input("Enter a topic: ")
    
    print("\nExplanation:")
    print(explain(topic))
    
    print("\nPractice Questions:")
    for q in generate_questions(topic):
        print("-", q)
