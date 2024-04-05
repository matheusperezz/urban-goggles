char = input()
text = input().split(" ")
total_words = len(text)
words_with_char = 0

for w in text:
    if char in w:
        words_with_char += 1

percent = (words_with_char / total_words) * 100
print("{:.1f}".format(percent))