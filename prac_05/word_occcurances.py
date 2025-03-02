"""
Word Occurrences
Estimate: 20 minutes
Actual:   25 minutes
"""

text = input("Text: ").strip()
words = text.split()
word_counts = {}

for word in words:
    word_counts[word] = word_counts.get(word, 0) + 1

# Sort words alphabetically
sorted_words = sorted(word_counts.keys())

# Find the longest word for alignment
max_length = max(len(word) for word in sorted_words)

# Print word counts with aligned formatting
for word in sorted_words:
    print(f"{word:{max_length}} : {word_counts[word]}")