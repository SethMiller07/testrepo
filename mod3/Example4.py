# 4. Slice a word
word_to_slice = input("Enter a word to slice: ")
first_index = int(input("Enter the first index: "))
last_index = int(input("Enter the last index: "))
sliced_word = word_to_slice[first_index:last_index]
print(sliced_word)
