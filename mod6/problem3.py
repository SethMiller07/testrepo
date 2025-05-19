words = ["cat", "tree", "sun", "blue", "sky", "code"]
filtered_words = []
for word in words:
    if len(word) > 3:
        filtered_words.append(word)
print("Filtered list:", filtered_words)
