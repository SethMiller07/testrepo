# Word counter for song_lyrics.txt
with open("song_lyrics.txt.py", "r") as file:
    lyrics = file.read().lower()
for char in [",", ".", "!", "?", ":", ";"]:
    lyrics = lyrics.replace(char, "")
words = lyrics.split()
word_counts = {}
for i in range(5):
    word = input(f"Enter word {i+1} to count: ").lower()
    word_counts[word] = words.count(word)
print("\nWord Frequencies:")
for word, count in word_counts.items():
    print(f"{word}: {count}")




Twinkle twinkle little star
How I wonder what you are
Up above the world so high
Like a diamond in the sky
