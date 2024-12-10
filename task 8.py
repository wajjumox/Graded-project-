def count_vowels(feedback):
    vowels = set("aeiouAEIOU")
    count = 0
    for char in feedback:
        if char in vowels:
            count += 1
    return count
def reverse_feedback(feedback):
    return feedback[::-1]
feedback_message = "The service was excellent, but it took long ."
vowel_count = count_vowels(feedback_message)
reversed_feedback = reverse_feedback(feedback_message)
print(f"Original Feedback: {feedback_message}")
print(f"Number of vowels: {vowel_count}")
print(f"Reversed Feedback: {reversed_feedback}")
