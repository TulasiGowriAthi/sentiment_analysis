# Simple Sentiment Analysis Program

positive_words = ["good", "great", "happy", "love", "excellent", "awesome", "amazing"]
negative_words = ["bad", "sad", "hate", "poor", "terrible", "awful", "worst"]

text = input("Enter a sentence: ").lower()

positive_count = 0
negative_count = 0

words = text.split()

for word in words:
    if word in positive_words:
        positive_count += 1
    elif word in negative_words:
        negative_count += 1

if positive_count > negative_count:
    print("Sentiment: Positive 😊")
elif negative_count > positive_count:
    print("Sentiment: Negative 😞")
else:
    print("Sentiment: Neutral 😐")
