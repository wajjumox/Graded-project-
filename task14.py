#deciding positive and negative feedbacks
positive_words = ["good", "happy", "excellent", "amazing", "great"]
negative_words = ["bad", "sad", "disappointed", "terrible", "poor"]

# feedback analyzation
def analyze_feedback(feedback):
    feedback_words = feedback.lower().split()
    if any(word in feedback_words for word in positive_words):
        return "Positive"
    elif any(word in feedback_words for word in negative_words):
        return "Negative"
    else:
        return "Neutral"

# samples for test analyzation of customers
feedback_list = [
    "The product quality is absolutely fantastic !",
    "I am very disappointed  service.",
    "experince was very good .",
    "damaged item was delivered and it is not good.",
    "The service waa average enough ."
]
for feedback in feedback_list:
    sentiment = analyze_feedback(feedback)
    print(f"Feedback: {feedback}\nSentiment: {sentiment}\n")
